from typing import Literal

IdempotencyKeyConflictStatus = Literal[409]

IDEMPOTENCY_KEY_CONFLICT_STATUS_VALUES: set[IdempotencyKeyConflictStatus] = {
    409,
}


def check_idempotency_key_conflict_status(value: int) -> IdempotencyKeyConflictStatus:
    if value in IDEMPOTENCY_KEY_CONFLICT_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IDEMPOTENCY_KEY_CONFLICT_STATUS_VALUES!r}")
