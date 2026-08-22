from typing import Literal

NotificationResendRequestFrequency = Literal["daily", "monthly", "quarterly", "weekly", "yearly"]

NOTIFICATION_RESEND_REQUEST_FREQUENCY_VALUES: set[NotificationResendRequestFrequency] = {
    "daily",
    "monthly",
    "quarterly",
    "weekly",
    "yearly",
}


def check_notification_resend_request_frequency(value: str) -> NotificationResendRequestFrequency:
    if value in NOTIFICATION_RESEND_REQUEST_FREQUENCY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_RESEND_REQUEST_FREQUENCY_VALUES!r}")
