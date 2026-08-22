from typing import Literal

AlertSubscriptionQueryRequestMonitorTypeItem = Literal[
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

ALERT_SUBSCRIPTION_QUERY_REQUEST_MONITOR_TYPE_ITEM_VALUES: set[AlertSubscriptionQueryRequestMonitorTypeItem] = {
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


def check_alert_subscription_query_request_monitor_type_item(
    value: str,
) -> AlertSubscriptionQueryRequestMonitorTypeItem:
    if value in ALERT_SUBSCRIPTION_QUERY_REQUEST_MONITOR_TYPE_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_SUBSCRIPTION_QUERY_REQUEST_MONITOR_TYPE_ITEM_VALUES!r}"
    )
