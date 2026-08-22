from typing import Literal

MonitorSettingsApiExpectationFunc = Literal[
    "eq", "ge", "gt", "in", "inr", "le", "ls", "neq", "no", "null", "out", "outr"
]

MONITOR_SETTINGS_API_EXPECTATION_FUNC_VALUES: set[MonitorSettingsApiExpectationFunc] = {
    "eq",
    "ge",
    "gt",
    "in",
    "inr",
    "le",
    "ls",
    "neq",
    "no",
    "null",
    "out",
    "outr",
}


def check_monitor_settings_api_expectation_func(value: str) -> MonitorSettingsApiExpectationFunc:
    if value in MONITOR_SETTINGS_API_EXPECTATION_FUNC_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_SETTINGS_API_EXPECTATION_FUNC_VALUES!r}")
