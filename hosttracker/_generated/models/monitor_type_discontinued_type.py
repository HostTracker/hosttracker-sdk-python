from typing import Literal

MonitorTypeDiscontinuedType = Literal["https://api2.host-tracker.com/problems/monitor-type-discontinued"]

MONITOR_TYPE_DISCONTINUED_TYPE_VALUES: set[MonitorTypeDiscontinuedType] = {
    "https://api2.host-tracker.com/problems/monitor-type-discontinued",
}


def check_monitor_type_discontinued_type(value: str) -> MonitorTypeDiscontinuedType:
    if value in MONITOR_TYPE_DISCONTINUED_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_TYPE_DISCONTINUED_TYPE_VALUES!r}")
