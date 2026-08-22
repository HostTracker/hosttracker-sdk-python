from typing import Literal

MonitorSettingsTranStepSelectAction = Literal["select"]

MONITOR_SETTINGS_TRAN_STEP_SELECT_ACTION_VALUES: set[MonitorSettingsTranStepSelectAction] = {
    "select",
}


def check_monitor_settings_tran_step_select_action(value: str) -> MonitorSettingsTranStepSelectAction:
    if value in MONITOR_SETTINGS_TRAN_STEP_SELECT_ACTION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_SETTINGS_TRAN_STEP_SELECT_ACTION_VALUES!r}")
