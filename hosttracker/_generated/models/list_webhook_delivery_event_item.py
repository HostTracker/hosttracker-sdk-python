from typing import Literal

ListWebhookDeliveryEventItem = Literal[
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

LIST_WEBHOOK_DELIVERY_EVENT_ITEM_VALUES: set[ListWebhookDeliveryEventItem] = {
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


def check_list_webhook_delivery_event_item(value: str) -> ListWebhookDeliveryEventItem:
    if value in LIST_WEBHOOK_DELIVERY_EVENT_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_WEBHOOK_DELIVERY_EVENT_ITEM_VALUES!r}")
