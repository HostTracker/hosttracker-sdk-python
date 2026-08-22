from typing import Literal

UnknownEventTypeType = Literal["https://api2.host-tracker.com/problems/unknown-event-type"]

UNKNOWN_EVENT_TYPE_TYPE_VALUES: set[UnknownEventTypeType] = {
    "https://api2.host-tracker.com/problems/unknown-event-type",
}


def check_unknown_event_type_type(value: str) -> UnknownEventTypeType:
    if value in UNKNOWN_EVENT_TYPE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_EVENT_TYPE_TYPE_VALUES!r}")
