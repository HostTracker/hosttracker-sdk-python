from typing import Literal

QuotaExceededType = Literal["https://api2.host-tracker.com/problems/quota-exceeded"]

QUOTA_EXCEEDED_TYPE_VALUES: set[QuotaExceededType] = {
    "https://api2.host-tracker.com/problems/quota-exceeded",
}


def check_quota_exceeded_type(value: str) -> QuotaExceededType:
    if value in QUOTA_EXCEEDED_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {QUOTA_EXCEEDED_TYPE_VALUES!r}")
