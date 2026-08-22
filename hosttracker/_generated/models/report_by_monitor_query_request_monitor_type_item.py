from typing import Literal

ReportByMonitorQueryRequestMonitorTypeItem = Literal[
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

REPORT_BY_MONITOR_QUERY_REQUEST_MONITOR_TYPE_ITEM_VALUES: set[ReportByMonitorQueryRequestMonitorTypeItem] = {
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


def check_report_by_monitor_query_request_monitor_type_item(value: str) -> ReportByMonitorQueryRequestMonitorTypeItem:
    if value in REPORT_BY_MONITOR_QUERY_REQUEST_MONITOR_TYPE_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_BY_MONITOR_QUERY_REQUEST_MONITOR_TYPE_ITEM_VALUES!r}"
    )
