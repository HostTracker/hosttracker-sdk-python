from typing import Literal

UnknownContactRefStatus = Literal[422]

UNKNOWN_CONTACT_REF_STATUS_VALUES: set[UnknownContactRefStatus] = {
    422,
}


def check_unknown_contact_ref_status(value: int) -> UnknownContactRefStatus:
    if value in UNKNOWN_CONTACT_REF_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_CONTACT_REF_STATUS_VALUES!r}")
