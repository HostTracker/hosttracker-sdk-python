from typing import Literal

DatabaseCheckSettingsComparisonMode = Literal[
    "Equal", "GreaterThan", "InInterval", "LessThan", "No", "NotEqual", "OutInterval"
]

DATABASE_CHECK_SETTINGS_COMPARISON_MODE_VALUES: set[DatabaseCheckSettingsComparisonMode] = {
    "Equal",
    "GreaterThan",
    "InInterval",
    "LessThan",
    "No",
    "NotEqual",
    "OutInterval",
}


def check_database_check_settings_comparison_mode(value: str) -> DatabaseCheckSettingsComparisonMode:
    if value in DATABASE_CHECK_SETTINGS_COMPARISON_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATABASE_CHECK_SETTINGS_COMPARISON_MODE_VALUES!r}")
