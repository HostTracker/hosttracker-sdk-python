from typing import Literal

MonitorSettingsAssertRowOp = Literal[
    "contains",
    "containsAll",
    "containsAny",
    "endsWith",
    "eq",
    "exists",
    "ge",
    "gt",
    "in",
    "isNumber",
    "le",
    "lt",
    "matches",
    "startsWith",
    "unique",
]

MONITOR_SETTINGS_ASSERT_ROW_OP_VALUES: set[MonitorSettingsAssertRowOp] = {
    "contains",
    "containsAll",
    "containsAny",
    "endsWith",
    "eq",
    "exists",
    "ge",
    "gt",
    "in",
    "isNumber",
    "le",
    "lt",
    "matches",
    "startsWith",
    "unique",
}


def check_monitor_settings_assert_row_op(value: str) -> MonitorSettingsAssertRowOp:
    if value in MONITOR_SETTINGS_ASSERT_ROW_OP_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_SETTINGS_ASSERT_ROW_OP_VALUES!r}")
