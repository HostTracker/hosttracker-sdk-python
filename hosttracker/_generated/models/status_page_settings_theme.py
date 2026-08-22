from typing import Literal

StatusPageSettingsTheme = Literal["dark", "light"]

STATUS_PAGE_SETTINGS_THEME_VALUES: set[StatusPageSettingsTheme] = {
    "dark",
    "light",
}


def check_status_page_settings_theme(value: str) -> StatusPageSettingsTheme:
    if value in STATUS_PAGE_SETTINGS_THEME_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_SETTINGS_THEME_VALUES!r}")
