from typing import Literal

ListMaintenanceExpandItem = Literal[
    "monitor", "monitor.lastIncident", "monitor.maintenance", "monitor.settings", "monitor.subscription"
]

LIST_MAINTENANCE_EXPAND_ITEM_VALUES: set[ListMaintenanceExpandItem] = {
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
}


def check_list_maintenance_expand_item(value: str) -> ListMaintenanceExpandItem:
    if value in LIST_MAINTENANCE_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MAINTENANCE_EXPAND_ITEM_VALUES!r}")
