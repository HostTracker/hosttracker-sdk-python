from typing import Literal

ListMonitorSort = Literal[
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

LIST_MONITOR_SORT_VALUES: set[ListMonitorSort] = {
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


def check_list_monitor_sort(value: str) -> ListMonitorSort:
    if value in LIST_MONITOR_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MONITOR_SORT_VALUES!r}")
