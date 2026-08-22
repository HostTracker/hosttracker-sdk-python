from typing import Literal

ListReportByMonitorContactTypeItem = Literal[
    "discord", "email", "facebook", "googleChat", "http", "skype", "sms", "telegram", "viber", "voiceCall", "webPush"
]

LIST_REPORT_BY_MONITOR_CONTACT_TYPE_ITEM_VALUES: set[ListReportByMonitorContactTypeItem] = {
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


def check_list_report_by_monitor_contact_type_item(value: str) -> ListReportByMonitorContactTypeItem:
    if value in LIST_REPORT_BY_MONITOR_CONTACT_TYPE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_REPORT_BY_MONITOR_CONTACT_TYPE_ITEM_VALUES!r}")
