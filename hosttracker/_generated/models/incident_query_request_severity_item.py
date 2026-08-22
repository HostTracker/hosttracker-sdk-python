from typing import Literal

IncidentQueryRequestSeverityItem = Literal["critical", "major", "minor"]

INCIDENT_QUERY_REQUEST_SEVERITY_ITEM_VALUES: set[IncidentQueryRequestSeverityItem] = {
    "critical",
    "major",
    "minor",
}


def check_incident_query_request_severity_item(value: str) -> IncidentQueryRequestSeverityItem:
    if value in INCIDENT_QUERY_REQUEST_SEVERITY_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_QUERY_REQUEST_SEVERITY_ITEM_VALUES!r}")
