from typing import Literal

InvalidSettingsType = Literal["https://api2.host-tracker.com/problems/invalid-settings"]

INVALID_SETTINGS_TYPE_VALUES: set[InvalidSettingsType] = {
    "https://api2.host-tracker.com/problems/invalid-settings",
}


def check_invalid_settings_type(value: str) -> InvalidSettingsType:
    if value in INVALID_SETTINGS_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_SETTINGS_TYPE_VALUES!r}")
