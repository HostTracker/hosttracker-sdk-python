from typing import Literal

GetResultSummaryFieldsItem = Literal[
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

GET_RESULT_SUMMARY_FIELDS_ITEM_VALUES: set[GetResultSummaryFieldsItem] = {
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


def check_get_result_summary_fields_item(value: str) -> GetResultSummaryFieldsItem:
    if value in GET_RESULT_SUMMARY_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_RESULT_SUMMARY_FIELDS_ITEM_VALUES!r}")
