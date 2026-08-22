from typing import Literal

UnknownEventTypeStatus = Literal[422]

UNKNOWN_EVENT_TYPE_STATUS_VALUES: set[UnknownEventTypeStatus] = {
    422,
}


def check_unknown_event_type_status(value: int) -> UnknownEventTypeStatus:
    if value in UNKNOWN_EVENT_TYPE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_EVENT_TYPE_STATUS_VALUES!r}")
