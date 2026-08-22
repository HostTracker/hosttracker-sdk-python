from typing import Literal

MonitorCPURAMHDDSettingsDeploymentType = Literal["manual"]

MONITOR_CPURAMHDD_SETTINGS_DEPLOYMENT_TYPE_VALUES: set[MonitorCPURAMHDDSettingsDeploymentType] = {
    "manual",
}


def check_monitor_cpuramhdd_settings_deployment_type(value: str) -> MonitorCPURAMHDDSettingsDeploymentType:
    if value in MONITOR_CPURAMHDD_SETTINGS_DEPLOYMENT_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_CPURAMHDD_SETTINGS_DEPLOYMENT_TYPE_VALUES!r}"
    )
