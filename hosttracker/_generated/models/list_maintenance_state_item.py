from typing import Literal

ListMaintenanceStateItem = Literal["active", "finished", "scheduled"]

LIST_MAINTENANCE_STATE_ITEM_VALUES: set[ListMaintenanceStateItem] = {
    "active",
    "finished",
    "scheduled",
}


def check_list_maintenance_state_item(value: str) -> ListMaintenanceStateItem:
    if value in LIST_MAINTENANCE_STATE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MAINTENANCE_STATE_ITEM_VALUES!r}")
