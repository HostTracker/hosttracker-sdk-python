from typing import Literal

InvalidSettingsStatus = Literal[422]

INVALID_SETTINGS_STATUS_VALUES: set[InvalidSettingsStatus] = {
    422,
}


def check_invalid_settings_status(value: int) -> InvalidSettingsStatus:
    if value in INVALID_SETTINGS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_SETTINGS_STATUS_VALUES!r}")
