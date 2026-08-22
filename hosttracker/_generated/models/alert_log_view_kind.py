from typing import Literal

AlertLogViewKind = Literal["alert", "info"]

ALERT_LOG_VIEW_KIND_VALUES: set[AlertLogViewKind] = {
    "alert",
    "info",
}


def check_alert_log_view_kind(value: str) -> AlertLogViewKind:
    if value in ALERT_LOG_VIEW_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_LOG_VIEW_KIND_VALUES!r}")
