from typing import Literal

ContactAlreadyConfirmedType = Literal["https://api2.host-tracker.com/problems/contact-already-confirmed"]

CONTACT_ALREADY_CONFIRMED_TYPE_VALUES: set[ContactAlreadyConfirmedType] = {
    "https://api2.host-tracker.com/problems/contact-already-confirmed",
}


def check_contact_already_confirmed_type(value: str) -> ContactAlreadyConfirmedType:
    if value in CONTACT_ALREADY_CONFIRMED_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_ALREADY_CONFIRMED_TYPE_VALUES!r}")
