from typing import Literal

GetMaintenanceExpandItem = Literal[
    "monitor", "monitor.lastIncident", "monitor.maintenance", "monitor.settings", "monitor.subscription"
]

GET_MAINTENANCE_EXPAND_ITEM_VALUES: set[GetMaintenanceExpandItem] = {
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
}


def check_get_maintenance_expand_item(value: str) -> GetMaintenanceExpandItem:
    if value in GET_MAINTENANCE_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_MAINTENANCE_EXPAND_ITEM_VALUES!r}")
