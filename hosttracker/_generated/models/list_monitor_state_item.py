from typing import Literal

ListMonitorStateItem = Literal["down", "maintenance", "paused", "up"]

LIST_MONITOR_STATE_ITEM_VALUES: set[ListMonitorStateItem] = {
    "down",
    "maintenance",
    "paused",
    "up",
}


def check_list_monitor_state_item(value: str) -> ListMonitorStateItem:
    if value in LIST_MONITOR_STATE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MONITOR_STATE_ITEM_VALUES!r}")
