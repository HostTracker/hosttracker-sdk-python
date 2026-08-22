from typing import Literal

AlertDetailViewKind = Literal["alert", "info"]

ALERT_DETAIL_VIEW_KIND_VALUES: set[AlertDetailViewKind] = {
    "alert",
    "info",
}


def check_alert_detail_view_kind(value: str) -> AlertDetailViewKind:
    if value in ALERT_DETAIL_VIEW_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALERT_DETAIL_VIEW_KIND_VALUES!r}")
