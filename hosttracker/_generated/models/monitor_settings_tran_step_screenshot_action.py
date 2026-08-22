from typing import Literal

MonitorSettingsTranStepScreenshotAction = Literal["screenshot"]

MONITOR_SETTINGS_TRAN_STEP_SCREENSHOT_ACTION_VALUES: set[MonitorSettingsTranStepScreenshotAction] = {
    "screenshot",
}


def check_monitor_settings_tran_step_screenshot_action(value: str) -> MonitorSettingsTranStepScreenshotAction:
    if value in MONITOR_SETTINGS_TRAN_STEP_SCREENSHOT_ACTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_SETTINGS_TRAN_STEP_SCREENSHOT_ACTION_VALUES!r}"
    )
