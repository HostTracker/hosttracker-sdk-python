from typing import Literal

MaintenanceEndedEnvelopeEvent = Literal["maintenance.ended"]

MAINTENANCE_ENDED_ENVELOPE_EVENT_VALUES: set[MaintenanceEndedEnvelopeEvent] = {
    "maintenance.ended",
}


def check_maintenance_ended_envelope_event(value: str) -> MaintenanceEndedEnvelopeEvent:
    if value in MAINTENANCE_ENDED_ENVELOPE_EVENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_ENDED_ENVELOPE_EVENT_VALUES!r}")
