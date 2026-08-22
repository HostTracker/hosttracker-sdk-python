from typing import Literal

MonitorBulkUpdateRequestOnError = Literal["continue", "stop"]

MONITOR_BULK_UPDATE_REQUEST_ON_ERROR_VALUES: set[MonitorBulkUpdateRequestOnError] = {
    "continue",
    "stop",
}


def check_monitor_bulk_update_request_on_error(value: str) -> MonitorBulkUpdateRequestOnError:
    if value in MONITOR_BULK_UPDATE_REQUEST_ON_ERROR_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_BULK_UPDATE_REQUEST_ON_ERROR_VALUES!r}")
