from typing import Literal

ResultQueryRequestExpandItem = Literal[
    "count",
    "metrics",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
]

RESULT_QUERY_REQUEST_EXPAND_ITEM_VALUES: set[ResultQueryRequestExpandItem] = {
    "count",
    "metrics",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
    "recheck",
}


def check_result_query_request_expand_item(value: str) -> ResultQueryRequestExpandItem:
    if value in RESULT_QUERY_REQUEST_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESULT_QUERY_REQUEST_EXPAND_ITEM_VALUES!r}")
