from typing import Literal

MonitorSettingsAssertRowValT = Literal["json", "xml", "yaml"]

MONITOR_SETTINGS_ASSERT_ROW_VAL_T_VALUES: set[MonitorSettingsAssertRowValT] = {
    "json",
    "xml",
    "yaml",
}


def check_monitor_settings_assert_row_val_t(value: str) -> MonitorSettingsAssertRowValT:
    if value in MONITOR_SETTINGS_ASSERT_ROW_VAL_T_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_SETTINGS_ASSERT_ROW_VAL_T_VALUES!r}")
