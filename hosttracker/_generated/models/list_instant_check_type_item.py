from typing import Literal

ListInstantCheckTypeItem = Literal[
    "crawl", "dns", "dnsbl", "http", "ping", "port", "rusRegBL", "trace", "waterfall", "webRisk", "whois"
]

LIST_INSTANT_CHECK_TYPE_ITEM_VALUES: set[ListInstantCheckTypeItem] = {
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


def check_list_instant_check_type_item(value: str) -> ListInstantCheckTypeItem:
    if value in LIST_INSTANT_CHECK_TYPE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INSTANT_CHECK_TYPE_ITEM_VALUES!r}")
