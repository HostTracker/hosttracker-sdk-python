from typing import Literal

InvalidCursorCode = Literal["invalid_cursor"]

INVALID_CURSOR_CODE_VALUES: set[InvalidCursorCode] = {
    "invalid_cursor",
}


def check_invalid_cursor_code(value: str) -> InvalidCursorCode:
    if value in INVALID_CURSOR_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_CURSOR_CODE_VALUES!r}")
