from typing import Literal

GetMonitorAttachedFieldsItem = Literal["dnsbl", "domainExp", "sslExp", "webRisk"]

GET_MONITOR_ATTACHED_FIELDS_ITEM_VALUES: set[GetMonitorAttachedFieldsItem] = {
    "dnsbl",
    "domainExp",
    "sslExp",
    "webRisk",
}


def check_get_monitor_attached_fields_item(value: str) -> GetMonitorAttachedFieldsItem:
    if value in GET_MONITOR_ATTACHED_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_MONITOR_ATTACHED_FIELDS_ITEM_VALUES!r}")
