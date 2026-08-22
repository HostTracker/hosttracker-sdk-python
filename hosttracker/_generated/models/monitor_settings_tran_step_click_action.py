from typing import Literal

MonitorSettingsTranStepClickAction = Literal["click"]

MONITOR_SETTINGS_TRAN_STEP_CLICK_ACTION_VALUES: set[MonitorSettingsTranStepClickAction] = {
    "click",
}


def check_monitor_settings_tran_step_click_action(value: str) -> MonitorSettingsTranStepClickAction:
    if value in MONITOR_SETTINGS_TRAN_STEP_CLICK_ACTION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_SETTINGS_TRAN_STEP_CLICK_ACTION_VALUES!r}")
