from typing import Literal

ValidationFailedStatus = Literal[422]

VALIDATION_FAILED_STATUS_VALUES: set[ValidationFailedStatus] = {
    422,
}


def check_validation_failed_status(value: int) -> ValidationFailedStatus:
    if value in VALIDATION_FAILED_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VALIDATION_FAILED_STATUS_VALUES!r}")
