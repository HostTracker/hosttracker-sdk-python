from typing import Literal

ListResultExpandItem = Literal[
    "count",
    "metrics",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
]

LIST_RESULT_EXPAND_ITEM_VALUES: set[ListResultExpandItem] = {
    "count",
    "metrics",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
}


def check_list_result_expand_item(value: str) -> ListResultExpandItem:
    if value in LIST_RESULT_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_RESULT_EXPAND_ITEM_VALUES!r}")
