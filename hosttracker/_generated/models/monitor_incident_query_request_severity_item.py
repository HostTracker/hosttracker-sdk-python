from typing import Literal

MonitorIncidentQueryRequestSeverityItem = Literal["critical", "major", "minor"]

MONITOR_INCIDENT_QUERY_REQUEST_SEVERITY_ITEM_VALUES: set[MonitorIncidentQueryRequestSeverityItem] = {
    "critical",
    "major",
    "minor",
}


def check_monitor_incident_query_request_severity_item(value: str) -> MonitorIncidentQueryRequestSeverityItem:
    if value in MONITOR_INCIDENT_QUERY_REQUEST_SEVERITY_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_INCIDENT_QUERY_REQUEST_SEVERITY_ITEM_VALUES!r}"
    )
