from typing import Literal

ListAlertSubscriptionMonitorTypeItem = Literal[
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

LIST_ALERT_SUBSCRIPTION_MONITOR_TYPE_ITEM_VALUES: set[ListAlertSubscriptionMonitorTypeItem] = {
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


def check_list_alert_subscription_monitor_type_item(value: str) -> ListAlertSubscriptionMonitorTypeItem:
    if value in LIST_ALERT_SUBSCRIPTION_MONITOR_TYPE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ALERT_SUBSCRIPTION_MONITOR_TYPE_ITEM_VALUES!r}")
