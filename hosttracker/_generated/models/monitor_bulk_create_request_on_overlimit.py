from typing import Literal

MonitorBulkCreateRequestOnOverlimit = Literal["disable", "fail", "stop"]

MONITOR_BULK_CREATE_REQUEST_ON_OVERLIMIT_VALUES: set[MonitorBulkCreateRequestOnOverlimit] = {
    "disable",
    "fail",
    "stop",
}


def check_monitor_bulk_create_request_on_overlimit(value: str) -> MonitorBulkCreateRequestOnOverlimit:
    if value in MONITOR_BULK_CREATE_REQUEST_ON_OVERLIMIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_BULK_CREATE_REQUEST_ON_OVERLIMIT_VALUES!r}")
