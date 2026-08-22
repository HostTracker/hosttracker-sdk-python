from typing import Literal

DuplicateMonitorStatus = Literal[409]

DUPLICATE_MONITOR_STATUS_VALUES: set[DuplicateMonitorStatus] = {
    409,
}


def check_duplicate_monitor_status(value: int) -> DuplicateMonitorStatus:
    if value in DUPLICATE_MONITOR_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DUPLICATE_MONITOR_STATUS_VALUES!r}")
