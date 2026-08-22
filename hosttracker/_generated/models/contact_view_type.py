from typing import Literal

ContactViewType = Literal[
    "discord", "email", "facebook", "googleChat", "http", "skype", "sms", "telegram", "viber", "voiceCall", "webPush"
]

CONTACT_VIEW_TYPE_VALUES: set[ContactViewType] = {
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


def check_contact_view_type(value: str) -> ContactViewType:
    if value in CONTACT_VIEW_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_VIEW_TYPE_VALUES!r}")
