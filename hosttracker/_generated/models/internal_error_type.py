from typing import Literal

InternalErrorType = Literal["https://api2.host-tracker.com/problems/internal-error"]

INTERNAL_ERROR_TYPE_VALUES: set[InternalErrorType] = {
    "https://api2.host-tracker.com/problems/internal-error",
}


def check_internal_error_type(value: str) -> InternalErrorType:
    if value in INTERNAL_ERROR_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INTERNAL_ERROR_TYPE_VALUES!r}")
