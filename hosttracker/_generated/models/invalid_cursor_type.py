from typing import Literal

InvalidCursorType = Literal["https://api2.host-tracker.com/problems/invalid-cursor"]

INVALID_CURSOR_TYPE_VALUES: set[InvalidCursorType] = {
    "https://api2.host-tracker.com/problems/invalid-cursor",
}


def check_invalid_cursor_type(value: str) -> InvalidCursorType:
    if value in INVALID_CURSOR_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_CURSOR_TYPE_VALUES!r}")
