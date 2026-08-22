from typing import Literal

MonitorPatchRequestOnOverlimit = Literal["disable", "fail"]

MONITOR_PATCH_REQUEST_ON_OVERLIMIT_VALUES: set[MonitorPatchRequestOnOverlimit] = {
    "disable",
    "fail",
}


def check_monitor_patch_request_on_overlimit(value: str) -> MonitorPatchRequestOnOverlimit:
    if value in MONITOR_PATCH_REQUEST_ON_OVERLIMIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_PATCH_REQUEST_ON_OVERLIMIT_VALUES!r}")
