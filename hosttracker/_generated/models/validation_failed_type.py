from typing import Literal

ValidationFailedType = Literal["https://api2.host-tracker.com/problems/validation-failed"]

VALIDATION_FAILED_TYPE_VALUES: set[ValidationFailedType] = {
    "https://api2.host-tracker.com/problems/validation-failed",
}


def check_validation_failed_type(value: str) -> ValidationFailedType:
    if value in VALIDATION_FAILED_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VALIDATION_FAILED_TYPE_VALUES!r}")
