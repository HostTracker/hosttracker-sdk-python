from typing import Literal

IntervalBelowTypeFloorType = Literal["https://api2.host-tracker.com/problems/interval-below-type-floor"]

INTERVAL_BELOW_TYPE_FLOOR_TYPE_VALUES: set[IntervalBelowTypeFloorType] = {
    "https://api2.host-tracker.com/problems/interval-below-type-floor",
}


def check_interval_below_type_floor_type(value: str) -> IntervalBelowTypeFloorType:
    if value in INTERVAL_BELOW_TYPE_FLOOR_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INTERVAL_BELOW_TYPE_FLOOR_TYPE_VALUES!r}")
