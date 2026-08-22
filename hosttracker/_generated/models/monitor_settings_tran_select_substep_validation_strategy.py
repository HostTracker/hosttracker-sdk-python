from typing import Literal

MonitorSettingsTranSelectSubstepValidationStrategy = Literal["one", "oneOrMore", "zero", "zeroOrMore"]

MONITOR_SETTINGS_TRAN_SELECT_SUBSTEP_VALIDATION_STRATEGY_VALUES: set[
    MonitorSettingsTranSelectSubstepValidationStrategy
] = {
    "one",
    "oneOrMore",
    "zero",
    "zeroOrMore",
}


def check_monitor_settings_tran_select_substep_validation_strategy(
    value: str,
) -> MonitorSettingsTranSelectSubstepValidationStrategy:
    if value in MONITOR_SETTINGS_TRAN_SELECT_SUBSTEP_VALIDATION_STRATEGY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_SETTINGS_TRAN_SELECT_SUBSTEP_VALIDATION_STRATEGY_VALUES!r}"
    )
