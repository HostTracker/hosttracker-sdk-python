from typing import Literal

MonitorUpdatedEnvelopeEvent = Literal["monitor.updated"]

MONITOR_UPDATED_ENVELOPE_EVENT_VALUES: set[MonitorUpdatedEnvelopeEvent] = {
    "monitor.updated",
}


def check_monitor_updated_envelope_event(value: str) -> MonitorUpdatedEnvelopeEvent:
    if value in MONITOR_UPDATED_ENVELOPE_EVENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_UPDATED_ENVELOPE_EVENT_VALUES!r}")
