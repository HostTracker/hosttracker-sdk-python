from typing import Literal

ListAlertSubscriptionContactTypeItem = Literal[
    "discord", "email", "facebook", "googleChat", "http", "skype", "sms", "telegram", "viber", "voiceCall", "webPush"
]

LIST_ALERT_SUBSCRIPTION_CONTACT_TYPE_ITEM_VALUES: set[ListAlertSubscriptionContactTypeItem] = {
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


def check_list_alert_subscription_contact_type_item(value: str) -> ListAlertSubscriptionContactTypeItem:
    if value in LIST_ALERT_SUBSCRIPTION_CONTACT_TYPE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ALERT_SUBSCRIPTION_CONTACT_TYPE_ITEM_VALUES!r}")
