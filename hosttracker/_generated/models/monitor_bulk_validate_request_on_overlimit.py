from typing import Literal

MonitorBulkValidateRequestOnOverlimit = Literal["disable", "fail", "stop"]

MONITOR_BULK_VALIDATE_REQUEST_ON_OVERLIMIT_VALUES: set[MonitorBulkValidateRequestOnOverlimit] = {
    "disable",
    "fail",
    "stop",
}


def check_monitor_bulk_validate_request_on_overlimit(value: str) -> MonitorBulkValidateRequestOnOverlimit:
    if value in MONITOR_BULK_VALIDATE_REQUEST_ON_OVERLIMIT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_BULK_VALIDATE_REQUEST_ON_OVERLIMIT_VALUES!r}"
    )
