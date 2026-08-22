from typing import Literal

TextAnalysisSettingsPreset = Literal["bl:ru"]

TEXT_ANALYSIS_SETTINGS_PRESET_VALUES: set[TextAnalysisSettingsPreset] = {
    "bl:ru",
}


def check_text_analysis_settings_preset(value: str) -> TextAnalysisSettingsPreset:
    if value in TEXT_ANALYSIS_SETTINGS_PRESET_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEXT_ANALYSIS_SETTINGS_PRESET_VALUES!r}")
