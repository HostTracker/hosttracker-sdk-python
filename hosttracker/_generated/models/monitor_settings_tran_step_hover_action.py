from typing import Literal

MonitorSettingsTranStepHoverAction = Literal["hover"]

MONITOR_SETTINGS_TRAN_STEP_HOVER_ACTION_VALUES: set[MonitorSettingsTranStepHoverAction] = {
    "hover",
}


def check_monitor_settings_tran_step_hover_action(value: str) -> MonitorSettingsTranStepHoverAction:
    if value in MONITOR_SETTINGS_TRAN_STEP_HOVER_ACTION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_SETTINGS_TRAN_STEP_HOVER_ACTION_VALUES!r}")
