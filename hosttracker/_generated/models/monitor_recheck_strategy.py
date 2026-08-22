from typing import Literal

MonitorRecheckStrategy = Literal["downFullAgreement", "fullAgreement", "minNumDown", "noRecheck"]

MONITOR_RECHECK_STRATEGY_VALUES: set[MonitorRecheckStrategy] = {
    "downFullAgreement",
    "fullAgreement",
    "minNumDown",
    "noRecheck",
}


def check_monitor_recheck_strategy(value: str) -> MonitorRecheckStrategy:
    if value in MONITOR_RECHECK_STRATEGY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_RECHECK_STRATEGY_VALUES!r}")
