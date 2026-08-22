from typing import Literal

IntervalBelowTypeFloorStatus = Literal[422]

INTERVAL_BELOW_TYPE_FLOOR_STATUS_VALUES: set[IntervalBelowTypeFloorStatus] = {
    422,
}


def check_interval_below_type_floor_status(value: int) -> IntervalBelowTypeFloorStatus:
    if value in INTERVAL_BELOW_TYPE_FLOOR_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INTERVAL_BELOW_TYPE_FLOOR_STATUS_VALUES!r}")
