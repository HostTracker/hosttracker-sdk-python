from typing import Literal

MonitorItemVerdictViewOverlimit = Literal["fits", "wouldDisable", "wouldFail"]

MONITOR_ITEM_VERDICT_VIEW_OVERLIMIT_VALUES: set[MonitorItemVerdictViewOverlimit] = {
    "fits",
    "wouldDisable",
    "wouldFail",
}


def check_monitor_item_verdict_view_overlimit(value: str) -> MonitorItemVerdictViewOverlimit:
    if value in MONITOR_ITEM_VERDICT_VIEW_OVERLIMIT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_ITEM_VERDICT_VIEW_OVERLIMIT_VALUES!r}")
