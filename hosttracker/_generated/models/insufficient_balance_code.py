from typing import Literal

InsufficientBalanceCode = Literal["insufficient_balance"]

INSUFFICIENT_BALANCE_CODE_VALUES: set[InsufficientBalanceCode] = {
    "insufficient_balance",
}


def check_insufficient_balance_code(value: str) -> InsufficientBalanceCode:
    if value in INSUFFICIENT_BALANCE_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INSUFFICIENT_BALANCE_CODE_VALUES!r}")
