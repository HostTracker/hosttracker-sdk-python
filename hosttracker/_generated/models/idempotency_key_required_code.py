from typing import Literal

IdempotencyKeyRequiredCode = Literal["idempotency_key_required"]

IDEMPOTENCY_KEY_REQUIRED_CODE_VALUES: set[IdempotencyKeyRequiredCode] = {
    "idempotency_key_required",
}


def check_idempotency_key_required_code(value: str) -> IdempotencyKeyRequiredCode:
    if value in IDEMPOTENCY_KEY_REQUIRED_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IDEMPOTENCY_KEY_REQUIRED_CODE_VALUES!r}")
