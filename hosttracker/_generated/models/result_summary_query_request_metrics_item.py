from typing import Literal

ResultSummaryQueryRequestMetricsItem = Literal["connect", "dns", "responseTime", "tls", "transfer", "ttfb"]

RESULT_SUMMARY_QUERY_REQUEST_METRICS_ITEM_VALUES: set[ResultSummaryQueryRequestMetricsItem] = {
    "connect",
    "dns",
    "responseTime",
    "tls",
    "transfer",
    "ttfb",
}


def check_result_summary_query_request_metrics_item(value: str) -> ResultSummaryQueryRequestMetricsItem:
    if value in RESULT_SUMMARY_QUERY_REQUEST_METRICS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESULT_SUMMARY_QUERY_REQUEST_METRICS_ITEM_VALUES!r}")
