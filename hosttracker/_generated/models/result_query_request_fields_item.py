from typing import Literal

ResultQueryRequestFieldsItem = Literal[
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

RESULT_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[ResultQueryRequestFieldsItem] = {
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


def check_result_query_request_fields_item(value: str) -> ResultQueryRequestFieldsItem:
    if value in RESULT_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESULT_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
