from typing import Literal

ListReportSubscriptionContactTypeItem = Literal[
    "discord", "email", "facebook", "googleChat", "http", "skype", "sms", "telegram", "viber", "voiceCall", "webPush"
]

LIST_REPORT_SUBSCRIPTION_CONTACT_TYPE_ITEM_VALUES: set[ListReportSubscriptionContactTypeItem] = {
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


def check_list_report_subscription_contact_type_item(value: str) -> ListReportSubscriptionContactTypeItem:
    if value in LIST_REPORT_SUBSCRIPTION_CONTACT_TYPE_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_REPORT_SUBSCRIPTION_CONTACT_TYPE_ITEM_VALUES!r}"
    )
