from typing import Literal

MonitorSettingsTranStepTypeAction = Literal["type"]

MONITOR_SETTINGS_TRAN_STEP_TYPE_ACTION_VALUES: set[MonitorSettingsTranStepTypeAction] = {
    "type",
}


def check_monitor_settings_tran_step_type_action(value: str) -> MonitorSettingsTranStepTypeAction:
    if value in MONITOR_SETTINGS_TRAN_STEP_TYPE_ACTION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_SETTINGS_TRAN_STEP_TYPE_ACTION_VALUES!r}")
