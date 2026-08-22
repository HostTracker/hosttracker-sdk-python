from typing import Literal

InvalidRangeCode = Literal["invalid_range"]

INVALID_RANGE_CODE_VALUES: set[InvalidRangeCode] = {
    "invalid_range",
}


def check_invalid_range_code(value: str) -> InvalidRangeCode:
    if value in INVALID_RANGE_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_RANGE_CODE_VALUES!r}")
