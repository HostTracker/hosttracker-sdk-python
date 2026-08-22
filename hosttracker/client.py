"""The client callers construct: :class:`HostTracker` and :class:`AsyncHostTracker`.

Both are thin, hand-written wrappers over the generated client. They own configuration
(base url, token, timeout, User-Agent, retry/idempotency policy), expose every generated
operation grouped by its tag, and carry the helpers that need more than one round trip
(:mod:`hosttracker.paging`, :mod:`hosttracker.jobs`, :mod:`hosttracker.checks`).
"""

from __future__ import annotations

import functools
import importlib
import inspect
import ssl
import typing
import uuid
from collections.abc import AsyncIterator, Callable, Iterator
from types import ModuleType
from typing import TYPE_CHECKING, Any

import httpx

from ._generated.client import AuthenticatedClient
from ._transport import (
    HtAsyncTransport,
    HtTransport,
    IdempotencyMode,
    RequestPolicy,
)
from ._transport import (
    idempotency_key as _idempotency_key,
)
from ._version import __version__

if TYPE_CHECKING:  # pragma: no cover - typing only
    from ._generated.models import IcCreateRequest, IcResultView, JobView

__all__ = ["DEFAULT_BASE_URL", "TAGS", "AsyncHostTracker", "HostTracker"]

#: Production. v2 has no path version prefix - a future breaking version gets a new
#: hostname rather than a `/v3` segment.
DEFAULT_BASE_URL = "https://api2.host-tracker.com"

DEFAULT_TIMEOUT = 30.0

_API_PACKAGE = "hosttracker._generated.api"

#: The operation families the API publishes. ``ht.<tag>.<operation_id>(...)`` reaches every
#: generated operation; ``hosttracker._generated.api.<tag>.<operation_id>`` is the same
#: function with full static typing.
TAGS: tuple[str, ...] = (
    "account",
    "alerts",
    "contacts",
    "incidents",
    "instant_checks",
    "jobs",
    "maintenance",
    "monitoring_locations",
    "monitors",
    "monitor_types",
    "reports",
    "results",
    "status_pages",
    "webhooks",
)


def default_user_agent(suffix: str | None = None) -> str:
    """``hosttracker-sdk-python/<version>``, plus the caller's own token when given."""
    base = f"hosttracker-sdk-python/{__version__}"
    return f"{base} {suffix}" if suffix else base


@functools.cache
def _accepts_idempotency_key(fn: Callable[..., Any]) -> bool:
    """Does this generated operation declare the ``Idempotency-Key`` header parameter?"""
    try:
        return "idempotency_key" in inspect.signature(fn).parameters
    except (TypeError, ValueError):  # pragma: no cover - builtins
        return False


@functools.cache
def _requires_idempotency_key(fn: Callable[..., Any]) -> bool:
    """Is the ``Idempotency-Key`` header MANDATORY on this operation?

    The spec marks it required on nine operations (the bulk doors, ``resetMonitorStats``,
    ``generateReport``, the two status-page incident writers); the SDK fills it in.
    """
    try:
        parameter = inspect.signature(fn).parameters.get("idempotency_key")
    except (TypeError, ValueError):  # pragma: no cover - builtins
        return False
    return parameter is not None and parameter.default is inspect.Parameter.empty


@functools.cache
def _body_model(fn: Callable[..., Any]) -> type | None:
    """The request-body model this operation declares, when it declares one."""
    try:
        parameter = inspect.signature(fn).parameters.get("body")
    except (TypeError, ValueError):  # pragma: no cover - builtins
        return None
    if parameter is None:
        return None
    # The annotation is either the model itself or `Model | Unset` when the body is
    # optional; take the single member that knows how to build itself from a dict.
    candidates = [
        member
        for member in (typing.get_args(parameter.annotation) or (parameter.annotation,))
        if isinstance(member, type) and hasattr(member, "from_dict")
    ]
    return candidates[0] if len(candidates) == 1 else None


class _ApiGroup:
    """One operation family, resolved lazily.

    ``ht.monitors`` is one of these; ``ht.monitors.list_monitor`` imports
    ``hosttracker._generated.api.monitors.list_monitor`` on first touch and returns a
    callable already bound to this client.
    """

    __slots__ = ("_bound", "_client", "_idempotency", "_is_async", "_tag")

    def __init__(self, tag: str, client: Any, is_async: bool, idempotency: str = "auto") -> None:
        self._tag = tag
        self._client = client
        self._is_async = is_async
        self._idempotency = idempotency
        self._bound: dict[str, Callable[..., Any]] = {}

    def __repr__(self) -> str:  # pragma: no cover - REPL aid
        return f"<hosttracker api group {self._tag!r}>"

    def module(self, operation_id: str) -> ModuleType:
        """The raw generated module for one operation (``sync``/``asyncio``/...)."""
        return importlib.import_module(f"{_API_PACKAGE}.{self._tag}.{operation_id}")

    def __dir__(self) -> list[str]:
        package = importlib.import_module(f"{_API_PACKAGE}.{self._tag}")
        path = list(getattr(package, "__path__", []))
        names: list[str] = []
        if path:
            import pkgutil

            names = [m.name for m in pkgutil.iter_modules(path)]
        return sorted({*names, *super().__dir__()})

    def __getattr__(self, name: str) -> Callable[..., Any]:
        if name.startswith("_"):
            raise AttributeError(name)
        cached = self._bound.get(name)
        if cached is not None:
            return cached
        try:
            module = self.module(name)
        except ModuleNotFoundError as exc:
            raise AttributeError(
                f"{self._tag!r} has no operation {name!r}. "
                f"Operation names are the OpenAPI operationIds in snake_case; "
                f"dir(client.{self._tag}) lists them."
            ) from exc
        bound = self._bind(module, name)
        self._bound[name] = bound
        return bound

    def _bind(self, module: ModuleType, name: str) -> Callable[..., Any]:
        if self._is_async:

            async def call_async(*args: Any, detailed: bool = False, idempotency_key: str | None = None, **kwargs: Any):
                fn = getattr(module, "asyncio_detailed" if detailed else "asyncio")
                args, kwargs = self._prepare(fn, args, kwargs, idempotency_key, self._idempotency)
                if idempotency_key is not None and "idempotency_key" not in kwargs:
                    with _idempotency_key(idempotency_key):
                        return await fn(*args, client=self._client, **kwargs)
                return await fn(*args, client=self._client, **kwargs)

            call_async.__name__ = name
            call_async.__doc__ = (getattr(module, "asyncio", None) or module).__doc__
            return call_async

        def call(*args: Any, detailed: bool = False, idempotency_key: str | None = None, **kwargs: Any):
            fn = getattr(module, "sync_detailed" if detailed else "sync")
            args, kwargs = self._prepare(fn, args, kwargs, idempotency_key, self._idempotency)
            if idempotency_key is not None and "idempotency_key" not in kwargs:
                with _idempotency_key(idempotency_key):
                    return fn(*args, client=self._client, **kwargs)
            return fn(*args, client=self._client, **kwargs)

        call.__name__ = name
        call.__doc__ = (getattr(module, "sync", None) or module).__doc__
        return call

    @staticmethod
    def _prepare(
        fn: Callable[..., Any],
        args: tuple[Any, ...],
        kwargs: dict[str, Any],
        key: str | None,
        idempotency_mode: str = "auto",
    ) -> tuple[tuple[Any, ...], dict[str, Any]]:
        """Coerce a ``dict`` body into the operation's request model and place the key.

        A model instance passes through untouched. A per-call idempotency key goes to the
        operation's own ``idempotency_key`` parameter where the spec declares one;
        otherwise the transport applies it.
        """
        body = kwargs.get("body")
        if isinstance(body, dict):
            model = _body_model(fn)
            if model is not None:
                kwargs["body"] = model.from_dict(body)
        if key is not None and _accepts_idempotency_key(fn):
            kwargs.setdefault("idempotency_key", key)
        elif "idempotency_key" not in kwargs and _requires_idempotency_key(fn):
            # Mandatory on this operation, so a key is generated even under
            # `idempotency="off"`: the API refuses the call without one.
            kwargs["idempotency_key"] = str(uuid.uuid4())
        return args, kwargs


class _BaseClient:
    """Configuration shared by the sync and async clients."""

    _is_async = False

    def __init__(
        self,
        token: str | None = None,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float | httpx.Timeout | None = DEFAULT_TIMEOUT,
        user_agent_suffix: str | None = None,
        max_retries: int = 2,
        idempotency: IdempotencyMode = "auto",
        raise_on_error: bool = True,
        verify: bool | str | ssl.SSLContext = True,
        headers: dict[str, str] | None = None,
        follow_redirects: bool = False,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.token = token
        self._policy = RequestPolicy(
            max_retries=max_retries,
            idempotency=idempotency,
            raise_on_error=raise_on_error,
        )
        request_headers: dict[str, str] = {
            "Accept": "application/json",
            "User-Agent": default_user_agent(user_agent_suffix),
        }
        if token:
            request_headers["Authorization"] = f"Bearer {token}"
        if headers:
            # An explicit User-Agent in `headers` wins; the transport re-stamps that value
            # on every retry.
            request_headers.update(headers)
        self._headers = request_headers
        self._policy.user_agent = request_headers["User-Agent"]
        self._timeout = timeout
        self._verify = verify
        self._follow_redirects = follow_redirects
        self._groups: dict[str, _ApiGroup] = {}

        # The generated client only carries the httpx client built below. The SDK owns the
        # Authorization header, so an anonymous (reference-tier) client is the same object
        # without a credential.
        self._generated = AuthenticatedClient(
            base_url=self.base_url,
            token=token or "",
            raise_on_unexpected_status=False,
        )

    # -- generated surface -----------------------------------------------------

    @property
    def raw(self) -> AuthenticatedClient:
        """The generated client, for calling ``hosttracker.api.<tag>.<op>`` directly."""
        return self._generated

    def __getattr__(self, name: str) -> _ApiGroup:
        if name.startswith("_"):
            raise AttributeError(name)
        if name in TAGS:
            group = self._groups.get(name)
            if group is None:
                group = _ApiGroup(name, self._generated, self._is_async, self._policy.idempotency)
                self._groups[name] = group
            return group
        raise AttributeError(
            f"{type(self).__name__!r} object has no attribute {name!r}. Operation families are: {', '.join(TAGS)}."
        )

    def __dir__(self) -> list[str]:
        return sorted({*TAGS, *super().__dir__()})


class HostTracker(_BaseClient):
    """Synchronous HostTracker API v2 client.

    ::

        from hosttracker import HostTracker

        with HostTracker(token="...") as ht:
            page = ht.monitors.list_monitor(limit=2)
            for monitor in ht.paginate(ht.monitors.list_monitor, limit=100):
                print(monitor.name, monitor.state)

    Omit ``token`` for the anonymous reference tier (monitor types, agent pools, contact
    types, ...); every other call then answers ``401 invalid_token``.

    Args:
        token: The API token (a long-lived JWT minted on the profile page). Sent as
            ``Authorization: Bearer <token>`` on every call. No refresh flow exists.
        base_url: Defaults to production. Point it at a test host to smoke locally.
        timeout: Per-request timeout in seconds (or an :class:`httpx.Timeout`).
        user_agent_suffix: Appended to ``hosttracker-sdk-python/<version>``.
        max_retries: Extra attempts for the retryable failures only - ``429`` other than
            ``quota_exceeded``, ``503`` that named a ``Retry-After``, and transport
            failures on reads. Set 0 to disable.
        idempotency: ``"auto"`` (default) stamps a fresh UUID ``Idempotency-Key`` on every
            POST/PATCH/PUT/DELETE that is not a ``/q`` read twin, which is what makes a
            retried write safe. ``"off"`` sends none unless the caller supplies one.
        raise_on_error: Raise :class:`~hosttracker.errors.HostTrackerError` on any status
            >= 400 (default). Set False to receive the generated problem models instead.
        verify: TLS verification, passed to httpx. Use ``verify=False`` ONLY against a
            local dev host with a self-signed certificate.
        headers: Extra headers merged into every request.
        transport: A custom :class:`httpx.BaseTransport` placed underneath the SDK's own
            policy wrapper - proxies, custom TLS, ``httpx.MockTransport`` in tests.
        httpx_client: A fully caller-owned :class:`httpx.Client`. It is used verbatim, so
            it bypasses the SDK's retry/idempotency/error policy unless you wrap your own
            transport in :class:`hosttracker.HtTransport` yourself.
    """

    _is_async = False

    def __init__(
        self,
        token: str | None = None,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float | httpx.Timeout | None = DEFAULT_TIMEOUT,
        user_agent_suffix: str | None = None,
        max_retries: int = 2,
        idempotency: IdempotencyMode = "auto",
        raise_on_error: bool = True,
        verify: bool | str | ssl.SSLContext = True,
        headers: dict[str, str] | None = None,
        follow_redirects: bool = False,
        transport: httpx.BaseTransport | None = None,
        httpx_client: httpx.Client | None = None,
    ) -> None:
        super().__init__(
            token,
            base_url=base_url,
            timeout=timeout,
            user_agent_suffix=user_agent_suffix,
            max_retries=max_retries,
            idempotency=idempotency,
            raise_on_error=raise_on_error,
            verify=verify,
            headers=headers,
            follow_redirects=follow_redirects,
        )
        if httpx_client is None:
            inner = transport if transport is not None else httpx.HTTPTransport(verify=verify)
            httpx_client = httpx.Client(
                base_url=self.base_url,
                transport=HtTransport(inner, self._policy),
                timeout=timeout,
                headers=self._headers,
                follow_redirects=follow_redirects,
            )
        self._httpx = httpx_client
        self._generated.set_httpx_client(httpx_client)

    @property
    def httpx_client(self) -> httpx.Client:
        """The underlying :class:`httpx.Client` - for raw calls that follow a server URL."""
        return self._httpx

    # -- lifecycle -------------------------------------------------------------

    def close(self) -> None:
        self._httpx.close()

    def __enter__(self) -> HostTracker:
        self._httpx.__enter__()
        return self

    def __exit__(self, *args: Any) -> None:
        self._httpx.__exit__(*args)

    # -- helpers ---------------------------------------------------------------

    def paginate(self, list_call: Callable[..., Any], /, *args: Any, **params: Any) -> Iterator[Any]:
        """Iterate ITEMS across every page of a list operation. See :func:`hosttracker.paginate`."""
        from .paging import paginate

        return paginate(list_call, *args, **params)

    def pages(self, list_call: Callable[..., Any], /, *args: Any, **params: Any) -> Iterator[Any]:
        """Iterate PAGE envelopes (``syncCursor``, ``count``, ``summary``). See :func:`hosttracker.pages`."""
        from .paging import pages

        return pages(list_call, *args, **params)

    def wait_for_job(self, job_id: Any, **kwargs: Any) -> JobView:
        """Poll a bulk job to a terminal state. See :func:`hosttracker.wait_for_job`."""
        from .jobs import wait_for_job

        return wait_for_job(self, job_id, **kwargs)

    def run_check(self, body: IcCreateRequest | dict[str, Any], **kwargs: Any) -> IcResultView:
        """Start an instant check and follow ``resultUrl`` to its result. See :func:`hosttracker.run_check`."""
        from .checks import run_check

        return run_check(self, body, **kwargs)


class AsyncHostTracker(_BaseClient):
    """Asynchronous twin of :class:`HostTracker` - same options, same helper names.

    ::

        async with AsyncHostTracker(token="...") as ht:
            page = await ht.monitors.list_monitor(limit=2)
            async for monitor in ht.paginate(ht.monitors.list_monitor, limit=100):
                print(monitor.name)
    """

    _is_async = True

    def __init__(
        self,
        token: str | None = None,
        *,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float | httpx.Timeout | None = DEFAULT_TIMEOUT,
        user_agent_suffix: str | None = None,
        max_retries: int = 2,
        idempotency: IdempotencyMode = "auto",
        raise_on_error: bool = True,
        verify: bool | str | ssl.SSLContext = True,
        headers: dict[str, str] | None = None,
        follow_redirects: bool = False,
        transport: httpx.AsyncBaseTransport | None = None,
        httpx_client: httpx.AsyncClient | None = None,
    ) -> None:
        super().__init__(
            token,
            base_url=base_url,
            timeout=timeout,
            user_agent_suffix=user_agent_suffix,
            max_retries=max_retries,
            idempotency=idempotency,
            raise_on_error=raise_on_error,
            verify=verify,
            headers=headers,
            follow_redirects=follow_redirects,
        )
        if httpx_client is None:
            inner = transport if transport is not None else httpx.AsyncHTTPTransport(verify=verify)
            httpx_client = httpx.AsyncClient(
                base_url=self.base_url,
                transport=HtAsyncTransport(inner, self._policy),
                timeout=timeout,
                headers=self._headers,
                follow_redirects=follow_redirects,
            )
        self._httpx = httpx_client
        self._generated.set_async_httpx_client(httpx_client)

    @property
    def httpx_client(self) -> httpx.AsyncClient:
        """The underlying :class:`httpx.AsyncClient`."""
        return self._httpx

    async def aclose(self) -> None:
        await self._httpx.aclose()

    async def __aenter__(self) -> AsyncHostTracker:
        await self._httpx.__aenter__()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self._httpx.__aexit__(*args)

    def paginate(self, list_call: Callable[..., Any], /, *args: Any, **params: Any) -> AsyncIterator[Any]:
        """Async-iterate ITEMS across every page. See :func:`hosttracker.apaginate`."""
        from .paging import apaginate

        return apaginate(list_call, *args, **params)

    def pages(self, list_call: Callable[..., Any], /, *args: Any, **params: Any) -> AsyncIterator[Any]:
        """Async-iterate PAGE envelopes. See :func:`hosttracker.apages`."""
        from .paging import apages

        return apages(list_call, *args, **params)

    async def wait_for_job(self, job_id: Any, **kwargs: Any) -> JobView:
        """Poll a bulk job to a terminal state. See :func:`hosttracker.await_for_job`."""
        from .jobs import await_for_job

        return await await_for_job(self, job_id, **kwargs)

    async def run_check(self, body: IcCreateRequest | dict[str, Any], **kwargs: Any) -> IcResultView:
        """Start an instant check and follow ``resultUrl``. See :func:`hosttracker.arun_check`."""
        from .checks import arun_check

        return await arun_check(self, body, **kwargs)
