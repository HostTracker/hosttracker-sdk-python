from typing import Literal

InstantCheckDeviceQueryRequestFieldsItem = Literal["device", "priority"]

INSTANT_CHECK_DEVICE_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[InstantCheckDeviceQueryRequestFieldsItem] = {
    "device",
    "priority",
}


def check_instant_check_device_query_request_fields_item(value: str) -> InstantCheckDeviceQueryRequestFieldsItem:
    if value in INSTANT_CHECK_DEVICE_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INSTANT_CHECK_DEVICE_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}"
    )
