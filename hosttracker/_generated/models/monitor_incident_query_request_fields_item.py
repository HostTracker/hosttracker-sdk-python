from typing import Literal

MonitorIncidentQueryRequestFieldsItem = Literal[
    "cause",
    "checkCount",
    "comment",
    "durationSec",
    "end",
    "id",
    "monitor",
    "monitorId",
    "recheck",
    "severity",
    "start",
    "state",
    "timeline",
    "underMaintenance",
]

MONITOR_INCIDENT_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[MonitorIncidentQueryRequestFieldsItem] = {
    "cause",
    "checkCount",
    "comment",
    "durationSec",
    "end",
    "id",
    "monitor",
    "monitorId",
    "recheck",
    "severity",
    "start",
    "state",
    "timeline",
    "underMaintenance",
}


def check_monitor_incident_query_request_fields_item(value: str) -> MonitorIncidentQueryRequestFieldsItem:
    if value in MONITOR_INCIDENT_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_INCIDENT_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}"
    )
