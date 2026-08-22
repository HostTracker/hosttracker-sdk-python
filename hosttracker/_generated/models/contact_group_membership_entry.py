from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.contact_group_membership_entry_events_item import (
    ContactGroupMembershipEntryEventsItem,
    check_contact_group_membership_entry_events_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactGroupMembershipEntry")


@_attrs_define
class ContactGroupMembershipEntry:
    """One group the contact should be in."""

    id: UUID
    """ The contact group. It must be the account's own. """
    events: list[ContactGroupMembershipEntryEventsItem] | Unset = UNSET
    """ What to join this group with. Omit the member to join with the events the group already carries for its
    other members; an empty array is refused, because a membership with no events is not a membership. """

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item: str = events_item_data
                events.append(events_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
            }
        )
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        _events = d.pop("events", UNSET)
        events: list[ContactGroupMembershipEntryEventsItem] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = check_contact_group_membership_entry_events_item(events_item_data)

                events.append(events_item)

        contact_group_membership_entry = cls(
            id=id,
            events=events,
        )

        return contact_group_membership_entry
