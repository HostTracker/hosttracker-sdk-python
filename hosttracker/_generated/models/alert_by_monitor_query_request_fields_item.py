from typing import Literal

AlertByMonitorQueryRequestFieldsItem = Literal["monitor", "subscriptions"]

ALERT_BY_MONITOR_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[AlertByMonitorQueryRequestFieldsItem] = {
    "monitor",
    "subscriptions",
}


def check_alert_by_monitor_query_request_fields_item(value: str) -> AlertByMonitorQueryRequestFieldsItem:
    if value in ALERT_BY_MONITOR_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_BY_MONITOR_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}"
    )
