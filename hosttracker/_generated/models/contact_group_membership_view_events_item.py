from typing import Literal

ContactGroupMembershipViewEventsItem = Literal[
    "daily", "down", "monthly", "quarterly", "repeatedlyDown", "up", "weekly", "yearly"
]

CONTACT_GROUP_MEMBERSHIP_VIEW_EVENTS_ITEM_VALUES: set[ContactGroupMembershipViewEventsItem] = {
    "daily",
    "down",
    "monthly",
    "quarterly",
    "repeatedlyDown",
    "up",
    "weekly",
    "yearly",
}


def check_contact_group_membership_view_events_item(value: str) -> ContactGroupMembershipViewEventsItem:
    if value in CONTACT_GROUP_MEMBERSHIP_VIEW_EVENTS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_GROUP_MEMBERSHIP_VIEW_EVENTS_ITEM_VALUES!r}")
