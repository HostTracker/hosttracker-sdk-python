from typing import Literal

IcCreateRequestDnsQueryItem = Literal["A", "AAAA", "CNAME", "MX", "TXT"]

IC_CREATE_REQUEST_DNS_QUERY_ITEM_VALUES: set[IcCreateRequestDnsQueryItem] = {
    "A",
    "AAAA",
    "CNAME",
    "MX",
    "TXT",
}


def check_ic_create_request_dns_query_item(value: str) -> IcCreateRequestDnsQueryItem:
    if value in IC_CREATE_REQUEST_DNS_QUERY_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IC_CREATE_REQUEST_DNS_QUERY_ITEM_VALUES!r}")
