from typing import Literal

UptimeSummaryViewScope = Literal["account", "selection"]

UPTIME_SUMMARY_VIEW_SCOPE_VALUES: set[UptimeSummaryViewScope] = {
    "account",
    "selection",
}


def check_uptime_summary_view_scope(value: str) -> UptimeSummaryViewScope:
    if value in UPTIME_SUMMARY_VIEW_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPTIME_SUMMARY_VIEW_SCOPE_VALUES!r}")
