from typing import Literal

MonitorBulkFilterTypesItem = Literal[
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

MONITOR_BULK_FILTER_TYPES_ITEM_VALUES: set[MonitorBulkFilterTypesItem] = {
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


def check_monitor_bulk_filter_types_item(value: str) -> MonitorBulkFilterTypesItem:
    if value in MONITOR_BULK_FILTER_TYPES_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_BULK_FILTER_TYPES_ITEM_VALUES!r}")
