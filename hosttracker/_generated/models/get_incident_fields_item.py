from typing import Literal

GetIncidentFieldsItem = Literal[
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

GET_INCIDENT_FIELDS_ITEM_VALUES: set[GetIncidentFieldsItem] = {
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


def check_get_incident_fields_item(value: str) -> GetIncidentFieldsItem:
    if value in GET_INCIDENT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_INCIDENT_FIELDS_ITEM_VALUES!r}")
