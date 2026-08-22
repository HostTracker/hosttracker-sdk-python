from typing import Literal

DuplicateMonitorCode = Literal["duplicate_monitor"]

DUPLICATE_MONITOR_CODE_VALUES: set[DuplicateMonitorCode] = {
    "duplicate_monitor",
}


def check_duplicate_monitor_code(value: str) -> DuplicateMonitorCode:
    if value in DUPLICATE_MONITOR_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DUPLICATE_MONITOR_CODE_VALUES!r}")
