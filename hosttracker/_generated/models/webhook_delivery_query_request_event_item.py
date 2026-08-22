from typing import Literal

WebhookDeliveryQueryRequestEventItem = Literal[
    "certificate.expiring",
    "contact.confirmed",
    "contact.updated",
    "domain.expiring",
    "incident.closed",
    "incident.opened",
    "job.completed",
    "job.progress",
    "maintenance.ended",
    "monitor.created",
    "monitor.deleted",
    "monitor.down",
    "monitor.repeatedlyDown",
    "monitor.up",
    "monitor.updated",
]

WEBHOOK_DELIVERY_QUERY_REQUEST_EVENT_ITEM_VALUES: set[WebhookDeliveryQueryRequestEventItem] = {
    "certificate.expiring",
    "contact.confirmed",
    "contact.updated",
    "domain.expiring",
    "incident.closed",
    "incident.opened",
    "job.completed",
    "job.progress",
    "maintenance.ended",
    "monitor.created",
    "monitor.deleted",
    "monitor.down",
    "monitor.repeatedlyDown",
    "monitor.up",
    "monitor.updated",
}


def check_webhook_delivery_query_request_event_item(value: str) -> WebhookDeliveryQueryRequestEventItem:
    if value in WEBHOOK_DELIVERY_QUERY_REQUEST_EVENT_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOK_DELIVERY_QUERY_REQUEST_EVENT_ITEM_VALUES!r}")
