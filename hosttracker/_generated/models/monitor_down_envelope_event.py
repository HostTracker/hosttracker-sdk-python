from typing import Literal

MonitorDownEnvelopeEvent = Literal["monitor.down"]

MONITOR_DOWN_ENVELOPE_EVENT_VALUES: set[MonitorDownEnvelopeEvent] = {
    "monitor.down",
}


def check_monitor_down_envelope_event(value: str) -> MonitorDownEnvelopeEvent:
    if value in MONITOR_DOWN_ENVELOPE_EVENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_DOWN_ENVELOPE_EVENT_VALUES!r}")
