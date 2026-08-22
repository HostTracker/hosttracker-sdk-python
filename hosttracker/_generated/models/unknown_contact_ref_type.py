from typing import Literal

UnknownContactRefType = Literal["https://api2.host-tracker.com/problems/unknown-contact-ref"]

UNKNOWN_CONTACT_REF_TYPE_VALUES: set[UnknownContactRefType] = {
    "https://api2.host-tracker.com/problems/unknown-contact-ref",
}


def check_unknown_contact_ref_type(value: str) -> UnknownContactRefType:
    if value in UNKNOWN_CONTACT_REF_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_CONTACT_REF_TYPE_VALUES!r}")
