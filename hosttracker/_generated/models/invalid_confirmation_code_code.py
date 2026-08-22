from typing import Literal

InvalidConfirmationCodeCode = Literal["invalid_confirmation_code"]

INVALID_CONFIRMATION_CODE_CODE_VALUES: set[InvalidConfirmationCodeCode] = {
    "invalid_confirmation_code",
}


def check_invalid_confirmation_code_code(value: str) -> InvalidConfirmationCodeCode:
    if value in INVALID_CONFIRMATION_CODE_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_CONFIRMATION_CODE_CODE_VALUES!r}")
