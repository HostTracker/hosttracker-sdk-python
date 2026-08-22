from typing import Literal

InternalErrorStatus = Literal[500]

INTERNAL_ERROR_STATUS_VALUES: set[InternalErrorStatus] = {
    500,
}


def check_internal_error_status(value: int) -> InternalErrorStatus:
    if value in INTERNAL_ERROR_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INTERNAL_ERROR_STATUS_VALUES!r}")
