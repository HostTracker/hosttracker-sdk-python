from typing import Literal

InvalidSettingsCode = Literal["invalid_settings"]

INVALID_SETTINGS_CODE_VALUES: set[InvalidSettingsCode] = {
    "invalid_settings",
}


def check_invalid_settings_code(value: str) -> InvalidSettingsCode:
    if value in INVALID_SETTINGS_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVALID_SETTINGS_CODE_VALUES!r}")
