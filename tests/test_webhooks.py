"""Webhook signature verification, both schemes, against vectors computed here.

The vectors are built with the documented algorithm rather than pasted, so a change to
either scheme's signed string, key derivation or encoding fails loudly.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json

import pytest

from hosttracker import WebhookEvent, parse_webhook_event, verify_webhook_signature

SECRET = "whsec_c2VjcmV0LXZhbHVlLWZvci10ZXN0cw=="
ROTATED = "whsec_bmV3LXNlY3JldC12YWx1ZS1oZXJlISE="
NOW = 1735689600
DELIVERY_ID = "d_5b1f4e0c9a2d4f1b8c7e6a5d4f3b2a19"

BODY = json.dumps(
    {
        "id": DELIVERY_ID,
        "event": "monitor.down",
        "occurredAt": NOW,
        "apiVersion": "v2",
        "data": {
            "monitor": {
                "id": "11111111-1111-1111-1111-111111111111",
                "name": "web",
                "url": "https://www.host-tracker.com",
                "type": "http",
            },
            "state": "down",
            "occurredAt": NOW,
            "recheck": [{"location": {"id": "cccccccc-cccc-cccc-cccc-cccccccccccc", "country": "DE"}, "state": "down"}],
        },
    },
    separators=(",", ":"),
).encode()


def ht_signature(body: bytes, *secrets: str, t: int = NOW) -> str:
    """`t=<unix>,v1=<hex>[,v1=<hex>]` - key = UTF-8 of the WHOLE secret, lowercase hex."""
    signed = str(t).encode() + b"." + body
    parts = [f"t={t}"]
    for secret in secrets:
        parts.append(f"v1={hmac.new(secret.encode(), signed, hashlib.sha256).hexdigest()}")
    return ",".join(parts)


def standard_headers(body: bytes, *secrets: str, t: int = NOW, delivery_id: str = DELIVERY_ID) -> dict[str, str]:
    """Standard Webhooks: signed `<id>.<ts>.<body>`, key = base64-decoded after `whsec_`, base64 out."""
    signed = f"{delivery_id}.{t}.".encode() + body
    sigs = []
    for secret in secrets:
        key = base64.b64decode(secret[len("whsec_") :])
        sigs.append("v1," + base64.b64encode(hmac.new(key, signed, hashlib.sha256).digest()).decode())
    return {
        "webhook-id": delivery_id,
        "webhook-timestamp": str(t),
        "webhook-signature": " ".join(sigs),
    }


# --- HT scheme --------------------------------------------------------------------


def test_good_ht_signature_verifies():
    headers = {"HT-Signature": ht_signature(BODY, SECRET), "HT-Event": "monitor.down"}
    assert verify_webhook_signature(headers, BODY, SECRET, now=NOW) is True


def test_header_case_does_not_matter():
    headers = {"ht-signature": ht_signature(BODY, SECRET)}
    assert verify_webhook_signature(headers, BODY, SECRET, now=NOW) is True


def test_wrong_secret_fails():
    headers = {"HT-Signature": ht_signature(BODY, SECRET)}
    assert verify_webhook_signature(headers, BODY, ROTATED, now=NOW) is False


def test_tampered_body_fails():
    headers = {"HT-Signature": ht_signature(BODY, SECRET)}
    assert verify_webhook_signature(headers, BODY + b" ", SECRET, now=NOW) is False


def test_stale_timestamp_fails_outside_the_window():
    headers = {"HT-Signature": ht_signature(BODY, SECRET, t=NOW - 400)}
    assert verify_webhook_signature(headers, BODY, SECRET, now=NOW) is False
    # Inside the 300 s tolerance the very same delivery verifies.
    fresh = {"HT-Signature": ht_signature(BODY, SECRET, t=NOW - 299)}
    assert verify_webhook_signature(fresh, BODY, SECRET, now=NOW) is True


def test_future_timestamp_beyond_tolerance_fails():
    headers = {"HT-Signature": ht_signature(BODY, SECRET, t=NOW + 400)}
    assert verify_webhook_signature(headers, BODY, SECRET, now=NOW) is False


def test_custom_tolerance_is_honoured():
    headers = {"HT-Signature": ht_signature(BODY, SECRET, t=NOW - 400)}
    assert verify_webhook_signature(headers, BODY, SECRET, now=NOW, tolerance=600) is True
    assert verify_webhook_signature(headers, BODY, SECRET, now=NOW, tolerance=None) is True


def test_rotation_sends_two_v1_values_and_either_secret_may_be_held():
    """During the 24 h rotation window both secrets sign; a verifier must accept ANY match."""
    header = ht_signature(BODY, ROTATED, SECRET)
    assert header.count("v1=") == 2
    assert verify_webhook_signature({"HT-Signature": header}, BODY, SECRET, now=NOW) is True
    assert verify_webhook_signature({"HT-Signature": header}, BODY, ROTATED, now=NOW) is True


def test_a_list_of_secrets_is_accepted():
    headers = {"HT-Signature": ht_signature(BODY, ROTATED)}
    assert verify_webhook_signature(headers, BODY, [SECRET, ROTATED], now=NOW) is True


def test_missing_signature_header_fails():
    assert verify_webhook_signature({}, BODY, SECRET, now=NOW) is False


def test_malformed_signature_header_fails():
    assert verify_webhook_signature({"HT-Signature": "garbage"}, BODY, SECRET, now=NOW) is False
    assert verify_webhook_signature({"HT-Signature": f"t={NOW}"}, BODY, SECRET, now=NOW) is False


def test_no_secret_fails_closed():
    headers = {"HT-Signature": ht_signature(BODY, SECRET)}
    assert verify_webhook_signature(headers, BODY, [], now=NOW) is False


# --- Standard Webhooks ------------------------------------------------------------


def test_standard_scheme_verifies():
    headers = standard_headers(BODY, SECRET)
    assert verify_webhook_signature(headers, BODY, SECRET, now=NOW) is True


def test_standard_scheme_rejects_the_wrong_secret():
    headers = standard_headers(BODY, SECRET)
    assert verify_webhook_signature(headers, BODY, ROTATED, now=NOW) is False


def test_standard_scheme_rotation():
    headers = standard_headers(BODY, ROTATED, SECRET)
    assert verify_webhook_signature(headers, BODY, SECRET, now=NOW) is True
    assert verify_webhook_signature(headers, BODY, ROTATED, now=NOW) is True


def test_standard_scheme_stale_timestamp_fails():
    headers = standard_headers(BODY, SECRET, t=NOW - 400)
    assert verify_webhook_signature(headers, BODY, SECRET, now=NOW) is False


def test_the_two_schemes_are_not_interchangeable():
    """Different signed string, key derivation AND encoding - halves must never be mixed."""
    ht_only = {"HT-Signature": ht_signature(BODY, SECRET)}
    std_only = standard_headers(BODY, SECRET)
    assert verify_webhook_signature(ht_only, BODY, SECRET, now=NOW, scheme="standard") is False
    assert verify_webhook_signature(std_only, BODY, SECRET, now=NOW, scheme="ht") is False


def test_auto_scheme_accepts_either():
    both = {"HT-Signature": ht_signature(BODY, SECRET), **standard_headers(BODY, SECRET)}
    assert verify_webhook_signature(both, BODY, SECRET, now=NOW) is True


def test_a_secret_without_valid_base64_after_the_prefix_still_derives_a_key():
    secret = "whsec_not-base64-at-all!!"
    signed = f"{DELIVERY_ID}.{NOW}.".encode() + BODY
    key = secret[len("whsec_") :].encode()
    sig = "v1," + base64.b64encode(hmac.new(key, signed, hashlib.sha256).digest()).decode()
    headers = {"webhook-id": DELIVERY_ID, "webhook-timestamp": str(NOW), "webhook-signature": sig}
    assert verify_webhook_signature(headers, BODY, secret, now=NOW) is True


def test_string_body_is_accepted_but_bytes_are_the_contract():
    headers = {"HT-Signature": ht_signature(BODY, SECRET)}
    assert verify_webhook_signature(headers, BODY.decode(), SECRET, now=NOW) is True


# --- parsing ----------------------------------------------------------------------


def test_parse_webhook_event_types_a_known_event():
    event = parse_webhook_event(BODY)
    assert isinstance(event, WebhookEvent)
    assert event.event == "monitor.down"
    assert event.id == DELIVERY_ID
    assert event.delivery_id == DELIVERY_ID
    assert event.occurred_at == NOW
    assert event.api_version == "v2"
    assert event.data["monitor"]["name"] == "web"
    assert event.raw["apiVersion"] == "v2"
    assert type(event.typed).__name__ == "MonitorDownEnvelope"


def test_unknown_event_parses_untyped():
    """The event vocabulary is open: a new event must never break a receiver."""
    body = json.dumps({"id": "d_x", "event": "monitor.teleported", "occurredAt": NOW, "data": {"x": 1}}).encode()
    event = parse_webhook_event(body)
    assert event.event == "monitor.teleported"
    assert event.typed is None
    assert event.data == {"x": 1}


def test_unknown_member_in_a_known_payload_does_not_break_parsing():
    body = json.dumps(
        {
            "id": DELIVERY_ID,
            "event": "monitor.down",
            "occurredAt": NOW,
            "apiVersion": "v2",
            "data": {
                "monitor": {
                    "id": "11111111-1111-1111-1111-111111111111",
                    "name": "web",
                    "url": "https://www.host-tracker.com",
                },
                "state": "down",
                "occurredAt": NOW,
                "recheck": [],
                "somethingNew": 42,
            },
        }
    ).encode()
    event = parse_webhook_event(body)
    assert event.data["somethingNew"] == 42


def test_parse_rejects_a_body_without_an_event():
    with pytest.raises(ValueError, match="event"):
        parse_webhook_event(b'{"id":"d_x"}')


def test_parse_rejects_a_non_object_body():
    with pytest.raises(ValueError, match="JSON object"):
        parse_webhook_event(b"[1,2,3]")
