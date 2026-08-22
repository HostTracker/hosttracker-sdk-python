from typing import Literal

UnknownEventTypeCode = Literal["unknown_event_type"]

UNKNOWN_EVENT_TYPE_CODE_VALUES: set[UnknownEventTypeCode] = {
    "unknown_event_type",
}


def check_unknown_event_type_code(value: str) -> UnknownEventTypeCode:
    if value in UNKNOWN_EVENT_TYPE_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNKNOWN_EVENT_TYPE_CODE_VALUES!r}")
