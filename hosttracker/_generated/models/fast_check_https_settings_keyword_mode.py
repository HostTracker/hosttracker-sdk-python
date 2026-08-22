from typing import Literal

FastCheckHttpsSettingsKeywordMode = Literal["PresentAll", "PresentAny", "ReverseAll", "ReverseAny", "ReverseWithResult"]

FAST_CHECK_HTTPS_SETTINGS_KEYWORD_MODE_VALUES: set[FastCheckHttpsSettingsKeywordMode] = {
    "PresentAll",
    "PresentAny",
    "ReverseAll",
    "ReverseAny",
    "ReverseWithResult",
}


def check_fast_check_https_settings_keyword_mode(value: str) -> FastCheckHttpsSettingsKeywordMode:
    if value in FAST_CHECK_HTTPS_SETTINGS_KEYWORD_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FAST_CHECK_HTTPS_SETTINGS_KEYWORD_MODE_VALUES!r}")
