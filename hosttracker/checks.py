"""Running an instant check end to end.

``POST /check`` is asynchronous and poll-based - no streaming, no websocket. It answers
``202`` with the identifiers, a first ``retryAfter``, and a ``resultUrl``. FOLLOW that
url rather than building a path: an instant check is addressed by the PAIR ``(dbId, id)``.
Only its path and query are followed: the scheme and host always stay the client's own,
so the bearer token can never reach an origin the caller did not configure.

The poll answer is incremental - ``events[]`` grows as fleet locations report - and every
non-terminal poll carries a fresh ``retryAfter``. ``state == "done"`` is the exit.
"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING, Any
from urllib.parse import urlsplit, urlunsplit

import anyio

from ._generated.types import Unset
from .errors import CODE_HTTP_ERROR, CODE_TIMEOUT, HostTrackerError

if TYPE_CHECKING:  # pragma: no cover - typing only
    from ._generated.models import IcCreateRequest, IcResultView
    from .client import AsyncHostTracker, HostTracker

# The generated api/model packages are imported inside the functions below: touching a
# generated operation loads ~1050 model modules, and `import hosttracker` must stay cheap.

__all__ = ["arun_check", "run_check"]

DEFAULT_POLL_INTERVAL = 2.0
MAX_POLL_INTERVAL = 30.0

#: The only schemes a server-supplied result url may name.
ALLOWED_RESULT_SCHEMES = frozenset({"http", "https"})


def _as_request(body: IcCreateRequest | dict[str, Any]) -> IcCreateRequest:
    """Accept either the generated request model or a plain camelCase dict."""
    from ._generated.models import IcCreateRequest as _IcCreateRequest

    if isinstance(body, _IcCreateRequest):
        return body
    return _IcCreateRequest.from_dict(body)


def _unset_to_none(value: Any) -> Any:
    return None if isinstance(value, Unset) else value


def _result_location(client: Any, created: Any, response: Any) -> str | None:
    """The url to poll: the body's ``resultUrl``, else the ``Location`` header, rebased."""
    url = _unset_to_none(getattr(created, "result_url", None))
    if not url:
        url = getattr(response, "headers", {}).get("Location")
    return _rebase(client.base_url, str(url)) if url else None


def _rebase(base_url: str, raw: str) -> str:
    """Path and query from the server, scheme and host from the configured base url.

    The bearer token rides every request this client makes, so a server-supplied url
    naming a foreign origin is never dialled: only its path and query survive. A scheme
    the SDK does not speak is refused outright, before any request goes out.
    """
    location = urlsplit(raw.strip())
    if location.scheme and location.scheme.lower() not in ALLOWED_RESULT_SCHEMES:
        raise HostTrackerError(
            code=CODE_HTTP_ERROR,
            title="Refusing to follow a result url",
            detail=(
                "the server returned a result URL the SDK will not follow: "
                f"scheme {location.scheme!r} is neither http nor https"
            ),
            method="GET",
            url=raw,
        )
    base = urlsplit(base_url)
    path = location.path if location.path.startswith("/") else "/" + location.path
    return urlunsplit((base.scheme, base.netloc, base.path.rstrip("/") + path, location.query, ""))


def _poll_delay(view: Any, floor: float | None) -> float:
    if floor is not None:
        return max(0.0, floor)
    retry_after = _unset_to_none(getattr(view, "retry_after", None))
    if retry_after is None:
        return DEFAULT_POLL_INTERVAL
    return min(max(float(retry_after), 0.0), MAX_POLL_INTERVAL)


def _is_done(view: Any) -> bool:
    state = _unset_to_none(getattr(view, "state", None))
    return str(state) == "done" if state is not None else False


def _timed_out(view: Any, timeout: float) -> HostTrackerError:
    state = _unset_to_none(getattr(view, "state", None))
    return HostTrackerError(
        code=CODE_TIMEOUT,
        title="Timed out waiting for instant check",
        detail=(
            f"instant check {getattr(view, 'db_id', '?')}/{getattr(view, 'id', '?')} was still "
            f"in state {state or 'unknown'!r} after {timeout:g}s"
        ),
    )


def run_check(
    client: HostTracker,
    body: IcCreateRequest | dict[str, Any],
    *,
    timeout: float = 120.0,
    poll_interval: float | None = None,
    on_poll: Any = None,
    idempotency_key: str | None = None,
) -> IcResultView:
    """Start an instant check and poll it to completion.

    ::

        result = ht.run_check({"url": "https://www.host-tracker.com", "type": "http"})
        for event in result.events:
            print(event.location, event.state)

    Args:
        client: A :class:`~hosttracker.HostTracker` with the ``check:write`` and
            ``check:read`` scopes.
        body: ``IcCreateRequest`` or the equivalent dict; minimally ``{url, type}``.
        timeout: Overall client-side deadline in seconds. The check keeps running
            server-side after a timeout; the pair ``(dbId, id)`` still resolves.
        poll_interval: Fixed seconds between polls. Omit to honour the server's
            ``retryAfter``, which is sized to the check type.
        on_poll: Optional callback invoked with each intermediate ``IcResultView`` -
            useful because ``events[]`` grows as locations report.
        idempotency_key: Optional caller-chosen key for the create call.
    """
    from ._generated.api.instant_checks import create_instant_check

    kwargs: dict[str, Any] = {}
    if idempotency_key is not None:
        kwargs["idempotency_key"] = idempotency_key
    response = create_instant_check.sync_detailed(client=client.raw, body=_as_request(body), **kwargs)
    created = response.parsed
    result_url = _result_location(client, created, response)

    deadline = time.monotonic() + timeout
    first_wait = _unset_to_none(getattr(created, "retry_after", None))
    delay = poll_interval if poll_interval is not None else (float(first_wait) if first_wait is not None else 0.0)
    view: Any = created
    while True:
        time.sleep(min(max(delay, 0.0), max(deadline - time.monotonic(), 0.0)))
        view = _fetch(client, created, result_url)
        if on_poll is not None:
            on_poll(view)
        if _is_done(view):
            return view  # type: ignore[return-value]
        if time.monotonic() >= deadline:
            raise _timed_out(view, timeout)
        delay = _poll_delay(view, poll_interval)


def _fetch(client: HostTracker, created: Any, result_url: str | None) -> IcResultView:
    from ._generated.api.instant_checks import get_instant_check
    from ._generated.models import IcResultView

    if result_url:
        # Already rebased onto the configured host by `_result_location`.
        raw = client.httpx_client.get(result_url)
        return IcResultView.from_dict(raw.json())
    # No resultUrl and no Location: fall back to the generated operation, which builds the
    # path from the spec rather than by hand.
    return get_instant_check.sync(  # type: ignore[return-value]
        _unset_to_none(getattr(created, "db_id", None)),
        _unset_to_none(getattr(created, "id", None)),
        client=client.raw,
    )


async def arun_check(
    client: AsyncHostTracker,
    body: IcCreateRequest | dict[str, Any],
    *,
    timeout: float = 120.0,
    poll_interval: float | None = None,
    on_poll: Any = None,
    idempotency_key: str | None = None,
) -> IcResultView:
    """Async twin of :func:`run_check`."""
    from ._generated.api.instant_checks import create_instant_check

    kwargs: dict[str, Any] = {}
    if idempotency_key is not None:
        kwargs["idempotency_key"] = idempotency_key
    response = await create_instant_check.asyncio_detailed(client=client.raw, body=_as_request(body), **kwargs)
    created = response.parsed
    result_url = _result_location(client, created, response)

    deadline = time.monotonic() + timeout
    first_wait = _unset_to_none(getattr(created, "retry_after", None))
    delay = poll_interval if poll_interval is not None else (float(first_wait) if first_wait is not None else 0.0)
    view: Any = created
    while True:
        await anyio.sleep(min(max(delay, 0.0), max(deadline - time.monotonic(), 0.0)))
        view = await _afetch(client, created, result_url)
        if on_poll is not None:
            on_poll(view)
        if _is_done(view):
            return view  # type: ignore[return-value]
        if time.monotonic() >= deadline:
            raise _timed_out(view, timeout)
        delay = _poll_delay(view, poll_interval)


async def _afetch(client: AsyncHostTracker, created: Any, result_url: str | None) -> IcResultView:
    from ._generated.api.instant_checks import get_instant_check
    from ._generated.models import IcResultView

    if result_url:
        # Already rebased onto the configured host by `_result_location`.
        raw = await client.httpx_client.get(result_url)
        return IcResultView.from_dict(raw.json())
    return await get_instant_check.asyncio(  # type: ignore[return-value]
        _unset_to_none(getattr(created, "db_id", None)),
        _unset_to_none(getattr(created, "id", None)),
        client=client.raw,
    )
