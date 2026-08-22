from typing import Literal

ListIncidentFieldsItem = Literal[
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

LIST_INCIDENT_FIELDS_ITEM_VALUES: set[ListIncidentFieldsItem] = {
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


def check_list_incident_fields_item(value: str) -> ListIncidentFieldsItem:
    if value in LIST_INCIDENT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INCIDENT_FIELDS_ITEM_VALUES!r}")
