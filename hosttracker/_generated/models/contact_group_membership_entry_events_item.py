from typing import Literal

ContactGroupMembershipEntryEventsItem = Literal[
    "daily", "down", "monthly", "quarterly", "repeatedlyDown", "up", "weekly", "yearly"
]

CONTACT_GROUP_MEMBERSHIP_ENTRY_EVENTS_ITEM_VALUES: set[ContactGroupMembershipEntryEventsItem] = {
    "daily",
    "down",
    "monthly",
    "quarterly",
    "repeatedlyDown",
    "up",
    "weekly",
    "yearly",
}


def check_contact_group_membership_entry_events_item(value: str) -> ContactGroupMembershipEntryEventsItem:
    if value in CONTACT_GROUP_MEMBERSHIP_ENTRY_EVENTS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACT_GROUP_MEMBERSHIP_ENTRY_EVENTS_ITEM_VALUES!r}"
    )
