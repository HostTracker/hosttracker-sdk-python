from typing import Literal

InvalidLimitCode = Literal["invalid_limit"]

INVALID_LIMIT_CODE_VALUES: set[InvalidLimitCode] = {
    "invalid_limit",
}


def check_invalid_limit_code(value: str) -> InvalidLimitCode:
    if value in INVALID_LIMIT_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_LIMIT_CODE_VALUES!r}")
