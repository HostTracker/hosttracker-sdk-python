from typing import Literal

ListReportSubscriptionMonitorTypeItem = Literal[
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

LIST_REPORT_SUBSCRIPTION_MONITOR_TYPE_ITEM_VALUES: set[ListReportSubscriptionMonitorTypeItem] = {
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


def check_list_report_subscription_monitor_type_item(value: str) -> ListReportSubscriptionMonitorTypeItem:
    if value in LIST_REPORT_SUBSCRIPTION_MONITOR_TYPE_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_REPORT_SUBSCRIPTION_MONITOR_TYPE_ITEM_VALUES!r}"
    )
