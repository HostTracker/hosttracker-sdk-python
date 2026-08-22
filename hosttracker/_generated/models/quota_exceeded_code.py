from typing import Literal

QuotaExceededCode = Literal["quota_exceeded"]

QUOTA_EXCEEDED_CODE_VALUES: set[QuotaExceededCode] = {
    "quota_exceeded",
}


def check_quota_exceeded_code(value: str) -> QuotaExceededCode:
    if value in QUOTA_EXCEEDED_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {QUOTA_EXCEEDED_CODE_VALUES!r}")
