from typing import Literal

ListReportByContactMonitorTypeItem = Literal[
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

LIST_REPORT_BY_CONTACT_MONITOR_TYPE_ITEM_VALUES: set[ListReportByContactMonitorTypeItem] = {
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


def check_list_report_by_contact_monitor_type_item(value: str) -> ListReportByContactMonitorTypeItem:
    if value in LIST_REPORT_BY_CONTACT_MONITOR_TYPE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_REPORT_BY_CONTACT_MONITOR_TYPE_ITEM_VALUES!r}")
