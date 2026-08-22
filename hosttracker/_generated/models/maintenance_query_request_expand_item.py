from typing import Literal

MaintenanceQueryRequestExpandItem = Literal[
    "monitor", "monitor.lastIncident", "monitor.maintenance", "monitor.settings", "monitor.subscription"
]

MAINTENANCE_QUERY_REQUEST_EXPAND_ITEM_VALUES: set[MaintenanceQueryRequestExpandItem] = {
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
}


def check_maintenance_query_request_expand_item(value: str) -> MaintenanceQueryRequestExpandItem:
    if value in MAINTENANCE_QUERY_REQUEST_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_QUERY_REQUEST_EXPAND_ITEM_VALUES!r}")
