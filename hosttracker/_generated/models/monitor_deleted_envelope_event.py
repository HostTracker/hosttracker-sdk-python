from typing import Literal

MonitorDeletedEnvelopeEvent = Literal["monitor.deleted"]

MONITOR_DELETED_ENVELOPE_EVENT_VALUES: set[MonitorDeletedEnvelopeEvent] = {
    "monitor.deleted",
}


def check_monitor_deleted_envelope_event(value: str) -> MonitorDeletedEnvelopeEvent:
    if value in MONITOR_DELETED_ENVELOPE_EVENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_DELETED_ENVELOPE_EVENT_VALUES!r}")
