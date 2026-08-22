from typing import Literal

ValidationFailedCode = Literal["validation_failed"]

VALIDATION_FAILED_CODE_VALUES: set[ValidationFailedCode] = {
    "validation_failed",
}


def check_validation_failed_code(value: str) -> ValidationFailedCode:
    if value in VALIDATION_FAILED_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VALIDATION_FAILED_CODE_VALUES!r}")
