from typing import Literal

StatusPageIncidentWriteRequestImpact = Literal["major", "minor"]

STATUS_PAGE_INCIDENT_WRITE_REQUEST_IMPACT_VALUES: set[StatusPageIncidentWriteRequestImpact] = {
    "major",
    "minor",
}


def check_status_page_incident_write_request_impact(value: str) -> StatusPageIncidentWriteRequestImpact:
    if value in STATUS_PAGE_INCIDENT_WRITE_REQUEST_IMPACT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_INCIDENT_WRITE_REQUEST_IMPACT_VALUES!r}")
