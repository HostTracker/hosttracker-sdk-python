from typing import Literal

MaintenanceViewState = Literal["active", "finished", "scheduled"]

MAINTENANCE_VIEW_STATE_VALUES: set[MaintenanceViewState] = {
    "active",
    "finished",
    "scheduled",
}


def check_maintenance_view_state(value: str) -> MaintenanceViewState:
    if value in MAINTENANCE_VIEW_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_VIEW_STATE_VALUES!r}")
