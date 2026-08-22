from typing import Literal

IncidentOpenedEnvelopeEvent = Literal["incident.opened"]

INCIDENT_OPENED_ENVELOPE_EVENT_VALUES: set[IncidentOpenedEnvelopeEvent] = {
    "incident.opened",
}


def check_incident_opened_envelope_event(value: str) -> IncidentOpenedEnvelopeEvent:
    if value in INCIDENT_OPENED_ENVELOPE_EVENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_OPENED_ENVELOPE_EVENT_VALUES!r}")
