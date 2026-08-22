from typing import Literal

InvalidConfirmationCodeType = Literal["https://api2.host-tracker.com/problems/invalid-confirmation-code"]

INVALID_CONFIRMATION_CODE_TYPE_VALUES: set[InvalidConfirmationCodeType] = {
    "https://api2.host-tracker.com/problems/invalid-confirmation-code",
}


def check_invalid_confirmation_code_type(value: str) -> InvalidConfirmationCodeType:
    if value in INVALID_CONFIRMATION_CODE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_CONFIRMATION_CODE_TYPE_VALUES!r}")
