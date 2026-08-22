from typing import Literal

MonitorCPURAMHDDSettingsMonitorType = Literal["aspnet4", "custom", "php"]

MONITOR_CPURAMHDD_SETTINGS_MONITOR_TYPE_VALUES: set[MonitorCPURAMHDDSettingsMonitorType] = {
    "aspnet4",
    "custom",
    "php",
}


def check_monitor_cpuramhdd_settings_monitor_type(value: str) -> MonitorCPURAMHDDSettingsMonitorType:
    if value in MONITOR_CPURAMHDD_SETTINGS_MONITOR_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_CPURAMHDD_SETTINGS_MONITOR_TYPE_VALUES!r}")
