from typing import Literal

MonitorPatchRequestType = Literal[
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

MONITOR_PATCH_REQUEST_TYPE_VALUES: set[MonitorPatchRequestType] = {
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


def check_monitor_patch_request_type(value: str) -> MonitorPatchRequestType:
    if value in MONITOR_PATCH_REQUEST_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_PATCH_REQUEST_TYPE_VALUES!r}")
