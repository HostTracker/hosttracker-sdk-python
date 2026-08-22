"""Unix-seconds helpers.

Every instant on this API - request, response, webhook envelope - is an integer count of
seconds since the Unix epoch. Never ISO-8601, never milliseconds. The one exception is a
member whose name ends in ``Ms`` (``latencyMs``): that is an elapsed duration, not an
instant, and these helpers do not apply to it.
"""

from __future__ import annotations

from datetime import UTC, datetime

__all__ = ["from_datetime", "to_datetime"]


def to_datetime(seconds: int | float | None) -> datetime | None:
    """Unix seconds -> an aware UTC :class:`~datetime.datetime` (``None`` passes through)."""
    if seconds is None:
        return None
    return datetime.fromtimestamp(float(seconds), tz=UTC)


def from_datetime(value: datetime | None) -> int | None:
    """A :class:`~datetime.datetime` -> Unix seconds (``None`` passes through).

    A NAIVE datetime is read as UTC, because that is what the API speaks; attach a
    ``tzinfo`` when the value is really local time.
    """
    if value is None:
        return None
    if value.tzinfo is None:
        value = value.replace(tzinfo=UTC)
    return int(value.timestamp())
