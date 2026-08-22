from typing import Literal

MonitorQueryRequestExpandItem = Literal[
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

MONITOR_QUERY_REQUEST_EXPAND_ITEM_VALUES: set[MonitorQueryRequestExpandItem] = {
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


def check_monitor_query_request_expand_item(value: str) -> MonitorQueryRequestExpandItem:
    if value in MONITOR_QUERY_REQUEST_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_QUERY_REQUEST_EXPAND_ITEM_VALUES!r}")
