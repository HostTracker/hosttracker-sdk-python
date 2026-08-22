from typing import Literal

IntervalBelowTypeFloorCode = Literal["interval_below_type_floor"]

INTERVAL_BELOW_TYPE_FLOOR_CODE_VALUES: set[IntervalBelowTypeFloorCode] = {
    "interval_below_type_floor",
}


def check_interval_below_type_floor_code(value: str) -> IntervalBelowTypeFloorCode:
    if value in INTERVAL_BELOW_TYPE_FLOOR_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INTERVAL_BELOW_TYPE_FLOOR_CODE_VALUES!r}")
