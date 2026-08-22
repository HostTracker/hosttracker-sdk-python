from typing import Literal

ContactGroupItemViewEventsItem = Literal[
    "daily", "down", "monthly", "quarterly", "repeatedlyDown", "up", "weekly", "yearly"
]

CONTACT_GROUP_ITEM_VIEW_EVENTS_ITEM_VALUES: set[ContactGroupItemViewEventsItem] = {
    "daily",
    "down",
    "monthly",
    "quarterly",
    "repeatedlyDown",
    "up",
    "weekly",
    "yearly",
}


def check_contact_group_item_view_events_item(value: str) -> ContactGroupItemViewEventsItem:
    if value in CONTACT_GROUP_ITEM_VIEW_EVENTS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_GROUP_ITEM_VIEW_EVENTS_ITEM_VALUES!r}")
