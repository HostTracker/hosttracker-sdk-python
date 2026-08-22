from typing import Literal

ResultSummaryQueryRequestBucket = Literal["day", "hour", "month", "none", "week"]

RESULT_SUMMARY_QUERY_REQUEST_BUCKET_VALUES: set[ResultSummaryQueryRequestBucket] = {
    "day",
    "hour",
    "month",
    "none",
    "week",
}


def check_result_summary_query_request_bucket(value: str) -> ResultSummaryQueryRequestBucket:
    if value in RESULT_SUMMARY_QUERY_REQUEST_BUCKET_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESULT_SUMMARY_QUERY_REQUEST_BUCKET_VALUES!r}")
