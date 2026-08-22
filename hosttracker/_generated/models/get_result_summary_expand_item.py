from typing import Literal

GetResultSummaryExpandItem = Literal[
    "count",
    "incidentCounts",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
]

GET_RESULT_SUMMARY_EXPAND_ITEM_VALUES: set[GetResultSummaryExpandItem] = {
    "count",
    "incidentCounts",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
}


def check_get_result_summary_expand_item(value: str) -> GetResultSummaryExpandItem:
    if value in GET_RESULT_SUMMARY_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_RESULT_SUMMARY_EXPAND_ITEM_VALUES!r}")
