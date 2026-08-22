from typing import Literal

ListAlertByContactContactTypeItem = Literal[
    "discord", "email", "facebook", "googleChat", "http", "skype", "sms", "telegram", "viber", "voiceCall", "webPush"
]

LIST_ALERT_BY_CONTACT_CONTACT_TYPE_ITEM_VALUES: set[ListAlertByContactContactTypeItem] = {
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


def check_list_alert_by_contact_contact_type_item(value: str) -> ListAlertByContactContactTypeItem:
    if value in LIST_ALERT_BY_CONTACT_CONTACT_TYPE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ALERT_BY_CONTACT_CONTACT_TYPE_ITEM_VALUES!r}")
