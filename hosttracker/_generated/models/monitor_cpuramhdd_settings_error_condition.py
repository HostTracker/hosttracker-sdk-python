from typing import Literal

MonitorCPURAMHDDSettingsErrorCondition = Literal[
    "eq", "ge", "gt", "in", "ine", "ine1", "ine2", "le", "ls", "ne", "no", "out", "oute", "oute1", "oute2"
]

MONITOR_CPURAMHDD_SETTINGS_ERROR_CONDITION_VALUES: set[MonitorCPURAMHDDSettingsErrorCondition] = {
    "eq",
    "ge",
    "gt",
    "in",
    "ine",
    "ine1",
    "ine2",
    "le",
    "ls",
    "ne",
    "no",
    "out",
    "oute",
    "oute1",
    "oute2",
}


def check_monitor_cpuramhdd_settings_error_condition(value: str) -> MonitorCPURAMHDDSettingsErrorCondition:
    if value in MONITOR_CPURAMHDD_SETTINGS_ERROR_CONDITION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_CPURAMHDD_SETTINGS_ERROR_CONDITION_VALUES!r}"
    )
