from typing import Literal

ListResultStateItem = Literal["down", "up"]

LIST_RESULT_STATE_ITEM_VALUES: set[ListResultStateItem] = {
    "down",
    "up",
}


def check_list_result_state_item(value: str) -> ListResultStateItem:
    if value in LIST_RESULT_STATE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_RESULT_STATE_ITEM_VALUES!r}")
