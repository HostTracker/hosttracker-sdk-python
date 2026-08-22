from typing import Literal

MonitorBulkCreateRequestOnError = Literal["continue", "stop"]

MONITOR_BULK_CREATE_REQUEST_ON_ERROR_VALUES: set[MonitorBulkCreateRequestOnError] = {
    "continue",
    "stop",
}


def check_monitor_bulk_create_request_on_error(value: str) -> MonitorBulkCreateRequestOnError:
    if value in MONITOR_BULK_CREATE_REQUEST_ON_ERROR_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_BULK_CREATE_REQUEST_ON_ERROR_VALUES!r}")
