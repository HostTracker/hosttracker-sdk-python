from typing import Literal

ListMonitorIncidentExpandItem = Literal[
    "count",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
]

LIST_MONITOR_INCIDENT_EXPAND_ITEM_VALUES: set[ListMonitorIncidentExpandItem] = {
    "count",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
}


def check_list_monitor_incident_expand_item(value: str) -> ListMonitorIncidentExpandItem:
    if value in LIST_MONITOR_INCIDENT_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MONITOR_INCIDENT_EXPAND_ITEM_VALUES!r}")
