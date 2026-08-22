from typing import Literal

ListReportByContactContactTypeItem = Literal[
    "discord", "email", "facebook", "googleChat", "http", "skype", "sms", "telegram", "viber", "voiceCall", "webPush"
]

LIST_REPORT_BY_CONTACT_CONTACT_TYPE_ITEM_VALUES: set[ListReportByContactContactTypeItem] = {
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


def check_list_report_by_contact_contact_type_item(value: str) -> ListReportByContactContactTypeItem:
    if value in LIST_REPORT_BY_CONTACT_CONTACT_TYPE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_REPORT_BY_CONTACT_CONTACT_TYPE_ITEM_VALUES!r}")
