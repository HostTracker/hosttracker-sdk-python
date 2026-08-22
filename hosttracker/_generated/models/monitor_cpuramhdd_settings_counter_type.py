from typing import Literal

MonitorCPURAMHDDSettingsCounterType = Literal["cpu", "disk", "mssql", "mysql", "perfCounter", "port", "ram"]

MONITOR_CPURAMHDD_SETTINGS_COUNTER_TYPE_VALUES: set[MonitorCPURAMHDDSettingsCounterType] = {
    "cpu",
    "disk",
    "mssql",
    "mysql",
    "perfCounter",
    "port",
    "ram",
}


def check_monitor_cpuramhdd_settings_counter_type(value: str) -> MonitorCPURAMHDDSettingsCounterType:
    if value in MONITOR_CPURAMHDD_SETTINGS_COUNTER_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_CPURAMHDD_SETTINGS_COUNTER_TYPE_VALUES!r}")
