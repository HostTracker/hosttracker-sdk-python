from typing import Literal

ResultSummaryQueryRequestFieldsItem = Literal[
    "checks",
    "downSec",
    "downSpans",
    "errorBudgetSecRemaining",
    "from",
    "incidents",
    "maintenance",
    "metrics",
    "monitor",
    "monitorId",
    "monitors",
    "sampled",
    "scope",
    "slaMet",
    "slaTarget",
    "to",
    "totalSec",
    "upSec",
    "uptimePercent",
]

RESULT_SUMMARY_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[ResultSummaryQueryRequestFieldsItem] = {
    "checks",
    "downSec",
    "downSpans",
    "errorBudgetSecRemaining",
    "from",
    "incidents",
    "maintenance",
    "metrics",
    "monitor",
    "monitorId",
    "monitors",
    "sampled",
    "scope",
    "slaMet",
    "slaTarget",
    "to",
    "totalSec",
    "upSec",
    "uptimePercent",
}


def check_result_summary_query_request_fields_item(value: str) -> ResultSummaryQueryRequestFieldsItem:
    if value in RESULT_SUMMARY_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESULT_SUMMARY_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
