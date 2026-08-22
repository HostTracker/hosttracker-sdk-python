from typing import Literal

ReportSubscriptionQueryRequestMonitorTypeItem = Literal[
    "api",
    "cntCheck",
    "counter",
    "database",
    "dnsbl",
    "domainExp",
    "http",
    "ping",
    "port",
    "snmp",
    "sslExp",
    "tran",
    "waterfall",
    "webRisk",
]

REPORT_SUBSCRIPTION_QUERY_REQUEST_MONITOR_TYPE_ITEM_VALUES: set[ReportSubscriptionQueryRequestMonitorTypeItem] = {
    "api",
    "cntCheck",
    "counter",
    "database",
    "dnsbl",
    "domainExp",
    "http",
    "ping",
    "port",
    "snmp",
    "sslExp",
    "tran",
    "waterfall",
    "webRisk",
}


def check_report_subscription_query_request_monitor_type_item(
    value: str,
) -> ReportSubscriptionQueryRequestMonitorTypeItem:
    if value in REPORT_SUBSCRIPTION_QUERY_REQUEST_MONITOR_TYPE_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_SUBSCRIPTION_QUERY_REQUEST_MONITOR_TYPE_ITEM_VALUES!r}"
    )
