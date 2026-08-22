from typing import Literal

IdempotencyKeyRequiredStatus = Literal[400]

IDEMPOTENCY_KEY_REQUIRED_STATUS_VALUES: set[IdempotencyKeyRequiredStatus] = {
    400,
}


def check_idempotency_key_required_status(value: int) -> IdempotencyKeyRequiredStatus:
    if value in IDEMPOTENCY_KEY_REQUIRED_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IDEMPOTENCY_KEY_REQUIRED_STATUS_VALUES!r}")
