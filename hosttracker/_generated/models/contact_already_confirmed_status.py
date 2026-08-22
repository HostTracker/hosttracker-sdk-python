from typing import Literal

ContactAlreadyConfirmedStatus = Literal[409]

CONTACT_ALREADY_CONFIRMED_STATUS_VALUES: set[ContactAlreadyConfirmedStatus] = {
    409,
}


def check_contact_already_confirmed_status(value: int) -> ContactAlreadyConfirmedStatus:
    if value in CONTACT_ALREADY_CONFIRMED_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_ALREADY_CONFIRMED_STATUS_VALUES!r}")
