from typing import Literal

MonitorQueryRequestTypeItem = Literal[
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

MONITOR_QUERY_REQUEST_TYPE_ITEM_VALUES: set[MonitorQueryRequestTypeItem] = {
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


def check_monitor_query_request_type_item(value: str) -> MonitorQueryRequestTypeItem:
    if value in MONITOR_QUERY_REQUEST_TYPE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_QUERY_REQUEST_TYPE_ITEM_VALUES!r}")
