from typing import Literal

MonitorMaintenanceQueryRequestExpandItem = Literal[
    "monitor", "monitor.lastIncident", "monitor.maintenance", "monitor.settings", "monitor.subscription"
]

MONITOR_MAINTENANCE_QUERY_REQUEST_EXPAND_ITEM_VALUES: set[MonitorMaintenanceQueryRequestExpandItem] = {
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
}


def check_monitor_maintenance_query_request_expand_item(value: str) -> MonitorMaintenanceQueryRequestExpandItem:
    if value in MONITOR_MAINTENANCE_QUERY_REQUEST_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_MAINTENANCE_QUERY_REQUEST_EXPAND_ITEM_VALUES!r}"
    )
