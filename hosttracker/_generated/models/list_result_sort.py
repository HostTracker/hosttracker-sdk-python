from typing import Literal

ListResultSort = Literal["monitor", "monitor:asc", "monitor:desc", "time", "time:desc"]

LIST_RESULT_SORT_VALUES: set[ListResultSort] = {
    "monitor",
    "monitor:asc",
    "monitor:desc",
    "time",
    "time:desc",
}


def check_list_result_sort(value: str) -> ListResultSort:
    if value in LIST_RESULT_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_RESULT_SORT_VALUES!r}")
