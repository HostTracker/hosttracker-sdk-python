from typing import Literal

GetMonitorResultExpandItem = Literal[
    "count",
    "metrics",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
]

GET_MONITOR_RESULT_EXPAND_ITEM_VALUES: set[GetMonitorResultExpandItem] = {
    "count",
    "metrics",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
}


def check_get_monitor_result_expand_item(value: str) -> GetMonitorResultExpandItem:
    if value in GET_MONITOR_RESULT_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_MONITOR_RESULT_EXPAND_ITEM_VALUES!r}")
