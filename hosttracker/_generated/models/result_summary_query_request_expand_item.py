from typing import Literal

ResultSummaryQueryRequestExpandItem = Literal[
    "count",
    "incidentCounts",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
]

RESULT_SUMMARY_QUERY_REQUEST_EXPAND_ITEM_VALUES: set[ResultSummaryQueryRequestExpandItem] = {
    "count",
    "incidentCounts",
    "monitor",
    "monitor.lastIncident",
    "monitor.maintenance",
    "monitor.settings",
    "monitor.subscription",
}


def check_result_summary_query_request_expand_item(value: str) -> ResultSummaryQueryRequestExpandItem:
    if value in RESULT_SUMMARY_QUERY_REQUEST_EXPAND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESULT_SUMMARY_QUERY_REQUEST_EXPAND_ITEM_VALUES!r}")
