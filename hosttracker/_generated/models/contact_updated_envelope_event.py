from typing import Literal

ContactUpdatedEnvelopeEvent = Literal["contact.updated"]

CONTACT_UPDATED_ENVELOPE_EVENT_VALUES: set[ContactUpdatedEnvelopeEvent] = {
    "contact.updated",
}


def check_contact_updated_envelope_event(value: str) -> ContactUpdatedEnvelopeEvent:
    if value in CONTACT_UPDATED_ENVELOPE_EVENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_UPDATED_ENVELOPE_EVENT_VALUES!r}")
