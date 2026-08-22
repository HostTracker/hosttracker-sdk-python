from typing import Literal

TextAnalysisSettingsMethod = Literal["A", "D", "G", "H", "P", "U"]

TEXT_ANALYSIS_SETTINGS_METHOD_VALUES: set[TextAnalysisSettingsMethod] = {
    "A",
    "D",
    "G",
    "H",
    "P",
    "U",
}


def check_text_analysis_settings_method(value: str) -> TextAnalysisSettingsMethod:
    if value in TEXT_ANALYSIS_SETTINGS_METHOD_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEXT_ANALYSIS_SETTINGS_METHOD_VALUES!r}")
