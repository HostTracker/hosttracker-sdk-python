from typing import Literal

TextAnalysisSettingsAuthSchema = Literal["Basic"]

TEXT_ANALYSIS_SETTINGS_AUTH_SCHEMA_VALUES: set[TextAnalysisSettingsAuthSchema] = {
    "Basic",
}


def check_text_analysis_settings_auth_schema(value: str) -> TextAnalysisSettingsAuthSchema:
    if value in TEXT_ANALYSIS_SETTINGS_AUTH_SCHEMA_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEXT_ANALYSIS_SETTINGS_AUTH_SCHEMA_VALUES!r}")
