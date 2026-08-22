from typing import Literal

ListAlertByMonitorMonitorTypeItem = Literal[
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

LIST_ALERT_BY_MONITOR_MONITOR_TYPE_ITEM_VALUES: set[ListAlertByMonitorMonitorTypeItem] = {
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


def check_list_alert_by_monitor_monitor_type_item(value: str) -> ListAlertByMonitorMonitorTypeItem:
    if value in LIST_ALERT_BY_MONITOR_MONITOR_TYPE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ALERT_BY_MONITOR_MONITOR_TYPE_ITEM_VALUES!r}")
