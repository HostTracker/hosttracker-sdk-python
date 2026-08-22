from typing import Literal

InvalidLimitStatus = Literal[422]

INVALID_LIMIT_STATUS_VALUES: set[InvalidLimitStatus] = {
    422,
}


def check_invalid_limit_status(value: int) -> InvalidLimitStatus:
    if value in INVALID_LIMIT_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_LIMIT_STATUS_VALUES!r}")
