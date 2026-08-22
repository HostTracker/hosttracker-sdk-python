from typing import Literal

ContactBulkUpdateItemType = Literal["email", "http", "sms", "voiceCall", "webPush"]

CONTACT_BULK_UPDATE_ITEM_TYPE_VALUES: set[ContactBulkUpdateItemType] = {
    "email",
    "http",
    "sms",
    "voiceCall",
    "webPush",
}


def check_contact_bulk_update_item_type(value: str) -> ContactBulkUpdateItemType:
    if value in CONTACT_BULK_UPDATE_ITEM_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_BULK_UPDATE_ITEM_TYPE_VALUES!r}")
