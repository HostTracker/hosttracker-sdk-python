from typing import Literal

AlertByContactQueryRequestContactTypeItem = Literal[
    "discord", "email", "facebook", "googleChat", "http", "skype", "sms", "telegram", "viber", "voiceCall", "webPush"
]

ALERT_BY_CONTACT_QUERY_REQUEST_CONTACT_TYPE_ITEM_VALUES: set[AlertByContactQueryRequestContactTypeItem] = {
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


def check_alert_by_contact_query_request_contact_type_item(value: str) -> AlertByContactQueryRequestContactTypeItem:
    if value in ALERT_BY_CONTACT_QUERY_REQUEST_CONTACT_TYPE_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_BY_CONTACT_QUERY_REQUEST_CONTACT_TYPE_ITEM_VALUES!r}"
    )
