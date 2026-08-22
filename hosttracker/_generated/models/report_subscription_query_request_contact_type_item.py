from typing import Literal

ReportSubscriptionQueryRequestContactTypeItem = Literal[
    "discord", "email", "facebook", "googleChat", "http", "skype", "sms", "telegram", "viber", "voiceCall", "webPush"
]

REPORT_SUBSCRIPTION_QUERY_REQUEST_CONTACT_TYPE_ITEM_VALUES: set[ReportSubscriptionQueryRequestContactTypeItem] = {
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


def check_report_subscription_query_request_contact_type_item(
    value: str,
) -> ReportSubscriptionQueryRequestContactTypeItem:
    if value in REPORT_SUBSCRIPTION_QUERY_REQUEST_CONTACT_TYPE_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_SUBSCRIPTION_QUERY_REQUEST_CONTACT_TYPE_ITEM_VALUES!r}"
    )
