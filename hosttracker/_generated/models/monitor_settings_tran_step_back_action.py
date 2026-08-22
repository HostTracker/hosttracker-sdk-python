from typing import Literal

MonitorSettingsTranStepBackAction = Literal["back"]

MONITOR_SETTINGS_TRAN_STEP_BACK_ACTION_VALUES: set[MonitorSettingsTranStepBackAction] = {
    "back",
}


def check_monitor_settings_tran_step_back_action(value: str) -> MonitorSettingsTranStepBackAction:
    if value in MONITOR_SETTINGS_TRAN_STEP_BACK_ACTION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_SETTINGS_TRAN_STEP_BACK_ACTION_VALUES!r}")
