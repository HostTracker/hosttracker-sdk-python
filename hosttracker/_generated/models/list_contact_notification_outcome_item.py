from typing import Literal

ListContactNotificationOutcomeItem = Literal[
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

LIST_CONTACT_NOTIFICATION_OUTCOME_ITEM_VALUES: set[ListContactNotificationOutcomeItem] = {
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


def check_list_contact_notification_outcome_item(value: str) -> ListContactNotificationOutcomeItem:
    if value in LIST_CONTACT_NOTIFICATION_OUTCOME_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CONTACT_NOTIFICATION_OUTCOME_ITEM_VALUES!r}")
