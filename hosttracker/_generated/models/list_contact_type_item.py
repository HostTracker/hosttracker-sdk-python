from typing import Literal

ListContactTypeItem = Literal[
    "discord", "email", "facebook", "googleChat", "http", "skype", "sms", "telegram", "viber", "voiceCall", "webPush"
]

LIST_CONTACT_TYPE_ITEM_VALUES: set[ListContactTypeItem] = {
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


def check_list_contact_type_item(value: str) -> ListContactTypeItem:
    if value in LIST_CONTACT_TYPE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CONTACT_TYPE_ITEM_VALUES!r}")
