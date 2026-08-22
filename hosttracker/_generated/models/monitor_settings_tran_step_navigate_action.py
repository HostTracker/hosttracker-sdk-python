from typing import Literal

MonitorSettingsTranStepNavigateAction = Literal["navigate"]

MONITOR_SETTINGS_TRAN_STEP_NAVIGATE_ACTION_VALUES: set[MonitorSettingsTranStepNavigateAction] = {
    "navigate",
}


def check_monitor_settings_tran_step_navigate_action(value: str) -> MonitorSettingsTranStepNavigateAction:
    if value in MONITOR_SETTINGS_TRAN_STEP_NAVIGATE_ACTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_SETTINGS_TRAN_STEP_NAVIGATE_ACTION_VALUES!r}"
    )
