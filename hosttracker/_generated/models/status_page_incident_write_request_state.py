from typing import Literal

StatusPageIncidentWriteRequestState = Literal["identified", "investigating", "monitoring", "resolved"]

STATUS_PAGE_INCIDENT_WRITE_REQUEST_STATE_VALUES: set[StatusPageIncidentWriteRequestState] = {
    "identified",
    "investigating",
    "monitoring",
    "resolved",
}


def check_status_page_incident_write_request_state(value: str) -> StatusPageIncidentWriteRequestState:
    if value in STATUS_PAGE_INCIDENT_WRITE_REQUEST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_INCIDENT_WRITE_REQUEST_STATE_VALUES!r}")
