from typing import Literal

UnknownExpandCode = Literal["unknown_expand"]

UNKNOWN_EXPAND_CODE_VALUES: set[UnknownExpandCode] = {
    "unknown_expand",
}


def check_unknown_expand_code(value: str) -> UnknownExpandCode:
    if value in UNKNOWN_EXPAND_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_EXPAND_CODE_VALUES!r}")
