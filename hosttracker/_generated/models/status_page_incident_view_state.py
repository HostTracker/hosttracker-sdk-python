from typing import Literal

StatusPageIncidentViewState = Literal["identified", "investigating", "monitoring", "resolved"]

STATUS_PAGE_INCIDENT_VIEW_STATE_VALUES: set[StatusPageIncidentViewState] = {
    "identified",
    "investigating",
    "monitoring",
    "resolved",
}


def check_status_page_incident_view_state(value: str) -> StatusPageIncidentViewState:
    if value in STATUS_PAGE_INCIDENT_VIEW_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_INCIDENT_VIEW_STATE_VALUES!r}")
