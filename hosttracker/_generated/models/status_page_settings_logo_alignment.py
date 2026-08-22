from typing import Literal

StatusPageSettingsLogoAlignment = Literal["center", "left"]

STATUS_PAGE_SETTINGS_LOGO_ALIGNMENT_VALUES: set[StatusPageSettingsLogoAlignment] = {
    "center",
    "left",
}


def check_status_page_settings_logo_alignment(value: str) -> StatusPageSettingsLogoAlignment:
    if value in STATUS_PAGE_SETTINGS_LOGO_ALIGNMENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_SETTINGS_LOGO_ALIGNMENT_VALUES!r}")
