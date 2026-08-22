from typing import Literal

ListMonitorResultFieldsItem = Literal[
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

LIST_MONITOR_RESULT_FIELDS_ITEM_VALUES: set[ListMonitorResultFieldsItem] = {
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


def check_list_monitor_result_fields_item(value: str) -> ListMonitorResultFieldsItem:
    if value in LIST_MONITOR_RESULT_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MONITOR_RESULT_FIELDS_ITEM_VALUES!r}")
