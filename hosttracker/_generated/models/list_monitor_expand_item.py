from typing import Literal

ListMonitorExpandItem = Literal[
    "attached",
    "count",
    "lastIncident",
    "lastResult",
    "lastResult.metrics",
    "lastResult.recheck",
    "maintenance",
    "settings",
    "spans",
    "subscription",
    "summary",
    "uptime",
]

LIST_MONITOR_EXPAND_ITEM_VALUES: set[ListMonitorExpandItem] = {
    "attached",
    "count",
    "lastIncident",
    "lastResult",
    "lastResult.metrics",
    "lastResult.recheck",
    "maintenance",
    "settings",
    "spans",
    "subscription",
    "summary",
    "uptime",
}


def check_list_monitor_expand_item(value: str) -> ListMonitorExpandItem:
    if value in LIST_MONITOR_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MONITOR_EXPAND_ITEM_VALUES!r}")
