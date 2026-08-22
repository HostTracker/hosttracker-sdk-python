from typing import Literal

WebhookWriteRequestEventsItem = Literal[
    "certificate.expiring",
    "contact.confirmed",
    "contact.updated",
    "domain.expiring",
    "incident.closed",
    "incident.opened",
    "maintenance.ended",
    "monitor.created",
    "monitor.deleted",
    "monitor.down",
    "monitor.repeatedlyDown",
    "monitor.up",
    "monitor.updated",
]

WEBHOOK_WRITE_REQUEST_EVENTS_ITEM_VALUES: set[WebhookWriteRequestEventsItem] = {
    "certificate.expiring",
    "contact.confirmed",
    "contact.updated",
    "domain.expiring",
    "incident.closed",
    "incident.opened",
    "maintenance.ended",
    "monitor.created",
    "monitor.deleted",
    "monitor.down",
    "monitor.repeatedlyDown",
    "monitor.up",
    "monitor.updated",
}


def check_webhook_write_request_events_item(value: str) -> WebhookWriteRequestEventsItem:
    if value in WEBHOOK_WRITE_REQUEST_EVENTS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOK_WRITE_REQUEST_EVENTS_ITEM_VALUES!r}")
