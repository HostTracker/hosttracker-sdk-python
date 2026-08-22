from typing import Literal

MonitorBulkUpdateRequestOperation = Literal["resetStats"]

MONITOR_BULK_UPDATE_REQUEST_OPERATION_VALUES: set[MonitorBulkUpdateRequestOperation] = {
    "resetStats",
}


def check_monitor_bulk_update_request_operation(value: str) -> MonitorBulkUpdateRequestOperation:
    if value in MONITOR_BULK_UPDATE_REQUEST_OPERATION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_BULK_UPDATE_REQUEST_OPERATION_VALUES!r}")
