from typing import Literal

MonitorSettingsTranStepSelectValidationStrategy = Literal["one", "oneOrMore", "zero", "zeroOrMore"]

MONITOR_SETTINGS_TRAN_STEP_SELECT_VALIDATION_STRATEGY_VALUES: set[MonitorSettingsTranStepSelectValidationStrategy] = {
    "one",
    "oneOrMore",
    "zero",
    "zeroOrMore",
}


def check_monitor_settings_tran_step_select_validation_strategy(
    value: str,
) -> MonitorSettingsTranStepSelectValidationStrategy:
    if value in MONITOR_SETTINGS_TRAN_STEP_SELECT_VALIDATION_STRATEGY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_SETTINGS_TRAN_STEP_SELECT_VALIDATION_STRATEGY_VALUES!r}"
    )
