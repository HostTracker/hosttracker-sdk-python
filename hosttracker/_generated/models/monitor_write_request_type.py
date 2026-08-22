from typing import Literal

MonitorWriteRequestType = Literal[
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

MONITOR_WRITE_REQUEST_TYPE_VALUES: set[MonitorWriteRequestType] = {
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


def check_monitor_write_request_type(value: str) -> MonitorWriteRequestType:
    if value in MONITOR_WRITE_REQUEST_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_WRITE_REQUEST_TYPE_VALUES!r}")
