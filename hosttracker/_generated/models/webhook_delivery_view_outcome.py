from typing import Literal

WebhookDeliveryViewOutcome = Literal["delivered", "dropped", "failed", "pending"]

WEBHOOK_DELIVERY_VIEW_OUTCOME_VALUES: set[WebhookDeliveryViewOutcome] = {
    "delivered",
    "dropped",
    "failed",
    "pending",
}


def check_webhook_delivery_view_outcome(value: str) -> WebhookDeliveryViewOutcome:
    if value in WEBHOOK_DELIVERY_VIEW_OUTCOME_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOK_DELIVERY_VIEW_OUTCOME_VALUES!r}")
