from typing import Literal

AlertByMonitorQueryRequestMonitorTypeItem = Literal[
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

ALERT_BY_MONITOR_QUERY_REQUEST_MONITOR_TYPE_ITEM_VALUES: set[AlertByMonitorQueryRequestMonitorTypeItem] = {
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


def check_alert_by_monitor_query_request_monitor_type_item(value: str) -> AlertByMonitorQueryRequestMonitorTypeItem:
    if value in ALERT_BY_MONITOR_QUERY_REQUEST_MONITOR_TYPE_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_BY_MONITOR_QUERY_REQUEST_MONITOR_TYPE_ITEM_VALUES!r}"
    )
