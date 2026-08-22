"""Retry policy and automatic idempotency keys - the two halves of a safe replay."""

from __future__ import annotations

import httpx
import pytest

from hosttracker import HostTracker, HostTrackerError, ResponseMeta, idempotency_key
from hosttracker.models import IcCreateRequest, MonitorQueryRequest

from .conftest import PROBLEM_HEADERS, monitor_row, problem

MONITOR_ID = "11111111-1111-1111-1111-111111111111"

IC_CREATED = {
    "id": "44444444-4444-4444-4444-444444444444",
    "dbId": 1,
    "retryAfter": 3,
    "estimatedDurationSec": 20,
    "resultUrl": "/check/1/44444444-4444-4444-4444-444444444444",
    "created": 1735689600,
}


def _scripted(responses: list[httpx.Response]):
    """Answer each call with the next scripted response."""
    remaining = list(responses)

    def handler(request: httpx.Request) -> httpx.Response:
        return remaining.pop(0) if remaining else httpx.Response(500, json=problem("internal_error", 500))

    return handler


# --- retry ------------------------------------------------------------------------


def test_rate_limited_is_retried_and_honours_retry_after(make_client, recorder, sleeps):
    limited = httpx.Response(
        429,
        json=problem("rate_limited", 429, errors=[{"limit": 60, "window": 60, "retryAfter": 7}]),
        headers={**PROBLEM_HEADERS, "Retry-After": "7"},
    )
    ok = httpx.Response(200, json={"data": [], "nextCursor": None, "hasMore": False})
    ht = make_client(_scripted([limited, ok]))

    page = ht.monitors.list_monitor(limit=1)

    assert page.data == []
    assert len(recorder) == 2
    assert sleeps == [7.0]  # the server's Retry-After, not a backoff guess


def test_quota_exceeded_is_never_retried(make_client, recorder, sleeps):
    """`rate_limited` and `quota_exceeded` share 429 and must NOT share behaviour."""
    exceeded = httpx.Response(
        429,
        json=problem("quota_exceeded", 429, errors=[{"limit": 1000, "remaining": 0, "resetAt": 1735689600}]),
        headers={**PROBLEM_HEADERS, "Retry-After": "600"},
    )
    ht = make_client(_scripted([exceeded, exceeded, exceeded]))

    with pytest.raises(HostTrackerError) as caught:
        ht.monitors.list_monitor(limit=1)

    assert caught.value.code == "quota_exceeded"
    assert len(recorder) == 1
    assert sleeps == []


def test_retry_after_is_capped_at_sixty_seconds(make_client, sleeps):
    limited = httpx.Response(429, json=problem("rate_limited", 429), headers={"Retry-After": "3600"})
    ok = httpx.Response(200, json={"data": [], "nextCursor": None, "hasMore": False})
    ht = make_client(_scripted([limited, ok]))
    ht.monitors.list_monitor(limit=1)
    assert sleeps == [60.0]


def test_service_unavailable_retries_only_when_it_names_a_wait(make_client, recorder, sleeps):
    unavailable = httpx.Response(
        503, json=problem("service_unavailable", 503), headers={**PROBLEM_HEADERS, "Retry-After": "2"}
    )
    ok = httpx.Response(200, json={"data": [], "nextCursor": None, "hasMore": False})
    ht = make_client(_scripted([unavailable, ok]))
    ht.monitors.list_monitor(limit=1)
    assert len(recorder) == 2
    assert sleeps == [2.0]


def test_bare_503_is_not_retried(make_client, recorder, sleeps):
    ht = make_client(_scripted([httpx.Response(503, json=problem("service_unavailable", 503))]))
    with pytest.raises(HostTrackerError):
        ht.monitors.list_monitor(limit=1)
    assert len(recorder) == 1


def test_max_retries_bounds_the_attempts(make_client, recorder, sleeps):
    limited = httpx.Response(429, json=problem("rate_limited", 429), headers={"Retry-After": "1"})
    ht = make_client(_scripted([limited] * 5), max_retries=2)
    with pytest.raises(HostTrackerError):
        ht.monitors.list_monitor(limit=1)
    assert len(recorder) == 3  # the original plus two retries


def test_transport_failure_is_retried_on_a_read(make_client, recorder, sleeps):
    state = {"failed": False}

    def handler(request: httpx.Request) -> httpx.Response:
        if not state["failed"]:
            state["failed"] = True
            raise httpx.ConnectError("reset by peer", request=request)
        return httpx.Response(200, json={"data": [], "nextCursor": None, "hasMore": False})

    ht = make_client(handler)
    ht.monitors.list_monitor(limit=1)
    assert len(recorder) == 2
    assert len(sleeps) == 1  # a backoff, no Retry-After to honour


def test_transport_failure_is_not_retried_on_a_write(make_client, recorder, sleeps):
    """A write that never answered may already have been applied; the caller decides."""

    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("reset by peer", request=request)

    ht = make_client(handler)
    with pytest.raises(HostTrackerError):
        ht.instant_checks.create_instant_check(
            body=IcCreateRequest.from_dict({"url": "https://x.test", "type": "http"})
        )
    assert len(recorder) == 1


def test_query_twin_post_is_treated_as_a_read(make_client, recorder, sleeps):
    """`POST /monitor/q` is a read wearing a POST: retryable, and no auto key."""
    limited = httpx.Response(429, json=problem("rate_limited", 429), headers={"Retry-After": "1"})
    ok = httpx.Response(200, json={"data": [], "nextCursor": None, "hasMore": False})
    ht = make_client(_scripted([limited, ok]))

    ht.monitors.query_monitor(body=MonitorQueryRequest.from_dict({"limit": 1}))

    assert len(recorder) == 2
    assert recorder.requests[0].url.path == "/monitor/q"
    assert recorder.idempotency_keys() == [None, None]


# --- idempotency ------------------------------------------------------------------


def test_auto_key_is_stamped_on_writes(make_client, recorder):
    ht = make_client(lambda r: httpx.Response(202, json=IC_CREATED, headers={"Location": IC_CREATED["resultUrl"]}))
    ht.instant_checks.create_instant_check(body=IcCreateRequest.from_dict({"url": "https://x.test", "type": "http"}))
    key = recorder.last.headers.get("Idempotency-Key")
    assert key and len(key) == 36  # a UUID


def test_no_auto_key_on_reads(make_client, recorder):
    ht = make_client(lambda r: httpx.Response(200, json={"data": [], "nextCursor": None, "hasMore": False}))
    ht.monitors.list_monitor(limit=1)
    assert recorder.last.headers.get("Idempotency-Key") is None


def test_idempotency_off_sends_no_key(make_client, recorder):
    ht = make_client(
        lambda r: httpx.Response(202, json=IC_CREATED),
        idempotency="off",
    )
    ht.instant_checks.create_instant_check(body=IcCreateRequest.from_dict({"url": "https://x.test", "type": "http"}))
    assert recorder.last.headers.get("Idempotency-Key") is None


def test_the_same_key_rides_every_retry_of_one_write(make_client, recorder, sleeps):
    """This is WHY writes may be retried at all: the replay is the same operation."""
    limited = httpx.Response(429, json=problem("rate_limited", 429), headers={"Retry-After": "1"})
    created = httpx.Response(202, json=IC_CREATED)
    ht = make_client(_scripted([limited, limited, created]))

    ht.instant_checks.create_instant_check(body=IcCreateRequest.from_dict({"url": "https://x.test", "type": "http"}))

    keys = recorder.idempotency_keys()
    assert len(keys) == 3
    assert all(k is not None for k in keys)
    assert len(set(keys)) == 1


def test_per_call_key_wins(make_client, recorder):
    ht = make_client(lambda r: httpx.Response(202, json=IC_CREATED))
    ht.instant_checks.create_instant_check(
        body=IcCreateRequest.from_dict({"url": "https://x.test", "type": "http"}),
        idempotency_key="order-4711",
    )
    assert recorder.last.headers["Idempotency-Key"] == "order-4711"


def test_idempotency_key_context_manager_applies_to_the_block(make_client, recorder):
    """The context manager covers operations that do not declare the header themselves."""
    receipt = {"id": MONITOR_ID, "deleted": True}
    ht = make_client(lambda r: httpx.Response(200, json=receipt))
    with idempotency_key("delete-once"):
        ht.monitors.delete_monitor(MONITOR_ID)
    assert recorder.last.headers["Idempotency-Key"] == "delete-once"


def test_idempotency_replayed_is_surfaced(make_client):
    ht = make_client(
        lambda r: httpx.Response(
            202,
            json=IC_CREATED,
            headers={"Idempotency-Replayed": "true", "X-Request-Id": "req-replay"},
        )
    )
    response = ht.instant_checks.create_instant_check(
        body=IcCreateRequest.from_dict({"url": "https://x.test", "type": "http"}),
        detailed=True,
    )
    meta = ResponseMeta.from_response(response)
    assert meta.idempotency_replayed is True
    assert meta.request_id == "req-replay"


def test_user_agent_and_bearer_token(make_client, recorder):
    ht = make_client(lambda r: httpx.Response(200, json={"data": [], "nextCursor": None, "hasMore": False}))
    ht.monitors.list_monitor(limit=1)
    assert recorder.last.headers["Authorization"] == "Bearer test-token"
    assert recorder.last.headers["User-Agent"].startswith("hosttracker-sdk-python/")


def test_user_agent_suffix_is_appended(recorder):
    seen: dict[str, str] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["ua"] = request.headers["User-Agent"]
        return httpx.Response(200, json={"data": [], "nextCursor": None, "hasMore": False})

    ht = HostTracker(
        token="t",
        base_url="https://api2.test",
        transport=httpx.MockTransport(handler),
        user_agent_suffix="acme-ops/2.0",
    )
    ht.monitors.list_monitor(limit=1)
    assert seen["ua"].endswith(" acme-ops/2.0")
    assert seen["ua"].startswith("hosttracker-sdk-python/")


def test_anonymous_client_sends_no_authorization(recorder):
    seen: dict[str, bool] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["auth"] = "Authorization" in request.headers
        return httpx.Response(200, json={"data": [], "nextCursor": None, "hasMore": False})

    ht = HostTracker(base_url="https://api2.test", transport=httpx.MockTransport(handler))
    ht.monitor_types.list_monitor_type()
    assert seen["auth"] is False


def test_unknown_operation_names_the_family(make_client):
    ht = make_client(lambda r: httpx.Response(200, json={}))
    with pytest.raises(AttributeError, match="has no operation"):
        ht.monitors.list_the_monitors()


def test_unknown_family_lists_the_real_ones(make_client):
    ht = make_client(lambda r: httpx.Response(200, json={}))
    with pytest.raises(AttributeError, match="Operation families are"):
        _ = ht.monitorz


def test_monitor_row_fixture_parses(make_client):
    """Guards the fixture itself: a MonitorView needs every required member."""
    ht = make_client(
        lambda r: httpx.Response(
            200, json={"data": [monitor_row(MONITOR_ID, "a")], "nextCursor": None, "hasMore": False}
        )
    )
    page = ht.monitors.list_monitor(limit=1)
    assert str(page.data[0].id) == MONITOR_ID


def test_a_bodiless_429_is_retried(make_client, recorder, sleeps):
    """The per-IP+endpoint throttle answers plain text plus a Retry-After, no problem body."""
    throttled = httpx.Response(429, text="API calls quota exceeded", headers={"Retry-After": "4"})
    ok = httpx.Response(200, json={"data": [], "nextCursor": None, "hasMore": False})
    ht = make_client(_scripted([throttled, ok]))

    ht.monitors.list_monitor(limit=1)

    assert len(recorder) == 2
    assert sleeps == [4.0]


def test_a_429_with_an_unrecognised_code_is_not_retried(make_client, recorder, sleeps):
    """The SDK replays `rate_limited` and bodiless 429s only - it never guesses."""
    odd = httpx.Response(429, json=problem("package_limit", 429), headers={**PROBLEM_HEADERS, "Retry-After": "1"})
    ht = make_client(_scripted([odd, odd, odd]))

    with pytest.raises(HostTrackerError) as caught:
        ht.monitors.list_monitor(limit=1)

    assert caught.value.code == "package_limit"
    assert len(recorder) == 1


def test_a_bodiless_503_with_retry_after_is_retried(make_client, recorder, sleeps):
    unavailable = httpx.Response(503, text="upstream down", headers={"Retry-After": "3"})
    ok = httpx.Response(200, json={"data": [], "nextCursor": None, "hasMore": False})
    ht = make_client(_scripted([unavailable, ok]))
    ht.monitors.list_monitor(limit=1)
    assert len(recorder) == 2
    assert sleeps == [3.0]


def test_a_503_with_another_code_is_not_retried(make_client, recorder, sleeps):
    other = httpx.Response(503, json=problem("upstream_error", 503), headers={"Retry-After": "1"})
    ht = make_client(_scripted([other, other]))
    with pytest.raises(HostTrackerError) as caught:
        ht.monitors.list_monitor(limit=1)
    assert caught.value.code == "upstream_error"
    assert len(recorder) == 1


def test_backoff_without_a_retry_after_is_full_jitter_under_the_cap(make_client, recorder, sleeps):
    """200 ms * 2**n, full jitter, capped at 5 s."""
    attempts = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        attempts["n"] += 1
        if attempts["n"] <= 2:
            raise httpx.ConnectError("reset by peer", request=request)
        return httpx.Response(200, json={"data": [], "nextCursor": None, "hasMore": False})

    ht = make_client(handler, max_retries=2)
    ht.monitors.list_monitor(limit=1)

    assert len(sleeps) == 2
    assert 0.0 <= sleeps[0] <= 0.2  # ceiling 200 ms * 2**0
    assert 0.0 <= sleeps[1] <= 0.4  # ceiling 200 ms * 2**1
    assert all(d <= 5.0 for d in sleeps)


# --- the nine operations that REQUIRE a key ---------------------------------------

REQUIRE_A_KEY = [
    ("monitors", "bulk_create_monitor"),
    ("monitors", "bulk_update_monitor"),
    ("monitors", "bulk_delete_monitor"),
    ("monitors", "reset_monitor_stats"),
    ("contacts", "bulk_write_contact"),
    ("contacts", "bulk_delete_contact"),
    ("reports", "generate_report"),
    ("status_pages", "create_status_page_incident"),
    ("status_pages", "add_status_page_incident_timeline_entry"),
]


@pytest.mark.parametrize(("family", "operation"), REQUIRE_A_KEY)
def test_the_nine_operations_declare_the_header_mandatory(family, operation):
    """Guards the list itself: if the spec relaxes one of these, this test says so."""
    import inspect

    module = __import__(f"hosttracker._generated.api.{family}.{operation}", fromlist=["sync_detailed"])
    parameter = inspect.signature(module.sync_detailed).parameters["idempotency_key"]
    assert parameter.default is inspect.Parameter.empty


def test_a_mandatory_key_is_supplied_for_the_caller(make_client, recorder):
    """A caller must never have to hand-write the key the spec makes required."""
    ht = make_client(
        lambda r: httpx.Response(202, json={"jobId": "55555555-5555-5555-5555-555555555555", "accepted": 1})
    )
    ht.monitors.bulk_create_monitor(body={"items": [{"type": "http", "url": "https://x.test"}]})
    key = recorder.last.headers.get("Idempotency-Key")
    assert key and len(key) == 36


def test_an_explicit_key_wins_on_a_mandatory_operation(make_client, recorder):
    ht = make_client(
        lambda r: httpx.Response(202, json={"jobId": "55555555-5555-5555-5555-555555555555", "accepted": 1})
    )
    ht.monitors.bulk_create_monitor(
        body={"items": [{"type": "http", "url": "https://x.test"}]}, idempotency_key="import-2025-01"
    )
    assert recorder.last.headers["Idempotency-Key"] == "import-2025-01"


def test_an_optional_union_body_still_accepts_a_dict(make_client, recorder):
    """`Model | Unset` annotations (optional bodies) coerce a dict just like plain ones."""
    ht = make_client(
        lambda r: httpx.Response(202, json={"jobId": "55555555-5555-5555-5555-555555555555", "accepted": 1})
    )
    ht.monitors.bulk_update_monitor(body={"ids": ["11111111-1111-1111-1111-111111111111"], "patch": {"enabled": False}})
    import json as _json

    assert "patch" in _json.loads(recorder.last.content)


def test_a_mandatory_key_is_still_supplied_when_idempotency_is_off(make_client, recorder):
    """`idempotency="off"` opts out of automatic keys; the API still refuses these without one."""
    ht = make_client(
        lambda r: httpx.Response(202, json={"jobId": "55555555-5555-5555-5555-555555555555", "accepted": 1}),
        idempotency="off",
    )
    ht.monitors.bulk_create_monitor(body={"items": []})
    assert recorder.last.headers.get("Idempotency-Key") is not None
