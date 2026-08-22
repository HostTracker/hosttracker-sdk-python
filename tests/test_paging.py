"""The cursor loop: follow ``nextCursor``, stop when it is null."""

from __future__ import annotations

import httpx
import pytest

from hosttracker import pages, paginate

from .conftest import MONITOR_A, MONITOR_B, MONITOR_C, monitor_row

PAGES = {
    None: {
        "data": [monitor_row(MONITOR_A, "alpha")],
        "nextCursor": "cursor-2",
        "hasMore": True,
        "syncCursor": "sync-1",
        "count": {"total": 3, "matched": 3},
    },
    "cursor-2": {
        "data": [monitor_row(MONITOR_B, "beta")],
        "nextCursor": "cursor-3",
        "hasMore": True,
    },
    "cursor-3": {
        "data": [monitor_row(MONITOR_C, "gamma")],
        "nextCursor": None,
        "hasMore": False,
    },
}


def _three_pages(request: httpx.Request) -> httpx.Response:
    return httpx.Response(200, json=PAGES[request.url.params.get("cursor")])


def test_paginate_walks_every_page_and_stops_on_null_cursor(make_client, recorder):
    ht = make_client(_three_pages)
    names = [m.name for m in ht.paginate(ht.monitors.list_monitor, limit=1)]
    assert names == ["alpha", "beta", "gamma"]
    assert len(recorder) == 3
    assert [r.url.params.get("cursor") for r in recorder.requests] == [None, "cursor-2", "cursor-3"]


def test_pages_exposes_the_envelope_members(make_client):
    ht = make_client(_three_pages)
    first = next(iter(ht.pages(ht.monitors.list_monitor, limit=1)))
    assert first.sync_cursor == "sync-1"
    assert first.count.total == 3
    assert first.count.matched == 3


def test_filters_are_repeated_on_every_page(make_client, recorder):
    ht = make_client(_three_pages)
    list(ht.paginate(ht.monitors.list_monitor, limit=1, state=["down"]))
    assert all(r.url.params.get_list("state") == ["down"] for r in recorder.requests)


def test_max_pages_stops_early(make_client, recorder):
    ht = make_client(_three_pages)
    rows = list(ht.paginate(ht.monitors.list_monitor, limit=1, max_pages=2))
    assert len(rows) == 2
    assert len(recorder) == 2


def test_module_level_paginate_accepts_any_callable():
    """The helper is generic - it drives anything that answers the envelope shape."""
    seen: list[str | None] = []

    class FakePage:
        def __init__(self, data, next_cursor):
            self.data = data
            self.next_cursor = next_cursor

    def call(*, cursor=None, limit=None):
        seen.append(cursor)
        if cursor is None:
            return FakePage(["a"], "c2")
        return FakePage(["b"], None)

    assert list(paginate(call, limit=10)) == ["a", "b"]
    assert seen == [None, "c2"]


def test_a_repeated_cursor_terminates_instead_of_looping():
    """A server fault must not turn into an infinite client loop."""

    class FakePage:
        data = ["x"]
        next_cursor = "stuck"

    calls = {"n": 0}

    def call(*, cursor=None):
        calls["n"] += 1
        return FakePage()

    rows = list(paginate(call))
    assert rows == ["x", "x"]  # first page, then the repeat is detected
    assert calls["n"] == 2


def test_empty_page_yields_nothing(make_client):
    ht = make_client(lambda r: httpx.Response(200, json={"data": [], "nextCursor": None, "hasMore": False}))
    assert list(ht.paginate(ht.monitors.list_monitor)) == []


async def test_async_pagination(make_async_client, recorder):
    ht = make_async_client(_three_pages)
    names = [m.name async for m in ht.paginate(ht.monitors.list_monitor, limit=1)]
    assert names == ["alpha", "beta", "gamma"]
    assert len(recorder) == 3
    await ht.aclose()


@pytest.mark.parametrize("helper", [paginate, pages])
def test_helpers_are_exported(helper):
    assert callable(helper)
