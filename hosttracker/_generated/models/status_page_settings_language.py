from typing import Literal

StatusPageSettingsLanguage = Literal["cs", "de", "en", "es", "fr", "it", "ja", "nl", "pl", "pt", "ru", "tr", "ua", "zh"]

STATUS_PAGE_SETTINGS_LANGUAGE_VALUES: set[StatusPageSettingsLanguage] = {
    "cs",
    "de",
    "en",
    "es",
    "fr",
    "it",
    "ja",
    "nl",
    "pl",
    "pt",
    "ru",
    "tr",
    "ua",
    "zh",
}


def check_status_page_settings_language(value: str) -> StatusPageSettingsLanguage:
    if value in STATUS_PAGE_SETTINGS_LANGUAGE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_SETTINGS_LANGUAGE_VALUES!r}")
