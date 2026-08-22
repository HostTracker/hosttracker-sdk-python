from typing import Literal

MonitorBulkValidateRequestOnDuplicate = Literal["createAnyway", "fail", "skip"]

MONITOR_BULK_VALIDATE_REQUEST_ON_DUPLICATE_VALUES: set[MonitorBulkValidateRequestOnDuplicate] = {
    "createAnyway",
    "fail",
    "skip",
}


def check_monitor_bulk_validate_request_on_duplicate(value: str) -> MonitorBulkValidateRequestOnDuplicate:
    if value in MONITOR_BULK_VALIDATE_REQUEST_ON_DUPLICATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_BULK_VALIDATE_REQUEST_ON_DUPLICATE_VALUES!r}"
    )
