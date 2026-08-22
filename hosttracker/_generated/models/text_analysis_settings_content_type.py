from typing import Literal

TextAnalysisSettingsContentType = Literal["application/json", "text/plain", "text/xml"]

TEXT_ANALYSIS_SETTINGS_CONTENT_TYPE_VALUES: set[TextAnalysisSettingsContentType] = {
    "application/json",
    "text/plain",
    "text/xml",
}


def check_text_analysis_settings_content_type(value: str) -> TextAnalysisSettingsContentType:
    if value in TEXT_ANALYSIS_SETTINGS_CONTENT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEXT_ANALYSIS_SETTINGS_CONTENT_TYPE_VALUES!r}")
