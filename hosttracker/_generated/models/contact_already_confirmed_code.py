from typing import Literal

ContactAlreadyConfirmedCode = Literal["contact_already_confirmed"]

CONTACT_ALREADY_CONFIRMED_CODE_VALUES: set[ContactAlreadyConfirmedCode] = {
    "contact_already_confirmed",
}


def check_contact_already_confirmed_code(value: str) -> ContactAlreadyConfirmedCode:
    if value in CONTACT_ALREADY_CONFIRMED_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_ALREADY_CONFIRMED_CODE_VALUES!r}")
