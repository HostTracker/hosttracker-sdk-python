from typing import Literal

StatusPageSettingsViewDensity = Literal["compact", "wide"]

STATUS_PAGE_SETTINGS_VIEW_DENSITY_VALUES: set[StatusPageSettingsViewDensity] = {
    "compact",
    "wide",
}


def check_status_page_settings_view_density(value: str) -> StatusPageSettingsViewDensity:
    if value in STATUS_PAGE_SETTINGS_VIEW_DENSITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_SETTINGS_VIEW_DENSITY_VALUES!r}")
