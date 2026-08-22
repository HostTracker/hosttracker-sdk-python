from typing import Literal

ContactGroupItemEventsItem = Literal[
    "daily", "down", "monthly", "quarterly", "repeatedlyDown", "up", "weekly", "yearly"
]

CONTACT_GROUP_ITEM_EVENTS_ITEM_VALUES: set[ContactGroupItemEventsItem] = {
    "daily",
    "down",
    "monthly",
    "quarterly",
    "repeatedlyDown",
    "up",
    "weekly",
    "yearly",
}


def check_contact_group_item_events_item(value: str) -> ContactGroupItemEventsItem:
    if value in CONTACT_GROUP_ITEM_EVENTS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_GROUP_ITEM_EVENTS_ITEM_VALUES!r}")
