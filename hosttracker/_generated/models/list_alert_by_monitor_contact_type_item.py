from typing import Literal

ListAlertByMonitorContactTypeItem = Literal[
    "discord", "email", "facebook", "googleChat", "http", "skype", "sms", "telegram", "viber", "voiceCall", "webPush"
]

LIST_ALERT_BY_MONITOR_CONTACT_TYPE_ITEM_VALUES: set[ListAlertByMonitorContactTypeItem] = {
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


def check_list_alert_by_monitor_contact_type_item(value: str) -> ListAlertByMonitorContactTypeItem:
    if value in LIST_ALERT_BY_MONITOR_CONTACT_TYPE_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ALERT_BY_MONITOR_CONTACT_TYPE_ITEM_VALUES!r}")
