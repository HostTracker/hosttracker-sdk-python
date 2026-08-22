from typing import Literal

MonitorBulkDeleteRequestOnError = Literal["continue", "stop"]

MONITOR_BULK_DELETE_REQUEST_ON_ERROR_VALUES: set[MonitorBulkDeleteRequestOnError] = {
    "continue",
    "stop",
}


def check_monitor_bulk_delete_request_on_error(value: str) -> MonitorBulkDeleteRequestOnError:
    if value in MONITOR_BULK_DELETE_REQUEST_ON_ERROR_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_BULK_DELETE_REQUEST_ON_ERROR_VALUES!r}")
