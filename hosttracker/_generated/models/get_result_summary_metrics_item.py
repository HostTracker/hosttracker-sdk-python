from typing import Literal

GetResultSummaryMetricsItem = Literal["connect", "dns", "responseTime", "tls", "transfer", "ttfb"]

GET_RESULT_SUMMARY_METRICS_ITEM_VALUES: set[GetResultSummaryMetricsItem] = {
    "connect",
    "dns",
    "responseTime",
    "tls",
    "transfer",
    "ttfb",
}


def check_get_result_summary_metrics_item(value: str) -> GetResultSummaryMetricsItem:
    if value in GET_RESULT_SUMMARY_METRICS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_RESULT_SUMMARY_METRICS_ITEM_VALUES!r}")
