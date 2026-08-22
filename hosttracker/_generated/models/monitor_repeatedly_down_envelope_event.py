from typing import Literal

MonitorRepeatedlyDownEnvelopeEvent = Literal["monitor.repeatedlyDown"]

MONITOR_REPEATEDLY_DOWN_ENVELOPE_EVENT_VALUES: set[MonitorRepeatedlyDownEnvelopeEvent] = {
    "monitor.repeatedlyDown",
}


def check_monitor_repeatedly_down_envelope_event(value: str) -> MonitorRepeatedlyDownEnvelopeEvent:
    if value in MONITOR_REPEATEDLY_DOWN_ENVELOPE_EVENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_REPEATEDLY_DOWN_ENVELOPE_EVENT_VALUES!r}")
