from typing import Literal

ListMonitorResultStateItem = Literal["down", "up"]

LIST_MONITOR_RESULT_STATE_ITEM_VALUES: set[ListMonitorResultStateItem] = {
    "down",
    "up",
}


def check_list_monitor_result_state_item(value: str) -> ListMonitorResultStateItem:
    if value in LIST_MONITOR_RESULT_STATE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MONITOR_RESULT_STATE_ITEM_VALUES!r}")
