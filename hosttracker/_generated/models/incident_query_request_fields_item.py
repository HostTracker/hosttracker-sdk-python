from typing import Literal

IncidentQueryRequestFieldsItem = Literal[
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

INCIDENT_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[IncidentQueryRequestFieldsItem] = {
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


def check_incident_query_request_fields_item(value: str) -> IncidentQueryRequestFieldsItem:
    if value in INCIDENT_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
