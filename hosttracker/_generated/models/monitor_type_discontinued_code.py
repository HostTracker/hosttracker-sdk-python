from typing import Literal

MonitorTypeDiscontinuedCode = Literal["monitor_type_discontinued"]

MONITOR_TYPE_DISCONTINUED_CODE_VALUES: set[MonitorTypeDiscontinuedCode] = {
    "monitor_type_discontinued",
}


def check_monitor_type_discontinued_code(value: str) -> MonitorTypeDiscontinuedCode:
    if value in MONITOR_TYPE_DISCONTINUED_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_TYPE_DISCONTINUED_CODE_VALUES!r}")
