from typing import Literal

WebhookPatchRequestEventsItem = Literal[
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

WEBHOOK_PATCH_REQUEST_EVENTS_ITEM_VALUES: set[WebhookPatchRequestEventsItem] = {
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


def check_webhook_patch_request_events_item(value: str) -> WebhookPatchRequestEventsItem:
    if value in WEBHOOK_PATCH_REQUEST_EVENTS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WEBHOOK_PATCH_REQUEST_EVENTS_ITEM_VALUES!r}")
