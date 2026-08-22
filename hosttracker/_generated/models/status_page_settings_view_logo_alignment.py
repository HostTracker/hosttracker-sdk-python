from typing import Literal

StatusPageSettingsViewLogoAlignment = Literal["center", "left"]

STATUS_PAGE_SETTINGS_VIEW_LOGO_ALIGNMENT_VALUES: set[StatusPageSettingsViewLogoAlignment] = {
    "center",
    "left",
}


def check_status_page_settings_view_logo_alignment(value: str) -> StatusPageSettingsViewLogoAlignment:
    if value in STATUS_PAGE_SETTINGS_VIEW_LOGO_ALIGNMENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_SETTINGS_VIEW_LOGO_ALIGNMENT_VALUES!r}")
