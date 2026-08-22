from typing import Literal

MaintenanceQueryRequestStateItem = Literal["active", "finished", "scheduled"]

MAINTENANCE_QUERY_REQUEST_STATE_ITEM_VALUES: set[MaintenanceQueryRequestStateItem] = {
    "active",
    "finished",
    "scheduled",
}


def check_maintenance_query_request_state_item(value: str) -> MaintenanceQueryRequestStateItem:
    if value in MAINTENANCE_QUERY_REQUEST_STATE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_QUERY_REQUEST_STATE_ITEM_VALUES!r}")
