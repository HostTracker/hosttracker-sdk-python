from typing import Literal

InvalidRangeType = Literal["https://api2.host-tracker.com/problems/invalid-range"]

INVALID_RANGE_TYPE_VALUES: set[InvalidRangeType] = {
    "https://api2.host-tracker.com/problems/invalid-range",
}


def check_invalid_range_type(value: str) -> InvalidRangeType:
    if value in INVALID_RANGE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_RANGE_TYPE_VALUES!r}")
