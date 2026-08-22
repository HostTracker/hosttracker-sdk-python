from typing import Literal

MonitorWriteRequestOnOverlimit = Literal["disable", "fail"]

MONITOR_WRITE_REQUEST_ON_OVERLIMIT_VALUES: set[MonitorWriteRequestOnOverlimit] = {
    "disable",
    "fail",
}


def check_monitor_write_request_on_overlimit(value: str) -> MonitorWriteRequestOnOverlimit:
    if value in MONITOR_WRITE_REQUEST_ON_OVERLIMIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_WRITE_REQUEST_ON_OVERLIMIT_VALUES!r}")
