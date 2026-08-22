from typing import Literal

MonitorCreatedEnvelopeEvent = Literal["monitor.created"]

MONITOR_CREATED_ENVELOPE_EVENT_VALUES: set[MonitorCreatedEnvelopeEvent] = {
    "monitor.created",
}


def check_monitor_created_envelope_event(value: str) -> MonitorCreatedEnvelopeEvent:
    if value in MONITOR_CREATED_ENVELOPE_EVENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_CREATED_ENVELOPE_EVENT_VALUES!r}")
