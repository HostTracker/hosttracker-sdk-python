from typing import Literal

QuotaExceededStatus = Literal[429]

QUOTA_EXCEEDED_STATUS_VALUES: set[QuotaExceededStatus] = {
    429,
}


def check_quota_exceeded_status(value: int) -> QuotaExceededStatus:
    if value in QUOTA_EXCEEDED_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {QUOTA_EXCEEDED_STATUS_VALUES!r}")
