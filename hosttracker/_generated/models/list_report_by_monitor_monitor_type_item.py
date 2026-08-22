from typing import Literal

ListReportByMonitorMonitorTypeItem = Literal[
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

LIST_REPORT_BY_MONITOR_MONITOR_TYPE_ITEM_VALUES: set[ListReportByMonitorMonitorTypeItem] = {
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


def check_list_report_by_monitor_monitor_type_item(value: str) -> ListReportByMonitorMonitorTypeItem:
    if value in LIST_REPORT_BY_MONITOR_MONITOR_TYPE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_REPORT_BY_MONITOR_MONITOR_TYPE_ITEM_VALUES!r}")
