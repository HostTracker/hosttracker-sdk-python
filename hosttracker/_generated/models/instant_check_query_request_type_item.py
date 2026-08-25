from typing import Literal

InstantCheckQueryRequestTypeItem = Literal[
    "crawl", "dns", "dnsbl", "http", "ping", "port", "trace", "waterfall", "webRisk", "whois"
]

INSTANT_CHECK_QUERY_REQUEST_TYPE_ITEM_VALUES: set[InstantCheckQueryRequestTypeItem] = {
    "crawl",
    "dns",
    "dnsbl",
    "http",
    "ping",
    "port",
    "trace",
    "waterfall",
    "webRisk",
    "whois",
}


def check_instant_check_query_request_type_item(value: str) -> InstantCheckQueryRequestTypeItem:
    if value in INSTANT_CHECK_QUERY_REQUEST_TYPE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INSTANT_CHECK_QUERY_REQUEST_TYPE_ITEM_VALUES!r}")
