from typing import Literal

MonitorResultQueryRequestFieldsItem = Literal[
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

MONITOR_RESULT_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[MonitorResultQueryRequestFieldsItem] = {
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


def check_monitor_result_query_request_fields_item(value: str) -> MonitorResultQueryRequestFieldsItem:
    if value in MONITOR_RESULT_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_RESULT_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
