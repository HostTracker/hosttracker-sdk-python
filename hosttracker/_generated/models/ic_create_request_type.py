from typing import Literal

IcCreateRequestType = Literal[
    "crawl", "dns", "dnsbl", "http", "ping", "port", "rusRegBL", "trace", "waterfall", "webRisk", "whois"
]

IC_CREATE_REQUEST_TYPE_VALUES: set[IcCreateRequestType] = {
    "crawl",
    "dns",
    "dnsbl",
    "http",
    "ping",
    "port",
    "rusRegBL",
    "trace",
    "waterfall",
    "webRisk",
    "whois",
}


def check_ic_create_request_type(value: str) -> IcCreateRequestType:
    if value in IC_CREATE_REQUEST_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IC_CREATE_REQUEST_TYPE_VALUES!r}")
