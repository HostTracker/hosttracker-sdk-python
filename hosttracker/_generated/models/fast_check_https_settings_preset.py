from typing import Literal

FastCheckHttpsSettingsPreset = Literal["bl:ru"]

FAST_CHECK_HTTPS_SETTINGS_PRESET_VALUES: set[FastCheckHttpsSettingsPreset] = {
    "bl:ru",
}


def check_fast_check_https_settings_preset(value: str) -> FastCheckHttpsSettingsPreset:
    if value in FAST_CHECK_HTTPS_SETTINGS_PRESET_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FAST_CHECK_HTTPS_SETTINGS_PRESET_VALUES!r}")
