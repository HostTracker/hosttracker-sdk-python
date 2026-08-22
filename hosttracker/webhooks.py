"""Verifying and parsing webhook deliveries.

Every delivery is signed TWICE, with two independent schemes, so a receiver can use
whichever its stack already speaks:

* **HT scheme** - ``HT-Signature: t=<unix>,v1=<hex>[,v1=<hex>...]``. Signed string is
  ``"<t>." + raw body``; the HMAC-SHA256 key is the UTF-8 bytes of the WHOLE secret,
  ``whsec_`` prefix included; the digest is lowercase hex.
* **Standard Webhooks** - ``webhook-id`` / ``webhook-timestamp`` / ``webhook-signature``.
  Signed string is ``"<id>.<ts>.<body>"``; the key is the base64-decoded remainder AFTER
  ``whsec_``; the digest is base64.

The two differ in signed content, key derivation AND encoding - never mix halves.

Repeated ``v1`` values are legal and expected: a rotation (``PATCH /webhook/{id}
{"secret":{"rotate":true}}``) signs with both the new and the old secret for 24 hours, so
a verifier must accept ANY match, not just the first.

Always verify the RAW request bytes, before any JSON parse or re-serialisation.
"""

from __future__ import annotations

import base64
import binascii
import hashlib
import hmac
import json
import time
from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Any, Literal

__all__ = [
    "WEBHOOK_EVENT_MODELS",
    "WebhookEvent",
    "parse_webhook_event",
    "verify_webhook_signature",
]

#: Default replay window in seconds, matching the API's own tolerance.
DEFAULT_TOLERANCE = 300

Scheme = Literal["auto", "ht", "standard"]

#: ``event`` -> the generated envelope model that types the whole document. Unknown
#: events (the vocabulary is deliberately open) parse untyped, they never fail.
WEBHOOK_EVENT_MODELS: dict[str, str] = {
    "monitor.down": "MonitorDownEnvelope",
    "monitor.up": "MonitorUpEnvelope",
    "monitor.repeatedlyDown": "MonitorRepeatedlyDownEnvelope",
    "incident.opened": "IncidentOpenedEnvelope",
    "incident.closed": "IncidentClosedEnvelope",
    "monitor.created": "MonitorCreatedEnvelope",
    "monitor.updated": "MonitorUpdatedEnvelope",
    "monitor.deleted": "MonitorDeletedEnvelope",
    "maintenance.ended": "MaintenanceEndedEnvelope",
    "certificate.expiring": "CertificateExpiringEnvelope",
    "domain.expiring": "DomainExpiringEnvelope",
    "contact.confirmed": "ContactConfirmedEnvelope",
    "contact.updated": "ContactUpdatedEnvelope",
    "job.completed": "JobCompletedEnvelope",
    "job.progress": "JobProgressEnvelope",
}


# ---------------------------------------------------------------------------
# verification
# ---------------------------------------------------------------------------


def _lower_headers(headers: Mapping[str, Any] | Any) -> dict[str, str]:
    """Normalise any header container (dict, httpx/requests Headers, WSGI-ish) to lowercase."""
    # A mapping (dict, httpx.Headers, werkzeug EnvironHeaders) or a bare pair sequence.
    items: Iterable[tuple[Any, Any]] = headers.items() if hasattr(headers, "items") else list(headers)
    out: dict[str, str] = {}
    for key, value in items:
        out[str(key).lower().replace("_", "-")] = value if isinstance(value, str) else str(value)
    return out


def _as_bytes(body: bytes | bytearray | memoryview | str) -> bytes:
    if isinstance(body, str):
        # Only correct when the caller already decoded UTF-8 losslessly; verifying the
        # bytes off the wire is always preferable.
        return body.encode("utf-8")
    return bytes(body)


def _secret_list(secrets: str | Iterable[str]) -> list[str]:
    if isinstance(secrets, str):
        return [secrets]
    return [s for s in secrets if s]


def _fresh(timestamp: str | None, tolerance: int | None, now: float | None) -> bool:
    if tolerance is None:
        return True
    if timestamp is None:
        return False
    try:
        sent = int(str(timestamp).strip())
    except (TypeError, ValueError):
        return False
    current = time.time() if now is None else float(now)
    return abs(current - sent) <= tolerance


def _parse_ht_signature(value: str) -> tuple[str | None, list[str]]:
    """Split ``t=<unix>,v1=<hex>[,v1=<hex>]`` into the timestamp and every ``v1``."""
    timestamp: str | None = None
    signatures: list[str] = []
    for part in value.split(","):
        name, _, raw = part.strip().partition("=")
        name = name.strip().lower()
        raw = raw.strip()
        if name == "t" and timestamp is None:
            timestamp = raw
        elif name == "v1" and raw:
            signatures.append(raw)
    return timestamp, signatures


def _standard_key(secret: str) -> bytes:
    """Standard Webhooks key derivation: base64-decode the part after ``whsec_``."""
    body = secret[len("whsec_") :] if secret.startswith("whsec_") else secret
    try:
        return base64.b64decode(body, validate=True)
    except (binascii.Error, ValueError):
        # Not valid base64 - the scheme falls back to the raw bytes of the remainder.
        return body.encode("utf-8")


def _verify_ht(
    headers: dict[str, str], body: bytes, secrets: list[str], tolerance: int | None, now: float | None
) -> bool:
    raw = headers.get("ht-signature")
    if not raw:
        return False
    timestamp, signatures = _parse_ht_signature(raw)
    if not timestamp or not signatures:
        return False
    if not _fresh(timestamp, tolerance, now):
        return False
    signed = timestamp.encode("utf-8") + b"." + body
    for secret in secrets:
        expected = hmac.new(secret.encode("utf-8"), signed, hashlib.sha256).hexdigest()
        for candidate in signatures:
            if hmac.compare_digest(expected, candidate.strip().lower()):
                return True
    return False


def _verify_standard(
    headers: dict[str, str], body: bytes, secrets: list[str], tolerance: int | None, now: float | None
) -> bool:
    delivery_id = headers.get("webhook-id")
    timestamp = headers.get("webhook-timestamp")
    raw = headers.get("webhook-signature")
    if not (delivery_id and timestamp and raw):
        return False
    if not _fresh(timestamp, tolerance, now):
        return False
    # `v1,<base64>` entries, whitespace-separated when several are present.
    candidates = [part.split(",", 1)[1] for part in raw.split() if part.startswith("v1,")]
    if not candidates:
        return False
    signed = f"{delivery_id}.{timestamp}.".encode() + body
    for secret in secrets:
        digest = hmac.new(_standard_key(secret), signed, hashlib.sha256).digest()
        expected = base64.b64encode(digest).decode("ascii")
        for candidate in candidates:
            if hmac.compare_digest(expected, candidate.strip()):
                return True
    return False


def verify_webhook_signature(
    headers: Mapping[str, Any],
    raw_body: bytes | bytearray | memoryview | str,
    secrets: str | Iterable[str],
    *,
    tolerance: int | None = DEFAULT_TOLERANCE,
    now: float | None = None,
    scheme: Scheme = "auto",
) -> bool:
    """Return True when the delivery is authentic and inside the replay window.

    ::

        if not verify_webhook_signature(request.headers, request.body, secret):
            return Response(status=400)
        event = parse_webhook_event(request.body)

    Args:
        headers: The inbound request headers (any mapping; case does not matter).
        raw_body: The RAW request bytes, exactly as received - not a re-serialised dict.
        secrets: One secret, or several during a rotation window. Pass the WHOLE value
            including the ``whsec_`` prefix; both schemes derive their key from it.
        tolerance: Replay window in seconds (default 300, matching the API). ``None``
            disables the timestamp check - only sensible in tests with fixed vectors.
        now: Override the current Unix time, for deterministic tests.
        scheme: ``"auto"`` (default) accepts either signature; ``"ht"`` or ``"standard"``
            pins one.
    """
    normalised = _lower_headers(headers)
    body = _as_bytes(raw_body)
    keys = _secret_list(secrets)
    if not keys:
        return False
    if scheme in ("auto", "ht") and _verify_ht(normalised, body, keys, tolerance, now):
        return True
    return scheme in ("auto", "standard") and _verify_standard(normalised, body, keys, tolerance, now)


# ---------------------------------------------------------------------------
# parsing
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class WebhookEvent:
    """The delivery envelope: ``{id, event, occurredAt, apiVersion, data}``.

    ``data`` is always the raw dict, so a payload member the SDK has never heard of is
    still readable. ``typed`` is the generated envelope model for the 15 published events
    when it parses cleanly, and ``None`` for an event (or a payload shape) this SDK
    release predates - the event vocabulary is open by design.
    """

    id: str | None
    event: str
    occurred_at: int | None
    api_version: str | None
    data: dict[str, Any] = field(default_factory=dict)
    raw: dict[str, Any] = field(default_factory=dict)
    typed: Any = None

    @property
    def delivery_id(self) -> str | None:
        """Same token as the ``HT-Delivery`` header - stable across retries, the dedupe key."""
        return self.id


def _typed_envelope(event: str, document: dict[str, Any]) -> Any:
    model_name = WEBHOOK_EVENT_MODELS.get(event)
    if model_name is None:
        return None
    try:
        module = __import__("hosttracker._generated.models", fromlist=[model_name])
        model = getattr(module, model_name)
        return model.from_dict(document)
    except Exception:
        # A newly added member or enum value must never break a receiver: fall back to
        # the raw dict, which is always present on the event.
        return None


def parse_webhook_event(raw_body: bytes | bytearray | memoryview | str) -> WebhookEvent:
    """Parse a delivery body into a :class:`WebhookEvent`.

    Verify the signature FIRST - this function does no authentication of its own.
    """
    body = _as_bytes(raw_body)
    document = json.loads(body.decode("utf-8"))
    if not isinstance(document, dict):
        raise ValueError("webhook body is not a JSON object")
    event = document.get("event")
    if not isinstance(event, str):
        raise ValueError("webhook body has no 'event' member")
    data = document.get("data")
    occurred = document.get("occurredAt")
    return WebhookEvent(
        id=document.get("id") if isinstance(document.get("id"), str) else None,
        event=event,
        occurred_at=occurred if isinstance(occurred, int) else None,
        api_version=document.get("apiVersion") if isinstance(document.get("apiVersion"), str) else None,
        data=data if isinstance(data, dict) else {},
        raw=document,
        typed=_typed_envelope(event, document),
    )
