from typing import Literal

StatusPageSettingsViewFeaturesItem = Literal[
    "barCharts",
    "detailsPages",
    "downtimeFeed",
    "floatingBar",
    "hidePaused",
    "monitorUrls",
    "outageDetails",
    "overallUptime",
    "subscribe",
    "uptimePercent",
]

STATUS_PAGE_SETTINGS_VIEW_FEATURES_ITEM_VALUES: set[StatusPageSettingsViewFeaturesItem] = {
    "barCharts",
    "detailsPages",
    "downtimeFeed",
    "floatingBar",
    "hidePaused",
    "monitorUrls",
    "outageDetails",
    "overallUptime",
    "subscribe",
    "uptimePercent",
}


def check_status_page_settings_view_features_item(value: str) -> StatusPageSettingsViewFeaturesItem:
    if value in STATUS_PAGE_SETTINGS_VIEW_FEATURES_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_SETTINGS_VIEW_FEATURES_ITEM_VALUES!r}")
