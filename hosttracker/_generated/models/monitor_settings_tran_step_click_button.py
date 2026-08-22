from typing import Literal

MonitorSettingsTranStepClickButton = Literal["left", "middle", "right"]

MONITOR_SETTINGS_TRAN_STEP_CLICK_BUTTON_VALUES: set[MonitorSettingsTranStepClickButton] = {
    "left",
    "middle",
    "right",
}


def check_monitor_settings_tran_step_click_button(value: str) -> MonitorSettingsTranStepClickButton:
    if value in MONITOR_SETTINGS_TRAN_STEP_CLICK_BUTTON_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_SETTINGS_TRAN_STEP_CLICK_BUTTON_VALUES!r}")
