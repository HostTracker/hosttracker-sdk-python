from typing import Literal

MonitorQueryRequestStateItem = Literal["down", "maintenance", "paused", "up"]

MONITOR_QUERY_REQUEST_STATE_ITEM_VALUES: set[MonitorQueryRequestStateItem] = {
    "down",
    "maintenance",
    "paused",
    "up",
}


def check_monitor_query_request_state_item(value: str) -> MonitorQueryRequestStateItem:
    if value in MONITOR_QUERY_REQUEST_STATE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_QUERY_REQUEST_STATE_ITEM_VALUES!r}")
