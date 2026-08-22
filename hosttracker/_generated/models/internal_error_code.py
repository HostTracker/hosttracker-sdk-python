from typing import Literal

InternalErrorCode = Literal["internal_error"]

INTERNAL_ERROR_CODE_VALUES: set[InternalErrorCode] = {
    "internal_error",
}


def check_internal_error_code(value: str) -> InternalErrorCode:
    if value in INTERNAL_ERROR_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INTERNAL_ERROR_CODE_VALUES!r}")
