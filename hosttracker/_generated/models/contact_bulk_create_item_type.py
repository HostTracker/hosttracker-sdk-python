from typing import Literal

ContactBulkCreateItemType = Literal["email", "http", "sms", "voiceCall", "webPush"]

CONTACT_BULK_CREATE_ITEM_TYPE_VALUES: set[ContactBulkCreateItemType] = {
    "email",
    "http",
    "sms",
    "voiceCall",
    "webPush",
}


def check_contact_bulk_create_item_type(value: str) -> ContactBulkCreateItemType:
    if value in CONTACT_BULK_CREATE_ITEM_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_BULK_CREATE_ITEM_TYPE_VALUES!r}")
