from typing import Literal

WebhookMonitorAlertState = Literal["down", "up"]

WEBHOOK_MONITOR_ALERT_STATE_VALUES: set[WebhookMonitorAlertState] = {
    "down",
    "up",
}


def check_webhook_monitor_alert_state(value: str) -> WebhookMonitorAlertState:
    if value in WEBHOOK_MONITOR_ALERT_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOK_MONITOR_ALERT_STATE_VALUES!r}")
