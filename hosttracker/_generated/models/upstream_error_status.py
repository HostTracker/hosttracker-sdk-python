from typing import Literal

UpstreamErrorStatus = Literal[502]

UPSTREAM_ERROR_STATUS_VALUES: set[UpstreamErrorStatus] = {
    502,
}


def check_upstream_error_status(value: int) -> UpstreamErrorStatus:
    if value in UPSTREAM_ERROR_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPSTREAM_ERROR_STATUS_VALUES!r}")
