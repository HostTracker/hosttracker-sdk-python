from typing import Literal

ReportByContactQueryRequestContactTypeItem = Literal[
    "discord", "email", "facebook", "googleChat", "http", "skype", "sms", "telegram", "viber", "voiceCall", "webPush"
]

REPORT_BY_CONTACT_QUERY_REQUEST_CONTACT_TYPE_ITEM_VALUES: set[ReportByContactQueryRequestContactTypeItem] = {
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


def check_report_by_contact_query_request_contact_type_item(value: str) -> ReportByContactQueryRequestContactTypeItem:
    if value in REPORT_BY_CONTACT_QUERY_REQUEST_CONTACT_TYPE_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_BY_CONTACT_QUERY_REQUEST_CONTACT_TYPE_ITEM_VALUES!r}"
    )
