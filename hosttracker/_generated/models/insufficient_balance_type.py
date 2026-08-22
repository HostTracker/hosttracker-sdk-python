from typing import Literal

InsufficientBalanceType = Literal["https://api2.host-tracker.com/problems/insufficient-balance"]

INSUFFICIENT_BALANCE_TYPE_VALUES: set[InsufficientBalanceType] = {
    "https://api2.host-tracker.com/problems/insufficient-balance",
}


def check_insufficient_balance_type(value: str) -> InsufficientBalanceType:
    if value in INSUFFICIENT_BALANCE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INSUFFICIENT_BALANCE_TYPE_VALUES!r}")
