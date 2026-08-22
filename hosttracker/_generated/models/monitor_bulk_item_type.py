from typing import Literal

MonitorBulkItemType = Literal[
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

MONITOR_BULK_ITEM_TYPE_VALUES: set[MonitorBulkItemType] = {
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


def check_monitor_bulk_item_type(value: str) -> MonitorBulkItemType:
    if value in MONITOR_BULK_ITEM_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_BULK_ITEM_TYPE_VALUES!r}")
