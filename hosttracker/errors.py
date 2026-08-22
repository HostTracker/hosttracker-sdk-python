"""The single error type the SDK raises, plus the response metadata it carries.

Every failure - an RFC 9457 ``application/problem+json`` document, a bare HTML 502
from a proxy, a DNS failure, a timeout - arrives as one :class:`HostTrackerError`.
Branch on :attr:`HostTrackerError.code`, never on the HTTP status alone: ``rate_limited``
and ``quota_exceeded`` are both 429 and need opposite remediation.
"""

from __future__ import annotations

import email.utils
import json
from dataclasses import dataclass, field
from typing import Any

import httpx

__all__ = [
    "CODE_HTTP_ERROR",
    "CODE_NETWORK_ERROR",
    "CODE_TIMEOUT",
    "HostTrackerError",
    "RateLimit",
    "ResponseMeta",
]

#: Assigned when the server answered a failure that was not a problem+json document
#: (an HTML error page from a proxy, an empty body, a truncated payload).
CODE_HTTP_ERROR = "http_error"

#: Assigned when no HTTP answer was obtained at all (DNS, TLS, connection reset).
CODE_NETWORK_ERROR = "network_error"

#: Assigned when a client-side deadline expired (request timeout, ``wait_for_job``/
#: ``run_check`` overall timeout).
CODE_TIMEOUT = "timeout"


def _parse_retry_after(value: str | None) -> float | None:
    """Parse a ``Retry-After`` header - delta-seconds or an HTTP-date - into seconds."""
    if not value:
        return None
    value = value.strip()
    try:
        return max(0.0, float(value))
    except ValueError:
        pass
    try:
        when = email.utils.parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None
    if when is None:
        return None
    import datetime as _dt

    now = _dt.datetime.now(_dt.UTC)
    if when.tzinfo is None:
        when = when.replace(tzinfo=_dt.UTC)
    return max(0.0, (when - now).total_seconds())


def _int_or_none(value: str | None) -> int | None:
    if value is None:
        return None
    try:
        return int(value.strip())
    except (TypeError, ValueError):
        return None


@dataclass(frozen=True)
class RateLimit:
    """Snapshot of the ``RateLimit-*`` headers that rode a single response.

    ``policy`` is the literal ``RateLimit-Policy`` value: ``<bucket>;q=<limit>[;w=<seconds>]``,
    or ``none`` when the scope has no quota window. Under ``none`` the API omits
    ``RateLimit-Limit``/``-Remaining``/``-Reset``, so those stay ``None``.
    """

    policy: str | None = None
    limit: int | None = None
    remaining: int | None = None
    reset: int | None = None

    @property
    def metered(self) -> bool:
        """True when a real quota window bound this call."""
        return self.policy is not None and self.policy.strip().lower() != "none"

    @classmethod
    def from_headers(cls, headers: Any) -> RateLimit:
        get = getattr(headers, "get", None)
        if get is None:
            return cls()
        return cls(
            policy=get("RateLimit-Policy"),
            limit=_int_or_none(get("RateLimit-Limit")),
            remaining=_int_or_none(get("RateLimit-Remaining")),
            reset=_int_or_none(get("RateLimit-Reset")),
        )


@dataclass(frozen=True)
class ResponseMeta:
    """Per-response metadata the API stamps on every answer, success or failure.

    Obtain it from any ``detailed=True`` call::

        page = ht.monitors.list_monitor(limit=2, detailed=True)
        meta = ResponseMeta.from_response(page)
        print(meta.request_id, meta.rate_limit.remaining)
    """

    status_code: int
    request_id: str | None = None
    retry_after: float | None = None
    idempotency_replayed: bool = False
    rate_limit: RateLimit = field(default_factory=RateLimit)
    headers: dict[str, str] = field(default_factory=dict)

    @classmethod
    def from_headers(cls, status_code: int, headers: Any) -> ResponseMeta:
        get = getattr(headers, "get", lambda _k, _d=None: None)
        replayed = (get("Idempotency-Replayed") or "").strip().lower() == "true"
        try:
            flat = {str(k): str(v) for k, v in dict(headers).items()}
        except Exception:  # pragma: no cover - exotic header containers
            flat = {}
        return cls(
            status_code=status_code,
            request_id=get("X-Request-Id"),
            retry_after=_parse_retry_after(get("Retry-After")),
            idempotency_replayed=replayed,
            rate_limit=RateLimit.from_headers(headers),
            headers=flat,
        )

    @classmethod
    def from_response(cls, response: Any) -> ResponseMeta:
        """Build metadata from a generated ``Response`` or a raw :class:`httpx.Response`."""
        status = getattr(response, "status_code", None)
        headers = getattr(response, "headers", {})
        return cls.from_headers(int(status) if status is not None else 0, headers)


class HostTrackerError(Exception):
    """The one exception every HostTracker call raises.

    Carries the whole RFC 9457 problem document plus the response metadata that rode
    with it. For failures that are not problem documents the shape is preserved and
    :attr:`code` becomes ``http_error`` (a non-problem HTTP failure), ``network_error``
    (no answer at all) or ``timeout``.

    :attr:`errors` stays a list of raw dicts by design. The spec types one entry as
    ``ProblemError`` plus a per-code remediation shape (``ValidationFailedError``,
    ``InsufficientAgentsError``, ...), but a failure that is not a problem document has no
    typed shape at all, and importing a generated model here would load the model tree on
    ``import hosttracker``. Read the members you need off the dict; the per-code models in
    ``hosttracker.models`` document which ones each code carries.
    """

    def __init__(
        self,
        *,
        code: str,
        status: int | None = None,
        title: str | None = None,
        detail: str | None = None,
        type: str | None = None,  # noqa: A002 - mirrors the RFC 9457 member name
        instance: str | None = None,
        errors: list[dict[str, Any]] | None = None,
        problem: dict[str, Any] | None = None,
        meta: ResponseMeta | None = None,
        method: str | None = None,
        url: str | None = None,
        body: bytes | None = None,
    ) -> None:
        self.code = code
        self.status = status
        self.title = title
        self.detail = detail
        self.type = type
        self.instance = instance
        self.errors: list[dict[str, Any]] = errors or []
        self.problem: dict[str, Any] = problem or {}
        self.meta = meta or ResponseMeta(status_code=status or 0)
        self.method = method
        self.url = url
        self.body = body
        super().__init__(self._message())

    # -- convenience accessors -------------------------------------------------

    @property
    def request_id(self) -> str | None:
        """``X-Request-Id`` - quote it in support requests."""
        return self.meta.request_id

    @property
    def retry_after(self) -> float | None:
        """Seconds the server asked the caller to wait, when it said so."""
        if self.meta.retry_after is not None:
            return self.meta.retry_after
        for entry in self.errors:
            for key in ("retryAfter", "retryAfterSeconds"):
                value = entry.get(key)
                if isinstance(value, (int, float)):
                    return float(value)
        return None

    @property
    def rate_limit(self) -> RateLimit:
        """The ``RateLimit-*`` snapshot that rode this failure."""
        return self.meta.rate_limit

    def _message(self) -> str:
        head = f"{self.status} {self.code}" if self.status else self.code
        parts = [p for p in (self.title, self.detail) if p]
        text = f"{head}: {' - '.join(parts)}" if parts else head
        if self.method and self.url:
            text = f"{text} [{self.method} {self.url}]"
        if self.request_id:
            text = f"{text} (request_id={self.request_id})"
        return text

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return f"<HostTrackerError code={self.code!r} status={self.status!r}>"


def problem_code_of(body: bytes | None) -> str | None:
    """Best-effort read of the ``code`` member out of a problem+json body."""
    if not body:
        return None
    try:
        doc = json.loads(body)
    except (ValueError, TypeError):
        return None
    if isinstance(doc, dict):
        code = doc.get("code")
        if isinstance(code, str):
            return code
    return None


def error_from_response(request: httpx.Request | None, response: httpx.Response) -> HostTrackerError:
    """Map a >=400 :class:`httpx.Response` onto a :class:`HostTrackerError`.

    ``request`` is passed explicitly because a response handed back by a transport does
    not have ``.request`` bound yet (httpx binds it one layer up).
    """
    body = response.content
    meta = ResponseMeta.from_headers(response.status_code, response.headers)
    doc: dict[str, Any] = {}
    try:
        parsed = json.loads(body) if body else None
        if isinstance(parsed, dict):
            doc = parsed
    except (ValueError, TypeError):
        doc = {}

    code = doc.get("code")
    if not isinstance(code, str) or not code:
        code = CODE_HTTP_ERROR
    errors = doc.get("errors")
    if not isinstance(errors, list):
        errors = []
    errors = [e for e in errors if isinstance(e, dict)]

    title = doc.get("title")
    if not isinstance(title, str):
        title = response.reason_phrase or None
    detail = doc.get("detail")
    if not isinstance(detail, str):
        # A non-problem failure (HTML from a proxy, empty body) still deserves a hint.
        text = (body or b"").decode("utf-8", "replace").strip()
        detail = (text[:500] + "...") if len(text) > 500 else (text or None)

    return HostTrackerError(
        code=code,
        status=response.status_code,
        title=title,
        detail=detail,
        type=doc.get("type") if isinstance(doc.get("type"), str) else None,
        instance=doc.get("instance") if isinstance(doc.get("instance"), str) else None,
        errors=errors,
        problem=doc,
        meta=meta,
        method=request.method if request is not None else None,
        url=str(request.url) if request is not None else None,
        body=body,
    )


def network_error(request: httpx.Request, cause: BaseException) -> HostTrackerError:
    """Map a transport-level failure onto a :class:`HostTrackerError`.

    Timeouts are network failures too and carry ``code == "network_error"``; only the
    SDK's own deadlines (``wait_for_job``, ``run_check``) raise ``code == "timeout"``.
    """
    timed_out = isinstance(cause, httpx.TimeoutException)
    return HostTrackerError(
        code=CODE_NETWORK_ERROR,
        status=None,
        title="Request timed out" if timed_out else "Network error",
        detail=str(cause) or type(cause).__name__,
        method=request.method,
        url=str(request.url),
    )
