from typing import Literal

ListInstantCheckDeviceFieldsItem = Literal["device", "priority"]

LIST_INSTANT_CHECK_DEVICE_FIELDS_ITEM_VALUES: set[ListInstantCheckDeviceFieldsItem] = {
    "device",
    "priority",
}


def check_list_instant_check_device_fields_item(value: str) -> ListInstantCheckDeviceFieldsItem:
    if value in LIST_INSTANT_CHECK_DEVICE_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INSTANT_CHECK_DEVICE_FIELDS_ITEM_VALUES!r}")
