from typing import Literal

TextAnalysisSettingsKeywordMode = Literal["PresentAll", "PresentAny", "ReverseAll", "ReverseAny", "ReverseWithResult"]

TEXT_ANALYSIS_SETTINGS_KEYWORD_MODE_VALUES: set[TextAnalysisSettingsKeywordMode] = {
    "PresentAll",
    "PresentAny",
    "ReverseAll",
    "ReverseAny",
    "ReverseWithResult",
}


def check_text_analysis_settings_keyword_mode(value: str) -> TextAnalysisSettingsKeywordMode:
    if value in TEXT_ANALYSIS_SETTINGS_KEYWORD_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEXT_ANALYSIS_SETTINGS_KEYWORD_MODE_VALUES!r}")
