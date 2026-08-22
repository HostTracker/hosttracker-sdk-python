from typing import Literal

GetResultSummaryBucket = Literal["day", "hour", "month", "none", "week"]

GET_RESULT_SUMMARY_BUCKET_VALUES: set[GetResultSummaryBucket] = {
    "day",
    "hour",
    "month",
    "none",
    "week",
}


def check_get_result_summary_bucket(value: str) -> GetResultSummaryBucket:
    if value in GET_RESULT_SUMMARY_BUCKET_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_RESULT_SUMMARY_BUCKET_VALUES!r}")
