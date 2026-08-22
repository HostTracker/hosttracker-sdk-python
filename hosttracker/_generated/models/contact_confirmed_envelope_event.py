from typing import Literal

ContactConfirmedEnvelopeEvent = Literal["contact.confirmed"]

CONTACT_CONFIRMED_ENVELOPE_EVENT_VALUES: set[ContactConfirmedEnvelopeEvent] = {
    "contact.confirmed",
}


def check_contact_confirmed_envelope_event(value: str) -> ContactConfirmedEnvelopeEvent:
    if value in CONTACT_CONFIRMED_ENVELOPE_EVENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_CONFIRMED_ENVELOPE_EVENT_VALUES!r}")
