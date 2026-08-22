from typing import Literal

MonitorSettingsTranSelectSubstepSelectStrategy = Literal["all", "first", "random"]

MONITOR_SETTINGS_TRAN_SELECT_SUBSTEP_SELECT_STRATEGY_VALUES: set[MonitorSettingsTranSelectSubstepSelectStrategy] = {
    "all",
    "first",
    "random",
}


def check_monitor_settings_tran_select_substep_select_strategy(
    value: str,
) -> MonitorSettingsTranSelectSubstepSelectStrategy:
    if value in MONITOR_SETTINGS_TRAN_SELECT_SUBSTEP_SELECT_STRATEGY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MONITOR_SETTINGS_TRAN_SELECT_SUBSTEP_SELECT_STRATEGY_VALUES!r}"
    )
