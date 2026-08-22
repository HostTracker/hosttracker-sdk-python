from typing import Literal

ContactBulkFilterTypesItem = Literal[
    "discord", "email", "facebook", "googleChat", "http", "skype", "sms", "telegram", "viber", "voiceCall", "webPush"
]

CONTACT_BULK_FILTER_TYPES_ITEM_VALUES: set[ContactBulkFilterTypesItem] = {
    "discord",
    "email",
    "facebook",
    "googleChat",
    "http",
    "skype",
    "sms",
    "telegram",
    "viber",
    "voiceCall",
    "webPush",
}


def check_contact_bulk_filter_types_item(value: str) -> ContactBulkFilterTypesItem:
    if value in CONTACT_BULK_FILTER_TYPES_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_BULK_FILTER_TYPES_ITEM_VALUES!r}")
