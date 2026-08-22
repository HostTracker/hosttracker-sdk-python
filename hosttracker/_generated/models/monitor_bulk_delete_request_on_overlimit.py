from typing import Literal

MonitorBulkDeleteRequestOnOverlimit = Literal["disable", "fail", "stop"]

MONITOR_BULK_DELETE_REQUEST_ON_OVERLIMIT_VALUES: set[MonitorBulkDeleteRequestOnOverlimit] = {
    "disable",
    "fail",
    "stop",
}


def check_monitor_bulk_delete_request_on_overlimit(value: str) -> MonitorBulkDeleteRequestOnOverlimit:
    if value in MONITOR_BULK_DELETE_REQUEST_ON_OVERLIMIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_BULK_DELETE_REQUEST_ON_OVERLIMIT_VALUES!r}")
