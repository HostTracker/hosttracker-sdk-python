from typing import Literal

MonitorBulkUpdateValidateRequestOperation = Literal["resetStats"]

MONITOR_BULK_UPDATE_VALIDATE_REQUEST_OPERATION_VALUES: set[MonitorBulkUpdateValidateRequestOperation] = {
    "resetStats",
}


def check_monitor_bulk_update_validate_request_operation(value: str) -> MonitorBulkUpdateValidateRequestOperation:
    if value in MONITOR_BULK_UPDATE_VALIDATE_REQUEST_OPERATION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_BULK_UPDATE_VALIDATE_REQUEST_OPERATION_VALUES!r}"
    )
