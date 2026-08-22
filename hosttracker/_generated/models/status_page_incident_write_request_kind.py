from typing import Literal

StatusPageIncidentWriteRequestKind = Literal["incident", "maintenance"]

STATUS_PAGE_INCIDENT_WRITE_REQUEST_KIND_VALUES: set[StatusPageIncidentWriteRequestKind] = {
    "incident",
    "maintenance",
}


def check_status_page_incident_write_request_kind(value: str) -> StatusPageIncidentWriteRequestKind:
    if value in STATUS_PAGE_INCIDENT_WRITE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_INCIDENT_WRITE_REQUEST_KIND_VALUES!r}")
