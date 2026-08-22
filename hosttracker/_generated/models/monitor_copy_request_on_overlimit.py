from typing import Literal

MonitorCopyRequestOnOverlimit = Literal["disable", "fail"]

MONITOR_COPY_REQUEST_ON_OVERLIMIT_VALUES: set[MonitorCopyRequestOnOverlimit] = {
    "disable",
    "fail",
}


def check_monitor_copy_request_on_overlimit(value: str) -> MonitorCopyRequestOnOverlimit:
    if value in MONITOR_COPY_REQUEST_ON_OVERLIMIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_COPY_REQUEST_ON_OVERLIMIT_VALUES!r}")
