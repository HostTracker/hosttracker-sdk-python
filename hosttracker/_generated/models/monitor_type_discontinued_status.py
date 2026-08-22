from typing import Literal

MonitorTypeDiscontinuedStatus = Literal[422]

MONITOR_TYPE_DISCONTINUED_STATUS_VALUES: set[MonitorTypeDiscontinuedStatus] = {
    422,
}


def check_monitor_type_discontinued_status(value: int) -> MonitorTypeDiscontinuedStatus:
    if value in MONITOR_TYPE_DISCONTINUED_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_TYPE_DISCONTINUED_STATUS_VALUES!r}")
