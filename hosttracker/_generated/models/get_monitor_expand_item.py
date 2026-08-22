from typing import Literal

GetMonitorExpandItem = Literal[
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

GET_MONITOR_EXPAND_ITEM_VALUES: set[GetMonitorExpandItem] = {
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


def check_get_monitor_expand_item(value: str) -> GetMonitorExpandItem:
    if value in GET_MONITOR_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_MONITOR_EXPAND_ITEM_VALUES!r}")
