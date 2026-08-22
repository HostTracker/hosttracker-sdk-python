from typing import Literal

UnknownPoolType = Literal["https://api2.host-tracker.com/problems/unknown-pool"]

UNKNOWN_POOL_TYPE_VALUES: set[UnknownPoolType] = {
    "https://api2.host-tracker.com/problems/unknown-pool",
}


def check_unknown_pool_type(value: str) -> UnknownPoolType:
    if value in UNKNOWN_POOL_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_POOL_TYPE_VALUES!r}")
