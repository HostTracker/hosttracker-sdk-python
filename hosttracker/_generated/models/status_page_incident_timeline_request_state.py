from typing import Literal

StatusPageIncidentTimelineRequestState = Literal["identified", "investigating", "monitoring", "resolved"]

STATUS_PAGE_INCIDENT_TIMELINE_REQUEST_STATE_VALUES: set[StatusPageIncidentTimelineRequestState] = {
    "identified",
    "investigating",
    "monitoring",
    "resolved",
}


def check_status_page_incident_timeline_request_state(value: str) -> StatusPageIncidentTimelineRequestState:
    if value in STATUS_PAGE_INCIDENT_TIMELINE_REQUEST_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_INCIDENT_TIMELINE_REQUEST_STATE_VALUES!r}"
    )
