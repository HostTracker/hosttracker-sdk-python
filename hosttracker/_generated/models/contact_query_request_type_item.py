from typing import Literal

ContactQueryRequestTypeItem = Literal[
    "discord", "email", "facebook", "googleChat", "http", "skype", "sms", "telegram", "viber", "voiceCall", "webPush"
]

CONTACT_QUERY_REQUEST_TYPE_ITEM_VALUES: set[ContactQueryRequestTypeItem] = {
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


def check_contact_query_request_type_item(value: str) -> ContactQueryRequestTypeItem:
    if value in CONTACT_QUERY_REQUEST_TYPE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_QUERY_REQUEST_TYPE_ITEM_VALUES!r}")
