from typing import Literal

MonitorUpEnvelopeEvent = Literal["monitor.up"]

MONITOR_UP_ENVELOPE_EVENT_VALUES: set[MonitorUpEnvelopeEvent] = {
    "monitor.up",
}


def check_monitor_up_envelope_event(value: str) -> MonitorUpEnvelopeEvent:
    if value in MONITOR_UP_ENVELOPE_EVENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_UP_ENVELOPE_EVENT_VALUES!r}")
