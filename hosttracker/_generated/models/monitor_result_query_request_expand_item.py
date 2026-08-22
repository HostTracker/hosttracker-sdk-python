from typing import Literal

MonitorResultQueryRequestExpandItem = Literal[
    "count",
    "metrics",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
]

MONITOR_RESULT_QUERY_REQUEST_EXPAND_ITEM_VALUES: set[MonitorResultQueryRequestExpandItem] = {
    "count",
    "metrics",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
}


def check_monitor_result_query_request_expand_item(value: str) -> MonitorResultQueryRequestExpandItem:
    if value in MONITOR_RESULT_QUERY_REQUEST_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_RESULT_QUERY_REQUEST_EXPAND_ITEM_VALUES!r}")
