from typing import Literal

InvalidCursorStatus = Literal[422]

INVALID_CURSOR_STATUS_VALUES: set[InvalidCursorStatus] = {
    422,
}


def check_invalid_cursor_status(value: int) -> InvalidCursorStatus:
    if value in INVALID_CURSOR_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_CURSOR_STATUS_VALUES!r}")
