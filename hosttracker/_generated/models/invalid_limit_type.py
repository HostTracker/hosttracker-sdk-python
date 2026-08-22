from typing import Literal

InvalidLimitType = Literal["https://api2.host-tracker.com/problems/invalid-limit"]

INVALID_LIMIT_TYPE_VALUES: set[InvalidLimitType] = {
    "https://api2.host-tracker.com/problems/invalid-limit",
}


def check_invalid_limit_type(value: str) -> InvalidLimitType:
    if value in INVALID_LIMIT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_LIMIT_TYPE_VALUES!r}")
