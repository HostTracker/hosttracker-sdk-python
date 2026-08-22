from typing import Literal

ListMonitorResultExpandItem = Literal[
    "count",
    "metrics",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
]

LIST_MONITOR_RESULT_EXPAND_ITEM_VALUES: set[ListMonitorResultExpandItem] = {
    "count",
    "metrics",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
}


def check_list_monitor_result_expand_item(value: str) -> ListMonitorResultExpandItem:
    if value in LIST_MONITOR_RESULT_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MONITOR_RESULT_EXPAND_ITEM_VALUES!r}")
