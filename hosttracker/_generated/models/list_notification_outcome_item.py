from typing import Literal

ListNotificationOutcomeItem = Literal[
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

LIST_NOTIFICATION_OUTCOME_ITEM_VALUES: set[ListNotificationOutcomeItem] = {
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


def check_list_notification_outcome_item(value: str) -> ListNotificationOutcomeItem:
    if value in LIST_NOTIFICATION_OUTCOME_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_NOTIFICATION_OUTCOME_ITEM_VALUES!r}")
