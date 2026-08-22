from typing import Literal

UpstreamErrorCode = Literal["upstream_error"]

UPSTREAM_ERROR_CODE_VALUES: set[UpstreamErrorCode] = {
    "upstream_error",
}


def check_upstream_error_code(value: str) -> UpstreamErrorCode:
    if value in UPSTREAM_ERROR_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPSTREAM_ERROR_CODE_VALUES!r}")
