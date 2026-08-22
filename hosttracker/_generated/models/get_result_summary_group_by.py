from typing import Literal

GetResultSummaryGroupBy = Literal["account", "monitor"]

GET_RESULT_SUMMARY_GROUP_BY_VALUES: set[GetResultSummaryGroupBy] = {
    "account",
    "monitor",
}


def check_get_result_summary_group_by(value: str) -> GetResultSummaryGroupBy:
    if value in GET_RESULT_SUMMARY_GROUP_BY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_RESULT_SUMMARY_GROUP_BY_VALUES!r}")
