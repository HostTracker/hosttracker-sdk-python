from typing import Literal

WebhookMonitorAlertRecheckState = Literal["down", "up"]

WEBHOOK_MONITOR_ALERT_RECHECK_STATE_VALUES: set[WebhookMonitorAlertRecheckState] = {
    "down",
    "up",
}


def check_webhook_monitor_alert_recheck_state(value: str) -> WebhookMonitorAlertRecheckState:
    if value in WEBHOOK_MONITOR_ALERT_RECHECK_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOK_MONITOR_ALERT_RECHECK_STATE_VALUES!r}")
