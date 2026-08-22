from typing import Literal

ContactNotificationQueryRequestOutcomeItem = Literal[
    "billingFailed",
    "blocked",
    "cancelled",
    "grouped",
    "insufficientBalance",
    "noProfile",
    "renderFailed",
    "sendFailed",
    "sent",
    "startingError",
    "superseded",
]

CONTACT_NOTIFICATION_QUERY_REQUEST_OUTCOME_ITEM_VALUES: set[ContactNotificationQueryRequestOutcomeItem] = {
    "billingFailed",
    "blocked",
    "cancelled",
    "grouped",
    "insufficientBalance",
    "noProfile",
    "renderFailed",
    "sendFailed",
    "sent",
    "startingError",
    "superseded",
}


def check_contact_notification_query_request_outcome_item(value: str) -> ContactNotificationQueryRequestOutcomeItem:
    if value in CONTACT_NOTIFICATION_QUERY_REQUEST_OUTCOME_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACT_NOTIFICATION_QUERY_REQUEST_OUTCOME_ITEM_VALUES!r}"
    )
