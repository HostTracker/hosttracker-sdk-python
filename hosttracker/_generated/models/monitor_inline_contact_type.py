from typing import Literal

MonitorInlineContactType = Literal["email", "http", "sms", "voiceCall"]

MONITOR_INLINE_CONTACT_TYPE_VALUES: set[MonitorInlineContactType] = {
    "email",
    "http",
    "sms",
    "voiceCall",
}


def check_monitor_inline_contact_type(value: str) -> MonitorInlineContactType:
    if value in MONITOR_INLINE_CONTACT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_INLINE_CONTACT_TYPE_VALUES!r}")
