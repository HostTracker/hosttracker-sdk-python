from typing import Literal

MonitorSettingsTranStepCheckContentAction = Literal["checkContent"]

MONITOR_SETTINGS_TRAN_STEP_CHECK_CONTENT_ACTION_VALUES: set[MonitorSettingsTranStepCheckContentAction] = {
    "checkContent",
}


def check_monitor_settings_tran_step_check_content_action(value: str) -> MonitorSettingsTranStepCheckContentAction:
    if value in MONITOR_SETTINGS_TRAN_STEP_CHECK_CONTENT_ACTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_SETTINGS_TRAN_STEP_CHECK_CONTENT_ACTION_VALUES!r}"
    )
