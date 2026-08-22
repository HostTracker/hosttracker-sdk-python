"""httpx transport wrappers that carry the SDK's request policy.

Everything that has to happen around a single HTTP exchange lives here, in ONE place,
so it applies identically to the generated ``sync``/``sync_detailed``/``asyncio``/
``asyncio_detailed`` entry points and to the hand-written helpers:

* stamp ``Idempotency-Key`` on mutating calls (``idempotency="auto"``),
* retry per the published policy - re-sending the SAME request object, so a retried
  write replays under the SAME idempotency key,
* map every failure onto :class:`hosttracker.errors.HostTrackerError`.

A caller's own transport (proxy, custom TLS, ``httpx.MockTransport``) slots underneath
and keeps all of it.
"""

from __future__ import annotations

import random
import time
import uuid
from collections.abc import Iterator
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass
from typing import Literal

import anyio
import httpx

from .errors import (
    _parse_retry_after,
    error_from_response,
    network_error,
    problem_code_of,
)

__all__ = ["HtAsyncTransport", "HtTransport", "RequestPolicy", "idempotency_key"]

IdempotencyMode = Literal["auto", "off"]

IDEMPOTENCY_HEADER = "Idempotency-Key"

#: HTTP methods that carry an idempotency key under ``idempotency="auto"``.
_MUTATING = frozenset({"POST", "PATCH", "PUT", "DELETE"})

#: Methods that are safe to replay without an idempotency key.
_SAFE = frozenset({"GET", "HEAD", "OPTIONS"})

#: The only 429 the SDK replays. `quota_exceeded` shares the status and must NEVER be
#: retried - the window is spent - and any other named code is one the SDK cannot judge.
#: A 429 with NO problem body is the per-IP+endpoint throttle: wait and retry.
_RETRYABLE_429_CODES = frozenset({"rate_limited"})

#: Same rule for 503, and only when the server actually named a wait.
_RETRYABLE_503_CODES = frozenset({"service_unavailable"})

_explicit_key: ContextVar[str | None] = ContextVar("hosttracker_idempotency_key", default=None)


@contextmanager
def idempotency_key(key: str) -> Iterator[None]:
    """Pin an explicit ``Idempotency-Key`` on the mutating call made inside the block.

    Scope it to exactly ONE call: the API keys a stored response by
    ``key + resolved path + body``, so reusing a key with a different body is a
    ``409 idempotency_key_conflict``.

    ::

        with idempotency_key("order-4711"):
            ht.monitors.create_monitor(body=req)

    The client's per-call ``idempotency_key=`` keyword does exactly this around one call.
    """
    token = _explicit_key.set(key)
    try:
        yield
    finally:
        _explicit_key.reset(token)


@dataclass
class RequestPolicy:
    """Retry / idempotency / error-raising knobs shared by both transports."""

    max_retries: int = 2
    idempotency: IdempotencyMode = "auto"
    raise_on_error: bool = True
    #: Upper bound honoured for a server-supplied ``Retry-After`` (seconds).
    max_retry_after: float = 60.0
    #: First backoff step when no ``Retry-After`` is available (seconds).
    backoff_base: float = 0.2
    #: Ceiling for the computed backoff (seconds).
    backoff_max: float = 5.0
    #: Set False in tests to keep sleeps deterministic.
    jitter: bool = True
    user_agent: str | None = None


def _is_query_twin(request: httpx.Request) -> bool:
    """True for the ``POST <path>/q`` body-query twins - reads wearing a POST."""
    return request.method == "POST" and request.url.path.endswith("/q")


def _replayable(request: httpx.Request) -> bool:
    """A request may only be re-sent when its body is fully buffered in memory.

    httpx materialises ``json=``/``content=bytes`` bodies eagerly (``_content``); a
    streaming upload is not replayable and is never retried.
    """
    return hasattr(request, "_content")


def _stamp(request: httpx.Request, policy: RequestPolicy) -> None:
    """Apply User-Agent and the idempotency key before the first send."""
    if policy.user_agent:
        request.headers["User-Agent"] = policy.user_agent

    explicit = _explicit_key.get()
    if explicit:
        request.headers[IDEMPOTENCY_HEADER] = explicit
        return
    if IDEMPOTENCY_HEADER in request.headers:
        return
    if policy.idempotency != "auto":
        return
    if request.method not in _MUTATING or _is_query_twin(request):
        return
    request.headers[IDEMPOTENCY_HEADER] = str(uuid.uuid4())


def _retry_allowed_for(request: httpx.Request) -> bool:
    """Is this request shaped so a replay cannot duplicate a side effect?

    Safe methods and the ``/q`` read twins always are; a write only when it carries an
    ``Idempotency-Key``, which the default ``idempotency="auto"`` guarantees.
    """
    if request.method in _SAFE or _is_query_twin(request):
        return True
    return IDEMPOTENCY_HEADER in request.headers


def _should_retry_status(request: httpx.Request, response: httpx.Response) -> bool:
    """The published retry policy, read off the answered response."""
    status = response.status_code
    if status not in (429, 503):
        return False
    if not _retry_allowed_for(request):
        return False
    code = problem_code_of(response.content)
    if status == 429:
        return code is None or code in _RETRYABLE_429_CODES
    # 503: only when the server named a wait. A bare 503 could be anything.
    if response.headers.get("Retry-After") is None:
        return False
    return code is None or code in _RETRYABLE_503_CODES


def _should_retry_transport(request: httpx.Request) -> bool:
    """Transport failures are replayed for reads only (GET/HEAD/OPTIONS and ``/q``).

    A write that never got an answer may already have been applied server-side, so the
    decision to re-submit is left to the caller.
    """
    return request.method in _SAFE or _is_query_twin(request)


def _delay(policy: RequestPolicy, response: httpx.Response | None, attempt: int) -> float:
    """Seconds to wait before retry ``attempt`` (1-based)."""
    if response is not None:
        server = _parse_retry_after(response.headers.get("Retry-After"))
        if server is not None:
            return min(server, policy.max_retry_after)
    # Full jitter: a uniform draw from [0, ceiling), which spreads a thundering herd.
    ceiling = min(policy.backoff_base * (2 ** (attempt - 1)), policy.backoff_max)
    return random.uniform(0.0, ceiling) if policy.jitter else ceiling  # noqa: S311 - jitter, not cryptography


class HtTransport(httpx.BaseTransport):
    """Synchronous policy wrapper around any other httpx transport."""

    def __init__(self, inner: httpx.BaseTransport, policy: RequestPolicy) -> None:
        self._inner = inner
        self._policy = policy

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        policy = self._policy
        _stamp(request, policy)
        attempt = 0
        while True:
            try:
                response = self._inner.handle_request(request)
            except httpx.TransportError as exc:
                if attempt < policy.max_retries and _should_retry_transport(request) and _replayable(request):
                    attempt += 1
                    time.sleep(_delay(policy, None, attempt))
                    continue
                raise network_error(request, exc) from exc

            if response.status_code < 400:
                return response

            # Read here so the policy can branch on the problem `code` and the error can
            # carry the whole document. `read()` also closes the stream.
            response.read()
            if attempt < policy.max_retries and _should_retry_status(request, response) and _replayable(request):
                attempt += 1
                time.sleep(_delay(policy, response, attempt))
                continue
            if policy.raise_on_error:
                raise error_from_response(request, response)
            return response

    def close(self) -> None:
        self._inner.close()


class HtAsyncTransport(httpx.AsyncBaseTransport):
    """Asynchronous twin of :class:`HtTransport` - identical policy, awaited sleeps."""

    def __init__(self, inner: httpx.AsyncBaseTransport, policy: RequestPolicy) -> None:
        self._inner = inner
        self._policy = policy

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        policy = self._policy
        _stamp(request, policy)
        attempt = 0
        while True:
            try:
                response = await self._inner.handle_async_request(request)
            except httpx.TransportError as exc:
                if attempt < policy.max_retries and _should_retry_transport(request) and _replayable(request):
                    attempt += 1
                    await anyio.sleep(_delay(policy, None, attempt))
                    continue
                raise network_error(request, exc) from exc

            if response.status_code < 400:
                return response

            await response.aread()
            if attempt < policy.max_retries and _should_retry_status(request, response) and _replayable(request):
                attempt += 1
                await anyio.sleep(_delay(policy, response, attempt))
                continue
            if policy.raise_on_error:
                raise error_from_response(request, response)
            return response

    async def aclose(self) -> None:
        await self._inner.aclose()
