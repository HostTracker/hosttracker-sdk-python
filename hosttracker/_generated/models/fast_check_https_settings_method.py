from typing import Literal

FastCheckHttpsSettingsMethod = Literal["A", "D", "G", "H", "P", "U"]

FAST_CHECK_HTTPS_SETTINGS_METHOD_VALUES: set[FastCheckHttpsSettingsMethod] = {
    "A",
    "D",
    "G",
    "H",
    "P",
    "U",
}


def check_fast_check_https_settings_method(value: str) -> FastCheckHttpsSettingsMethod:
    if value in FAST_CHECK_HTTPS_SETTINGS_METHOD_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FAST_CHECK_HTTPS_SETTINGS_METHOD_VALUES!r}")
