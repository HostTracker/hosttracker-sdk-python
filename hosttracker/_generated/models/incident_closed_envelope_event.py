from typing import Literal

IncidentClosedEnvelopeEvent = Literal["incident.closed"]

INCIDENT_CLOSED_ENVELOPE_EVENT_VALUES: set[IncidentClosedEnvelopeEvent] = {
    "incident.closed",
}


def check_incident_closed_envelope_event(value: str) -> IncidentClosedEnvelopeEvent:
    if value in INCIDENT_CLOSED_ENVELOPE_EVENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INCIDENT_CLOSED_ENVELOPE_EVENT_VALUES!r}")
