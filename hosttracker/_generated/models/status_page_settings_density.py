from typing import Literal

StatusPageSettingsDensity = Literal["compact", "wide"]

STATUS_PAGE_SETTINGS_DENSITY_VALUES: set[StatusPageSettingsDensity] = {
    "compact",
    "wide",
}


def check_status_page_settings_density(value: str) -> StatusPageSettingsDensity:
    if value in STATUS_PAGE_SETTINGS_DENSITY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_SETTINGS_DENSITY_VALUES!r}")
