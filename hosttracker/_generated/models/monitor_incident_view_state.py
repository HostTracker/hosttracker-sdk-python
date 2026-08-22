from typing import Literal

MonitorIncidentViewState = Literal["down", "up"]

MONITOR_INCIDENT_VIEW_STATE_VALUES: set[MonitorIncidentViewState] = {
    "down",
    "up",
}


def check_monitor_incident_view_state(value: str) -> MonitorIncidentViewState:
    if value in MONITOR_INCIDENT_VIEW_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_INCIDENT_VIEW_STATE_VALUES!r}")
