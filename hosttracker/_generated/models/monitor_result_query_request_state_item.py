from typing import Literal

MonitorResultQueryRequestStateItem = Literal["down", "up"]

MONITOR_RESULT_QUERY_REQUEST_STATE_ITEM_VALUES: set[MonitorResultQueryRequestStateItem] = {
    "down",
    "up",
}


def check_monitor_result_query_request_state_item(value: str) -> MonitorResultQueryRequestStateItem:
    if value in MONITOR_RESULT_QUERY_REQUEST_STATE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_RESULT_QUERY_REQUEST_STATE_ITEM_VALUES!r}")
