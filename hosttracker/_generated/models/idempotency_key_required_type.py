from typing import Literal

IdempotencyKeyRequiredType = Literal["https://api2.host-tracker.com/problems/idempotency-key-required"]

IDEMPOTENCY_KEY_REQUIRED_TYPE_VALUES: set[IdempotencyKeyRequiredType] = {
    "https://api2.host-tracker.com/problems/idempotency-key-required",
}


def check_idempotency_key_required_type(value: str) -> IdempotencyKeyRequiredType:
    if value in IDEMPOTENCY_KEY_REQUIRED_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IDEMPOTENCY_KEY_REQUIRED_TYPE_VALUES!r}")
