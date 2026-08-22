from typing import Literal

ResultQueryRequestSort = Literal["monitor", "monitor:asc", "monitor:desc", "time", "time:desc"]

RESULT_QUERY_REQUEST_SORT_VALUES: set[ResultQueryRequestSort] = {
    "monitor",
    "monitor:asc",
    "monitor:desc",
    "time",
    "time:desc",
}


def check_result_query_request_sort(value: str) -> ResultQueryRequestSort:
    if value in RESULT_QUERY_REQUEST_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESULT_QUERY_REQUEST_SORT_VALUES!r}")
