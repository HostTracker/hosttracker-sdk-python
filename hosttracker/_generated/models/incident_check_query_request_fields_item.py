from typing import Literal

IncidentCheckQueryRequestFieldsItem = Literal[
    "assertEv",
    "assertFails",
    "at",
    "checkCount",
    "checkNumber",
    "durationSec",
    "error",
    "hasSnapshot",
    "id",
    "location",
    "metrics",
    "monitor",
    "monitorId",
    "policyViolations",
    "recheck",
    "snapshotUrl",
    "state",
    "underMaintenance",
]

INCIDENT_CHECK_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[IncidentCheckQueryRequestFieldsItem] = {
    "assertEv",
    "assertFails",
    "at",
    "checkCount",
    "checkNumber",
    "durationSec",
    "error",
    "hasSnapshot",
    "id",
    "location",
    "metrics",
    "monitor",
    "monitorId",
    "policyViolations",
    "recheck",
    "snapshotUrl",
    "state",
    "underMaintenance",
}


def check_incident_check_query_request_fields_item(value: str) -> IncidentCheckQueryRequestFieldsItem:
    if value in INCIDENT_CHECK_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_CHECK_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
