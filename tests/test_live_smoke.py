"""Opt-in smoke run against a real API instance.

Skipped unless ``HT_BASE_URL`` is set. Read-only by design - it never creates, edits or
deletes a monitor, contact or webhook. The one write it makes is ``POST /check``, which
creates a one-off check rather than a stored resource.

::

    HT_BASE_URL=https://api2.host-tracker.com \
    HT_TOKEN_FILE=/path/to/token \
    .venv/bin/python -m pytest tests/test_live_smoke.py -v

``HT_INSECURE=1`` disables TLS verification and is ONLY for a local instance with a
self-signed certificate. Never use it against a public host.
"""

from __future__ import annotations

import os
import pathlib

import pytest

from hosttracker import HostTracker, HostTrackerError

BASE_URL = os.environ.get("HT_BASE_URL")

pytestmark = pytest.mark.skipif(not BASE_URL, reason="set HT_BASE_URL to run the live smoke")

ZERO_GUID = "00000000-0000-0000-0000-000000000000"


def _token() -> str | None:
    token = os.environ.get("HT_TOKEN")
    if token:
        return token.strip()
    path = os.environ.get("HT_TOKEN_FILE")
    if path:
        return pathlib.Path(path).read_text(encoding="utf-8").strip()
    return None


def _verify() -> bool:
    # Only a local instance with a self-signed certificate may opt out of verification.
    return os.environ.get("HT_INSECURE", "").strip() not in ("1", "true", "yes")


@pytest.fixture(scope="module")
def ht():
    token = _token()
    if not token:
        pytest.skip("set HT_TOKEN or HT_TOKEN_FILE to run the authenticated smoke")
    client = HostTracker(token=token, base_url=BASE_URL, verify=_verify(), timeout=60)
    yield client
    client.close()


@pytest.fixture(scope="module")
def anon():
    client = HostTracker(base_url=BASE_URL, verify=_verify(), timeout=60)
    yield client
    client.close()


def test_get_account(ht):
    account = ht.account.get_account()
    assert account is not None
    print(f"\n[smoke] GET /account -> id={getattr(account, 'id', '?')}")


def test_get_account_quota(ht):
    quota = ht.account.get_account_quota()
    assert quota is not None
    print(f"[smoke] GET /account/quota -> apiEnabled={quota.api_enabled} scopes={getattr(quota, 'scopes', None)}")


def test_list_monitors_and_paginate(ht):
    page = ht.monitors.list_monitor(limit=2, detailed=True)
    assert page.status_code == 200
    assert page.parsed is not None
    print(f"[smoke] GET /monitor?limit=2 -> {len(page.parsed.data)} rows, nextCursor={page.parsed.next_cursor!r}")

    rows = list(ht.paginate(ht.monitors.list_monitor, limit=2, max_pages=3))
    print(f"[smoke] paginate(3 pages max) -> {len(rows)} rows")
    assert len(rows) >= len(page.parsed.data)


def test_reference_tier_needs_no_token(anon):
    types = anon.monitor_types.list_monitor_type()
    assert types is not None
    # `type` is a Python builtin, so the generator names the attribute `type_`.
    names = [getattr(row, "type_", None) for row in types.data][:8]
    print(f"[smoke] GET /monitor/type (anonymous) -> {len(types.data)} types: {names}")


def test_get_one_monitor_with_expand(ht):
    page = ht.monitors.list_monitor(limit=1)
    if not page.data:
        pytest.skip("the smoke account has no monitors")
    monitor_id = str(page.data[0].id)
    detailed = ht.monitors.get_monitor(monitor_id, expand=["settings"])
    assert str(detailed.id) == monitor_id
    print(f"[smoke] GET /monitor/{monitor_id}?expand=settings -> name={detailed.name!r}")


def test_unknown_monitor_maps_to_not_found(ht):
    with pytest.raises(HostTrackerError) as caught:
        ht.monitors.get_monitor(ZERO_GUID)
    err = caught.value
    print(f"[smoke] GET /monitor/{ZERO_GUID} -> {err.status} {err.code} type={err.type!r} request_id={err.request_id}")
    assert err.code == "not_found"
    assert err.status == 404


def test_run_instant_check(ht):
    try:
        result = ht.run_check({"url": "https://www.host-tracker.com", "type": "http"}, timeout=90)
    except HostTrackerError as exc:
        if exc.code == "service_unavailable":
            # A refused create is the documented behaviour when the pipeline is down.
            print(f"[smoke] POST /check refused (environment): {exc.status} {exc.code} - {exc.detail}")
            return
        raise
    print(f"[smoke] POST /check -> state={result.state} events={len(result.events or [])} doneAt={result.done_at}")
    assert result.state == "done"
