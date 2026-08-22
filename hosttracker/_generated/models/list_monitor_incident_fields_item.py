from typing import Literal

ListMonitorIncidentFieldsItem = Literal[
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

LIST_MONITOR_INCIDENT_FIELDS_ITEM_VALUES: set[ListMonitorIncidentFieldsItem] = {
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


def check_list_monitor_incident_fields_item(value: str) -> ListMonitorIncidentFieldsItem:
    if value in LIST_MONITOR_INCIDENT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MONITOR_INCIDENT_FIELDS_ITEM_VALUES!r}")
