from typing import Literal

NotificationResendReceiptFrequency = Literal["daily", "monthly", "quarterly", "weekly", "yearly"]

NOTIFICATION_RESEND_RECEIPT_FREQUENCY_VALUES: set[NotificationResendReceiptFrequency] = {
    "daily",
    "monthly",
    "quarterly",
    "weekly",
    "yearly",
}


def check_notification_resend_receipt_frequency(value: str) -> NotificationResendReceiptFrequency:
    if value in NOTIFICATION_RESEND_RECEIPT_FREQUENCY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_RESEND_RECEIPT_FREQUENCY_VALUES!r}")
