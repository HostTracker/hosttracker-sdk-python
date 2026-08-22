from typing import Literal

MonitorViewState = Literal["down", "maintenance", "paused", "up"]

MONITOR_VIEW_STATE_VALUES: set[MonitorViewState] = {
    "down",
    "maintenance",
    "paused",
    "up",
}


def check_monitor_view_state(value: str) -> MonitorViewState:
    if value in MONITOR_VIEW_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_VIEW_STATE_VALUES!r}")
