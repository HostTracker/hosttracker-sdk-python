from typing import Literal

IdempotencyKeyConflictType = Literal["https://api2.host-tracker.com/problems/idempotency-key-conflict"]

IDEMPOTENCY_KEY_CONFLICT_TYPE_VALUES: set[IdempotencyKeyConflictType] = {
    "https://api2.host-tracker.com/problems/idempotency-key-conflict",
}


def check_idempotency_key_conflict_type(value: str) -> IdempotencyKeyConflictType:
    if value in IDEMPOTENCY_KEY_CONFLICT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IDEMPOTENCY_KEY_CONFLICT_TYPE_VALUES!r}")
