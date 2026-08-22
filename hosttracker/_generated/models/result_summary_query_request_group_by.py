from typing import Literal

ResultSummaryQueryRequestGroupBy = Literal["account", "monitor"]

RESULT_SUMMARY_QUERY_REQUEST_GROUP_BY_VALUES: set[ResultSummaryQueryRequestGroupBy] = {
    "account",
    "monitor",
}


def check_result_summary_query_request_group_by(value: str) -> ResultSummaryQueryRequestGroupBy:
    if value in RESULT_SUMMARY_QUERY_REQUEST_GROUP_BY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESULT_SUMMARY_QUERY_REQUEST_GROUP_BY_VALUES!r}")
