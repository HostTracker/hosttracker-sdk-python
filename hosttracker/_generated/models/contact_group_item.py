from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.contact_group_item_events_item import ContactGroupItemEventsItem, check_contact_group_item_events_item

T = TypeVar("T", bound="ContactGroupItem")


@_attrs_define
class ContactGroupItem:
    """One contact and what the preset subscribes it to."""

    contact: UUID
    """ The contact. It must be the account's own. """
    events: list[ContactGroupItemEventsItem]
    """ At least one. The vocabulary spans both subscription kinds - the three alert types and the five report
    frequencies. """

    def to_dict(self) -> dict[str, Any]:
        contact = str(self.contact)

        events = []
        for events_item_data in self.events:
            events_item: str = events_item_data
            events.append(events_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "contact": contact,
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contact = UUID(d.pop("contact"))

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = check_contact_group_item_events_item(events_item_data)

            events.append(events_item)

        contact_group_item = cls(
            contact=contact,
            events=events,
        )

        return contact_group_item
