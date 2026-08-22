from typing import Literal

InsufficientBalanceStatus = Literal[402]

INSUFFICIENT_BALANCE_STATUS_VALUES: set[InsufficientBalanceStatus] = {
    402,
}


def check_insufficient_balance_status(value: int) -> InsufficientBalanceStatus:
    if value in INSUFFICIENT_BALANCE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INSUFFICIENT_BALANCE_STATUS_VALUES!r}")
