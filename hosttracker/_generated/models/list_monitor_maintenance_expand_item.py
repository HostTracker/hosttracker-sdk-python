from typing import Literal

ListMonitorMaintenanceExpandItem = Literal[
    "monitor", "monitor.lastIncident", "monitor.maintenance", "monitor.settings", "monitor.subscription"
]

LIST_MONITOR_MAINTENANCE_EXPAND_ITEM_VALUES: set[ListMonitorMaintenanceExpandItem] = {
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
}


def check_list_monitor_maintenance_expand_item(value: str) -> ListMonitorMaintenanceExpandItem:
    if value in LIST_MONITOR_MAINTENANCE_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MONITOR_MAINTENANCE_EXPAND_ITEM_VALUES!r}")
