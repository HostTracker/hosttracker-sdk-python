from typing import Literal

GetMonitorResultFieldsItem = Literal[
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

GET_MONITOR_RESULT_FIELDS_ITEM_VALUES: set[GetMonitorResultFieldsItem] = {
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


def check_get_monitor_result_fields_item(value: str) -> GetMonitorResultFieldsItem:
    if value in GET_MONITOR_RESULT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_MONITOR_RESULT_FIELDS_ITEM_VALUES!r}")
