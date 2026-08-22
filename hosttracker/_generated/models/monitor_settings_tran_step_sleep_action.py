from typing import Literal

MonitorSettingsTranStepSleepAction = Literal["sleep"]

MONITOR_SETTINGS_TRAN_STEP_SLEEP_ACTION_VALUES: set[MonitorSettingsTranStepSleepAction] = {
    "sleep",
}


def check_monitor_settings_tran_step_sleep_action(value: str) -> MonitorSettingsTranStepSleepAction:
    if value in MONITOR_SETTINGS_TRAN_STEP_SLEEP_ACTION_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_SETTINGS_TRAN_STEP_SLEEP_ACTION_VALUES!r}")
