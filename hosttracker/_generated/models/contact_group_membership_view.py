from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_group_membership_view_events_item import (
    ContactGroupMembershipViewEventsItem,
    check_contact_group_membership_view_events_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactGroupMembershipView")


@_attrs_define
class ContactGroupMembershipView:
    """One contact group the contact belongs to, with the events the group holds for it. A group is a passive preset:
    membership by itself subscribes the contact to nothing. The same element is what `expand=group` lands on a contact
    row and what setting a contact's groups answers with, so the read and the write describe membership identically.

    """

    id: UUID
    name: str | Unset = UNSET
    events: list[ContactGroupMembershipViewEventsItem] | Unset = UNSET
    """ The events this group holds for this contact - alert types and report frequencies in one vocabulary, because
    one preset row can carry both. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item: str = events_item_data
                events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name", UNSET)

        _events = d.pop("events", UNSET)
        events: list[ContactGroupMembershipViewEventsItem] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = check_contact_group_membership_view_events_item(events_item_data)

                events.append(events_item)

        contact_group_membership_view = cls(
            id=id,
            name=name,
            events=events,
        )

        contact_group_membership_view.additional_properties = d
        return contact_group_membership_view

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
