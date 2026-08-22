"""Cursor paging over the v2 collection envelope.

Every collection answers the same envelope - ``{data, nextCursor, hasMore, syncCursor?,
count?, summary?}`` - so one loop drives all of them. Cursors are OPAQUE: never build,
parse or mutate one, and never replay one under a different ``sort``.
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Callable, Iterator
from typing import Any

from ._generated.types import Unset

__all__ = ["apages", "apaginate", "pages", "paginate"]


def _cursor_of(page: Any) -> str | None:
    """The next cursor, or None when this was the last page."""
    if page is None:
        return None
    cursor = getattr(page, "next_cursor", None)
    if cursor is None or isinstance(cursor, Unset):
        return None
    cursor = str(cursor)
    return cursor or None


def _rows_of(page: Any) -> list[Any]:
    rows = getattr(page, "data", None)
    if rows is None or isinstance(rows, Unset):
        return []
    return list(rows)


def pages(
    list_call: Callable[..., Any],
    /,
    *args: Any,
    max_pages: int | None = None,
    **params: Any,
) -> Iterator[Any]:
    """Yield the PAGE envelopes of a list operation, following ``nextCursor``.

    Use this variant when you need the envelope's own members - ``syncCursor`` for the
    next incremental poll, ``count`` (``expand=count``) or ``summary``::

        for page in ht.pages(ht.monitors.list_monitor, limit=200, expand="count"):
            print(page.count.matched, len(page.data))

    ``list_call`` is any callable that answers a page: a bound operation such as
    ``ht.monitors.list_monitor``, or a generated ``list_monitor.sync`` given ``client=``.
    Extra positional/keyword arguments are forwarded unchanged on every request; the
    ``cursor`` argument is supplied by the loop.

    This drives the ``GET`` list operations. The ``POST <path>/q`` body-query twins take
    their cursor INSIDE the request body, so drive those yourself - read ``next_cursor``
    off each page and put it in the next body.
    """
    cursor: str | None = None
    seen = 0
    while True:
        call_params = dict(params)
        if cursor is not None:
            call_params["cursor"] = cursor
        page = list_call(*args, **call_params)
        yield page
        seen += 1
        if max_pages is not None and seen >= max_pages:
            return
        nxt = _cursor_of(page)
        if nxt is None or nxt == cursor:
            # `nextCursor: null` is the documented end. An unchanged cursor would be a
            # server-side fault; stopping beats looping forever.
            return
        cursor = nxt


def paginate(
    list_call: Callable[..., Any],
    /,
    *args: Any,
    max_pages: int | None = None,
    **params: Any,
) -> Iterator[Any]:
    """Yield the ITEMS of a list operation across every page::

    for monitor in ht.paginate(ht.monitors.list_monitor, limit=200, state="down"):
        print(monitor.name)
    """
    for page in pages(list_call, *args, max_pages=max_pages, **params):
        yield from _rows_of(page)


async def apages(
    list_call: Callable[..., Any],
    /,
    *args: Any,
    max_pages: int | None = None,
    **params: Any,
) -> AsyncIterator[Any]:
    """Async twin of :func:`pages`."""
    cursor: str | None = None
    seen = 0
    while True:
        call_params = dict(params)
        if cursor is not None:
            call_params["cursor"] = cursor
        page = await list_call(*args, **call_params)
        yield page
        seen += 1
        if max_pages is not None and seen >= max_pages:
            return
        nxt = _cursor_of(page)
        if nxt is None or nxt == cursor:
            return
        cursor = nxt


async def apaginate(
    list_call: Callable[..., Any],
    /,
    *args: Any,
    max_pages: int | None = None,
    **params: Any,
) -> AsyncIterator[Any]:
    """Async twin of :func:`paginate`."""
    async for page in apages(list_call, *args, max_pages=max_pages, **params):
        for row in _rows_of(page):
            yield row
