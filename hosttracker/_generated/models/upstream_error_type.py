from typing import Literal

UpstreamErrorType = Literal["https://api2.host-tracker.com/problems/upstream-error"]

UPSTREAM_ERROR_TYPE_VALUES: set[UpstreamErrorType] = {
    "https://api2.host-tracker.com/problems/upstream-error",
}


def check_upstream_error_type(value: str) -> UpstreamErrorType:
    if value in UPSTREAM_ERROR_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPSTREAM_ERROR_TYPE_VALUES!r}")
