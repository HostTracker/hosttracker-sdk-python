from typing import Literal

IncidentViewState = Literal["open", "resolved"]

INCIDENT_VIEW_STATE_VALUES: set[IncidentViewState] = {
    "open",
    "resolved",
}


def check_incident_view_state(value: str) -> IncidentViewState:
    if value in INCIDENT_VIEW_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_VIEW_STATE_VALUES!r}")
