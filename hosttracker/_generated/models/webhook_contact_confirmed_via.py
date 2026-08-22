from typing import Literal

WebhookContactConfirmedVia = Literal["code", "inherit"]

WEBHOOK_CONTACT_CONFIRMED_VIA_VALUES: set[WebhookContactConfirmedVia] = {
    "code",
    "inherit",
}


def check_webhook_contact_confirmed_via(value: str) -> WebhookContactConfirmedVia:
    if value in WEBHOOK_CONTACT_CONFIRMED_VIA_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOK_CONTACT_CONFIRMED_VIA_VALUES!r}")
