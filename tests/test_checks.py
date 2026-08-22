"""``run_check`` - POST /check, then FOLLOW ``resultUrl`` until ``state == "done"``."""

from __future__ import annotations

import httpx
import pytest

from hosttracker import CODE_HTTP_ERROR, CODE_TIMEOUT, HostTrackerError

from .conftest import BASE_URL, TOKEN

CHECK_ID = "44444444-4444-4444-4444-444444444444"
RESULT_PATH = f"/check/7/{CHECK_ID}"
FOREIGN_RESULT_URL = f"https://evil.test{RESULT_PATH}?verbose=1"

CREATED = {
    "id": CHECK_ID,
    "dbId": 7,
    "retryAfter": 3,
    "estimatedDurationSec": 20,
    "resultUrl": RESULT_PATH,
    "created": 1735689600,
}


def result(state: str, **extra) -> dict:
    doc = {"id": CHECK_ID, "dbId": 7, "state": state, "created": 1735689600, "events": []}
    doc.update(extra)
    return doc


def _pipeline(poll_states: list[dict]):
    remaining = list(poll_states)

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/check" and request.method == "POST":
            return httpx.Response(202, json=CREATED, headers={"Location": RESULT_PATH})
        return httpx.Response(200, json=remaining.pop(0))

    return handler


def test_follows_result_url_rather_than_building_a_path(make_client, recorder, sleeps):
    ht = make_client(_pipeline([result("running", retryAfter=5), result("done", doneAt=1735689630)]))

    final = ht.run_check({"url": "https://www.host-tracker.com", "type": "http"})

    assert final.state == "done"
    assert [r.url.path for r in recorder.requests] == ["/check", RESULT_PATH, RESULT_PATH]
    # The FIRST wait is the create response's retryAfter, then the poll's own.
    assert sleeps == [3.0, 5.0]


def test_returns_immediately_when_the_first_poll_is_done(make_client, recorder, sleeps):
    ht = make_client(_pipeline([result("done", doneAt=1735689630)]))
    final = ht.run_check({"url": "https://x.test", "type": "http"})
    assert final.state == "done"
    assert len(recorder) == 2


def test_poll_interval_overrides_the_server_hint(make_client, sleeps):
    ht = make_client(_pipeline([result("running"), result("done")]))
    ht.run_check({"url": "https://x.test", "type": "http"}, poll_interval=0.5)
    assert sleeps == [0.5, 0.5]


def test_on_poll_sees_the_growing_event_list(make_client, sleeps):
    """`events[]` grows as fleet locations report - that is why on_poll exists."""
    seen: list[int] = []
    de = {"agentId": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa", "location": "de-fra", "doneAt": 1735689610}
    us = {"agentId": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb", "location": "us-nyc", "doneAt": 1735689615}
    ht = make_client(_pipeline([result("running", events=[de]), result("done", events=[de, us])]))
    ht.run_check({"url": "https://x.test", "type": "http"}, on_poll=lambda v: seen.append(len(v.events)))
    assert seen == [1, 2]


def test_timeout_raises(make_client, monkeypatch):
    clock = {"t": 0.0}
    monkeypatch.setattr("hosttracker.checks.time.monotonic", lambda: clock["t"])
    monkeypatch.setattr("time.sleep", lambda s: clock.__setitem__("t", clock["t"] + s))

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/check" and request.method == "POST":
            return httpx.Response(202, json=CREATED)
        return httpx.Response(200, json=result("running", retryAfter=5))

    ht = make_client(handler)
    with pytest.raises(HostTrackerError) as caught:
        ht.run_check({"url": "https://x.test", "type": "http"}, timeout=11)
    assert caught.value.code == CODE_TIMEOUT


def test_a_refused_create_surfaces_the_problem(make_client):
    """The API refuses outright when the pipeline is down - never a fake 202."""
    doc = {
        "type": "https://api2.host-tracker.com/problems/service-unavailable",
        "title": "Service unavailable",
        "status": 503,
        "code": "service_unavailable",
    }
    ht = make_client(
        lambda r: httpx.Response(503, json=doc, headers={"content-type": "application/problem+json"}),
        max_retries=0,
    )
    with pytest.raises(HostTrackerError) as caught:
        ht.run_check({"url": "https://x.test", "type": "http"})
    assert caught.value.code == "service_unavailable"


def test_unknown_pool_is_a_422(make_client):
    doc = {
        "type": "https://api2.host-tracker.com/problems/unknown-pool",
        "title": "Unknown pool",
        "status": 422,
        "code": "unknown_pool",
        "errors": [{"pointer": "/pools", "value": "nowhere"}],
    }
    ht = make_client(
        lambda r: httpx.Response(422, json=doc, headers={"content-type": "application/problem+json"}),
        max_retries=0,
    )
    with pytest.raises(HostTrackerError) as caught:
        ht.run_check({"url": "https://x.test", "type": "http", "pools": ["nowhere"]})
    assert caught.value.code == "unknown_pool"
    assert caught.value.errors[0]["pointer"] == "/pools"


def test_falls_back_to_the_generated_operation_without_a_result_url(make_client, recorder, sleeps):
    """An empty ``resultUrl`` and no ``Location``: the path still comes from the spec, not by hand.

    The spec marks ``resultUrl`` required, so the member is always there; the fallback covers
    the degenerate answer that carries it blank.
    """
    created = {**CREATED, "resultUrl": ""}

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/check" and request.method == "POST":
            return httpx.Response(202, json=created)
        return httpx.Response(200, json=result("done"))

    ht = make_client(handler)
    final = ht.run_check({"url": "https://x.test", "type": "http"})
    assert final.state == "done"
    assert recorder.requests[1].url.path == RESULT_PATH


async def test_async_run_check(make_async_client, recorder, sleeps):
    ht = make_async_client(_pipeline([result("running", retryAfter=2), result("done")]))
    final = await ht.run_check({"url": "https://x.test", "type": "http"})
    assert final.state == "done"
    assert sleeps == [3.0, 2.0]
    await ht.aclose()


def _pipeline_with_result_url(result_url: str, poll_states: list[dict]):
    """The create answer names `result_url` in both the body and the Location header."""
    created = {**CREATED, "resultUrl": result_url}
    remaining = list(poll_states)

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/check" and request.method == "POST":
            return httpx.Response(202, json=created, headers={"Location": result_url})
        return httpx.Response(200, json=remaining.pop(0))

    return handler


def test_a_foreign_result_url_is_rebased_onto_the_configured_host(make_client, recorder, sleeps):
    """The token rides every request, so only the path and query of resultUrl survive."""
    ht = make_client(_pipeline_with_result_url(FOREIGN_RESULT_URL, [result("done")]))

    final = ht.run_check({"url": "https://x.test", "type": "http"})

    assert final.state == "done"
    poll = recorder.requests[1]
    assert str(poll.url) == f"{BASE_URL}{RESULT_PATH}?verbose=1"
    assert poll.headers["Authorization"] == f"Bearer {TOKEN}"
    assert [r.url.host for r in recorder.requests] == ["api2.test", "api2.test"]


@pytest.mark.parametrize("bad_url", ["file:///etc/passwd", "ftp://files.test/check/7/x", "FILE://x/y"])
def test_a_result_url_that_is_not_http_is_refused(make_client, recorder, sleeps, bad_url):
    """Refused before the poll: only the create call reached the transport."""
    ht = make_client(_pipeline_with_result_url(bad_url, [result("done")]))

    with pytest.raises(HostTrackerError) as caught:
        ht.run_check({"url": "https://x.test", "type": "http"})

    assert caught.value.code == CODE_HTTP_ERROR
    assert "will not follow" in str(caught.value)
    assert [r.url.path for r in recorder.requests] == ["/check"]
    assert sleeps == []


async def test_async_rebases_a_foreign_result_url(make_async_client, recorder, sleeps):
    ht = make_async_client(_pipeline_with_result_url(FOREIGN_RESULT_URL, [result("done")]))

    final = await ht.run_check({"url": "https://x.test", "type": "http"})

    assert final.state == "done"
    poll = recorder.requests[1]
    assert str(poll.url) == f"{BASE_URL}{RESULT_PATH}?verbose=1"
    assert poll.headers["Authorization"] == f"Bearer {TOKEN}"
    assert [r.url.host for r in recorder.requests] == ["api2.test", "api2.test"]
    await ht.aclose()


async def test_async_refuses_a_result_url_that_is_not_http(make_async_client, recorder, sleeps):
    ht = make_async_client(_pipeline_with_result_url("file:///etc/passwd", [result("done")]))

    with pytest.raises(HostTrackerError) as caught:
        await ht.run_check({"url": "https://x.test", "type": "http"})

    assert caught.value.code == CODE_HTTP_ERROR
    assert [r.url.path for r in recorder.requests] == ["/check"]
    assert sleeps == []
    await ht.aclose()
