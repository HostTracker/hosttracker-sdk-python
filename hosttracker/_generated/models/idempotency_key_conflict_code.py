from typing import Literal

IdempotencyKeyConflictCode = Literal["idempotency_key_conflict"]

IDEMPOTENCY_KEY_CONFLICT_CODE_VALUES: set[IdempotencyKeyConflictCode] = {
    "idempotency_key_conflict",
}


def check_idempotency_key_conflict_code(value: str) -> IdempotencyKeyConflictCode:
    if value in IDEMPOTENCY_KEY_CONFLICT_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IDEMPOTENCY_KEY_CONFLICT_CODE_VALUES!r}")
