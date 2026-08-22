from typing import Literal

DatabaseCheckSettingsMode = Literal["NonQuery", "Scalar"]

DATABASE_CHECK_SETTINGS_MODE_VALUES: set[DatabaseCheckSettingsMode] = {
    "NonQuery",
    "Scalar",
}


def check_database_check_settings_mode(value: str) -> DatabaseCheckSettingsMode:
    if value in DATABASE_CHECK_SETTINGS_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATABASE_CHECK_SETTINGS_MODE_VALUES!r}")
