from typing import Literal

DuplicateMonitorType = Literal["https://api2.host-tracker.com/problems/duplicate-monitor"]

DUPLICATE_MONITOR_TYPE_VALUES: set[DuplicateMonitorType] = {
    "https://api2.host-tracker.com/problems/duplicate-monitor",
}


def check_duplicate_monitor_type(value: str) -> DuplicateMonitorType:
    if value in DUPLICATE_MONITOR_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DUPLICATE_MONITOR_TYPE_VALUES!r}")
