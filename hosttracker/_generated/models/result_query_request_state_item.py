from typing import Literal

ResultQueryRequestStateItem = Literal["down", "up"]

RESULT_QUERY_REQUEST_STATE_ITEM_VALUES: set[ResultQueryRequestStateItem] = {
    "down",
    "up",
}


def check_result_query_request_state_item(value: str) -> ResultQueryRequestStateItem:
    if value in RESULT_QUERY_REQUEST_STATE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESULT_QUERY_REQUEST_STATE_ITEM_VALUES!r}")
