from typing import Literal

MonitorQueryRequestSort = Literal[
    "created",
    "created:asc",
    "created:desc",
    "interval",
    "interval:asc",
    "interval:desc",
    "lastChange",
    "lastChange:asc",
    "lastChange:desc",
    "name",
    "name:asc",
    "name:desc",
    "state",
    "state:asc",
    "state:desc",
    "tags",
    "tags:asc",
    "tags:desc",
    "type",
    "type:asc",
    "type:desc",
    "url",
    "url:asc",
    "url:desc",
]

MONITOR_QUERY_REQUEST_SORT_VALUES: set[MonitorQueryRequestSort] = {
    "created",
    "created:asc",
    "created:desc",
    "interval",
    "interval:asc",
    "interval:desc",
    "lastChange",
    "lastChange:asc",
    "lastChange:desc",
    "name",
    "name:asc",
    "name:desc",
    "state",
    "state:asc",
    "state:desc",
    "tags",
    "tags:asc",
    "tags:desc",
    "type",
    "type:asc",
    "type:desc",
    "url",
    "url:asc",
    "url:desc",
}


def check_monitor_query_request_sort(value: str) -> MonitorQueryRequestSort:
    if value in MONITOR_QUERY_REQUEST_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_QUERY_REQUEST_SORT_VALUES!r}")
