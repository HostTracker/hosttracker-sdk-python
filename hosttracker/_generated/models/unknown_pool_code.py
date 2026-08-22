from typing import Literal

UnknownPoolCode = Literal["unknown_pool"]

UNKNOWN_POOL_CODE_VALUES: set[UnknownPoolCode] = {
    "unknown_pool",
}


def check_unknown_pool_code(value: str) -> UnknownPoolCode:
    if value in UNKNOWN_POOL_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_POOL_CODE_VALUES!r}")
