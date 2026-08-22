"""Construction options, the operation proxy, and interop with plain httpx tooling."""

from __future__ import annotations

import datetime as dt

import httpx
import pytest
import respx

from hosttracker import (
    DEFAULT_BASE_URL,
    TAGS,
    AsyncHostTracker,
    HostTracker,
    HostTrackerError,
    from_datetime,
    to_datetime,
)
from hosttracker.models import IcCreateRequest

from .conftest import monitor_row, problem

MONITOR_ID = "11111111-1111-1111-1111-111111111111"
EMPTY_PAGE = {"data": [], "nextCursor": None, "hasMore": False}


def test_default_base_url_is_production():
    assert DEFAULT_BASE_URL == "https://api2.host-tracker.com"
    assert HostTracker(token="t").base_url == DEFAULT_BASE_URL


def test_base_url_trailing_slash_is_normalised():
    assert HostTracker(token="t", base_url="https://api.example.test/").base_url == "https://api.example.test"


def test_every_published_tag_is_reachable():
    ht = HostTracker(token="t", transport=httpx.MockTransport(lambda r: httpx.Response(200, json=EMPTY_PAGE)))
    for tag in TAGS:
        assert getattr(ht, tag) is not None
    assert set(TAGS) <= set(dir(ht))


def test_operation_names_are_discoverable():
    ht = HostTracker(token="t", transport=httpx.MockTransport(lambda r: httpx.Response(200, json=EMPTY_PAGE)))
    names = dir(ht.monitors)
    assert "list_monitor" in names
    assert "bulk_create_monitor" in names
    assert "query_monitor" in names


def test_detailed_returns_the_generated_response_wrapper(make_client):
    ht = make_client(lambda r: httpx.Response(200, json=EMPTY_PAGE, headers={"X-Request-Id": "abc"}))
    detailed = ht.monitors.list_monitor(detailed=True)
    assert detailed.status_code == 200
    assert detailed.headers["x-request-id"] == "abc"
    assert detailed.parsed.data == []


def test_raw_exposes_the_generated_client(make_client):
    """The escape hatch: call a generated operation module directly, fully typed."""
    from hosttracker._generated.api.monitors import list_monitor

    ht = make_client(
        lambda r: httpx.Response(
            200, json={"data": [monitor_row(MONITOR_ID, "a")], "nextCursor": None, "hasMore": False}
        )
    )
    page = list_monitor.sync(client=ht.raw, limit=1)
    assert page.data[0].name == "a"


def test_context_manager_closes_the_transport():
    with HostTracker(token="t", transport=httpx.MockTransport(lambda r: httpx.Response(200, json=EMPTY_PAGE))) as ht:
        assert ht.monitors.list_monitor().data == []
    assert ht.httpx_client.is_closed


def test_a_caller_supplied_httpx_client_is_used_verbatim():
    """Documented escape hatch - it bypasses the SDK policy unless the caller wraps it."""
    seen: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request.headers.get("User-Agent", ""))
        return httpx.Response(200, json=EMPTY_PAGE)

    own = httpx.Client(
        base_url="https://api2.test", transport=httpx.MockTransport(handler), headers={"User-Agent": "mine/1"}
    )
    ht = HostTracker(token="t", base_url="https://api2.test", httpx_client=own)
    ht.monitors.list_monitor()
    assert seen == ["mine/1"]


def test_respx_intercepts_the_sdk_end_to_end():
    """The SDK is plain httpx underneath, so the usual mocking tools work unchanged."""
    with respx.mock(base_url="https://api2.test") as mock:
        route = mock.get("/monitor").mock(
            return_value=httpx.Response(
                200, json={"data": [monitor_row(MONITOR_ID, "respx")], "nextCursor": None, "hasMore": False}
            )
        )
        ht = HostTracker(token="t", base_url="https://api2.test")
        page = ht.monitors.list_monitor(limit=1)

    assert route.called
    assert page.data[0].name == "respx"


def test_respx_sees_the_retry_and_the_shared_idempotency_key():
    with respx.mock(base_url="https://api2.test") as mock:
        route = mock.post("/check").mock(
            side_effect=[
                httpx.Response(429, json=problem("rate_limited", 429), headers={"Retry-After": "0"}),
                httpx.Response(
                    202,
                    json={
                        "id": "44444444-4444-4444-4444-444444444444",
                        "dbId": 1,
                        "retryAfter": 1,
                        "estimatedDurationSec": 5,
                        "resultUrl": "/check/1/44444444-4444-4444-4444-444444444444",
                        "created": 1735689600,
                    },
                ),
            ]
        )
        ht = HostTracker(token="t", base_url="https://api2.test", max_retries=1)
        ht.instant_checks.create_instant_check(
            body=IcCreateRequest.from_dict({"url": "https://x.test", "type": "http"})
        )

    assert route.call_count == 2
    keys = [call.request.headers.get("Idempotency-Key") for call in route.calls]
    assert len(set(keys)) == 1 and keys[0] is not None


def test_timestamps_round_trip():
    moment = dt.datetime(2025, 1, 1, tzinfo=dt.UTC)
    assert from_datetime(moment) == 1735689600
    assert to_datetime(1735689600) == moment
    assert to_datetime(None) is None
    assert from_datetime(None) is None


def test_naive_datetimes_are_read_as_utc():
    assert from_datetime(dt.datetime(2025, 1, 1)) == 1735689600


def test_to_datetime_is_timezone_aware():
    assert to_datetime(1735689600).tzinfo is not None


async def test_async_client_shares_the_same_surface(make_async_client):
    ht = make_async_client(lambda r: httpx.Response(200, json=EMPTY_PAGE))
    assert (await ht.monitors.list_monitor()).data == []
    await ht.aclose()


async def test_async_client_raises_the_same_error(make_async_client):
    ht = make_async_client(
        lambda r: httpx.Response(
            404, json=problem("not_found", 404), headers={"content-type": "application/problem+json"}
        ),
        max_retries=0,
    )
    with pytest.raises(HostTrackerError) as caught:
        await ht.monitors.get_monitor(MONITOR_ID)
    assert caught.value.code == "not_found"
    await ht.aclose()


async def test_async_context_manager():
    async with AsyncHostTracker(
        token="t",
        base_url="https://api2.test",
        transport=httpx.MockTransport(lambda r: httpx.Response(200, json=EMPTY_PAGE)),
    ) as ht:
        assert (await ht.monitors.list_monitor()).data == []


def test_a_dict_body_is_converted_to_the_operations_request_model(make_client, recorder):
    """`body={...}` works without importing a model first; a model instance passes through."""
    ht = make_client(
        lambda r: httpx.Response(
            202,
            json={
                "id": "44444444-4444-4444-4444-444444444444",
                "dbId": 1,
                "retryAfter": 1,
                "estimatedDurationSec": 5,
                "resultUrl": "/check/1/44444444-4444-4444-4444-444444444444",
                "created": 1735689600,
            },
        )
    )
    ht.instant_checks.create_instant_check(body={"url": "https://x.test", "type": "http"})
    import json as _json

    assert _json.loads(recorder.last.content) == {"url": "https://x.test", "type": "http"}
