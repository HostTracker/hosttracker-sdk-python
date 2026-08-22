from typing import Literal

MonitorBulkUpdateRequestOnOverlimit = Literal["disable", "fail", "stop"]

MONITOR_BULK_UPDATE_REQUEST_ON_OVERLIMIT_VALUES: set[MonitorBulkUpdateRequestOnOverlimit] = {
    "disable",
    "fail",
    "stop",
}


def check_monitor_bulk_update_request_on_overlimit(value: str) -> MonitorBulkUpdateRequestOnOverlimit:
    if value in MONITOR_BULK_UPDATE_REQUEST_ON_OVERLIMIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_BULK_UPDATE_REQUEST_ON_OVERLIMIT_VALUES!r}")
