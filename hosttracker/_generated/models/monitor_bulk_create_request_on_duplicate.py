from typing import Literal

MonitorBulkCreateRequestOnDuplicate = Literal["createAnyway", "fail", "skip"]

MONITOR_BULK_CREATE_REQUEST_ON_DUPLICATE_VALUES: set[MonitorBulkCreateRequestOnDuplicate] = {
    "createAnyway",
    "fail",
    "skip",
}


def check_monitor_bulk_create_request_on_duplicate(value: str) -> MonitorBulkCreateRequestOnDuplicate:
    if value in MONITOR_BULK_CREATE_REQUEST_ON_DUPLICATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_BULK_CREATE_REQUEST_ON_DUPLICATE_VALUES!r}")
