from typing import Literal

MonitorSettingsTranStepSelectSelectStrategy = Literal["all", "first", "random"]

MONITOR_SETTINGS_TRAN_STEP_SELECT_SELECT_STRATEGY_VALUES: set[MonitorSettingsTranStepSelectSelectStrategy] = {
    "all",
    "first",
    "random",
}


def check_monitor_settings_tran_step_select_select_strategy(value: str) -> MonitorSettingsTranStepSelectSelectStrategy:
    if value in MONITOR_SETTINGS_TRAN_STEP_SELECT_SELECT_STRATEGY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_SETTINGS_TRAN_STEP_SELECT_SELECT_STRATEGY_VALUES!r}"
    )
