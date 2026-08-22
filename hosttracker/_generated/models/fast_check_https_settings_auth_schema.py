from typing import Literal

FastCheckHttpsSettingsAuthSchema = Literal["Basic"]

FAST_CHECK_HTTPS_SETTINGS_AUTH_SCHEMA_VALUES: set[FastCheckHttpsSettingsAuthSchema] = {
    "Basic",
}


def check_fast_check_https_settings_auth_schema(value: str) -> FastCheckHttpsSettingsAuthSchema:
    if value in FAST_CHECK_HTTPS_SETTINGS_AUTH_SCHEMA_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FAST_CHECK_HTTPS_SETTINGS_AUTH_SCHEMA_VALUES!r}")
