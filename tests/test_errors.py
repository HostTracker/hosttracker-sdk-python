"""Every failure shape must arrive as ONE exception type with the RFC 9457 fields."""

from __future__ import annotations

import httpx
import pytest

from hosttracker import CODE_HTTP_ERROR, CODE_NETWORK_ERROR, HostTrackerError

from .conftest import PROBLEM_HEADERS, problem


def test_problem_json_maps_every_member(make_client):
    doc = problem(
        "invalid_interval",
        422,
        detail="Interval 7 is not allowed for this type.",
        instance="/monitor",
        errors=[{"pointer": "/interval", "value": 7, "allowed": [1, 5, 15, 30, 60]}],
    )
    ht = make_client(lambda r: httpx.Response(422, json=doc, headers=PROBLEM_HEADERS))

    with pytest.raises(HostTrackerError) as caught:
        ht.monitors.get_monitor("11111111-1111-1111-1111-111111111111")

    err = caught.value
    assert err.code == "invalid_interval"
    assert err.status == 422
    assert err.type == "https://api2.host-tracker.com/problems/invalid-interval"
    assert err.title
    assert err.detail == "Interval 7 is not allowed for this type."
    assert err.instance == "/monitor"
    assert err.errors[0]["pointer"] == "/interval"
    assert err.errors[0]["allowed"] == [1, 5, 15, 30, 60]
    assert err.request_id == "req-test"
    assert err.problem == doc


def test_not_found_is_branchable_by_code(make_client):
    ht = make_client(lambda r: httpx.Response(404, json=problem("not_found", 404), headers=PROBLEM_HEADERS))
    with pytest.raises(HostTrackerError) as caught:
        ht.monitors.get_monitor("00000000-0000-0000-0000-000000000000")
    assert caught.value.code == "not_found"


def test_non_json_502_becomes_http_error(make_client):
    """A proxy's HTML 502 never reaches the caller as a JSON parse crash."""
    html = b"<html><head><title>502 Bad Gateway</title></head><body>nginx</body></html>"
    ht = make_client(lambda r: httpx.Response(502, content=html, headers={"content-type": "text/html"}))

    with pytest.raises(HostTrackerError) as caught:
        ht.account.get_account()

    err = caught.value
    assert err.code == CODE_HTTP_ERROR
    assert err.status == 502
    assert "502 Bad Gateway" in (err.detail or "")
    assert err.body == html


def test_empty_body_failure_still_maps(make_client):
    ht = make_client(lambda r: httpx.Response(500, content=b""))
    with pytest.raises(HostTrackerError) as caught:
        ht.account.get_account()
    assert caught.value.code == CODE_HTTP_ERROR
    assert caught.value.status == 500


def test_transport_failure_becomes_network_error(make_client):
    def boom(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("name resolution failed", request=request)

    ht = make_client(boom, max_retries=0)
    with pytest.raises(HostTrackerError) as caught:
        ht.account.get_account()

    err = caught.value
    assert err.code == CODE_NETWORK_ERROR
    assert err.status is None
    assert isinstance(err.__cause__, httpx.ConnectError)


def test_timeout_is_a_network_error(make_client):
    def slow(request: httpx.Request) -> httpx.Response:
        raise httpx.ReadTimeout("too slow", request=request)

    ht = make_client(slow, max_retries=0)
    with pytest.raises(HostTrackerError) as caught:
        ht.account.get_account()
    assert caught.value.code == CODE_NETWORK_ERROR


def test_rate_limit_snapshot_rides_the_error(make_client):
    headers = {
        **PROBLEM_HEADERS,
        "RateLimit-Policy": "account;q=1000;w=3600",
        "RateLimit-Limit": "1000",
        "RateLimit-Remaining": "0",
        "RateLimit-Reset": "1735689600",
        "Retry-After": "30",
    }
    doc = problem("quota_exceeded", 429, errors=[{"limit": 1000, "remaining": 0, "resetAt": 1735689600}])
    ht = make_client(lambda r: httpx.Response(429, json=doc, headers=headers), max_retries=0)

    with pytest.raises(HostTrackerError) as caught:
        ht.account.get_account()

    err = caught.value
    assert err.code == "quota_exceeded"
    assert err.retry_after == 30
    assert err.rate_limit.metered is True
    assert err.rate_limit.limit == 1000
    assert err.rate_limit.remaining == 0
    assert err.rate_limit.reset == 1735689600


def test_unmetered_scope_reports_policy_none_without_numbers(make_client):
    ht = make_client(
        lambda r: httpx.Response(403, json=problem("missing_scope", 403), headers={"RateLimit-Policy": "none"}),
        max_retries=0,
    )
    with pytest.raises(HostTrackerError) as caught:
        ht.account.get_account()
    assert caught.value.rate_limit.policy == "none"
    assert caught.value.rate_limit.metered is False
    assert caught.value.rate_limit.limit is None


def test_raise_on_error_false_returns_the_problem_model(make_client):
    """Opting out gives the generated problem model instead of an exception."""
    ht = make_client(
        lambda r: httpx.Response(404, json=problem("not_found", 404), headers=PROBLEM_HEADERS),
        raise_on_error=False,
        max_retries=0,
    )
    parsed = ht.monitors.get_monitor("00000000-0000-0000-0000-000000000000")
    assert parsed.code == "not_found"
