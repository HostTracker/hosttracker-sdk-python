from typing import Literal

NotificationQueryRequestOutcomeItem = Literal[
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

NOTIFICATION_QUERY_REQUEST_OUTCOME_ITEM_VALUES: set[NotificationQueryRequestOutcomeItem] = {
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


def check_notification_query_request_outcome_item(value: str) -> NotificationQueryRequestOutcomeItem:
    if value in NOTIFICATION_QUERY_REQUEST_OUTCOME_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_QUERY_REQUEST_OUTCOME_ITEM_VALUES!r}")
