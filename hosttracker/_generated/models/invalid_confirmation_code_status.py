from typing import Literal

InvalidConfirmationCodeStatus = Literal[422]

INVALID_CONFIRMATION_CODE_STATUS_VALUES: set[InvalidConfirmationCodeStatus] = {
    422,
}


def check_invalid_confirmation_code_status(value: int) -> InvalidConfirmationCodeStatus:
    if value in INVALID_CONFIRMATION_CODE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_CONFIRMATION_CODE_STATUS_VALUES!r}")
