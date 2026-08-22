from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_group_item_view_events_item import (
    ContactGroupItemViewEventsItem,
    check_contact_group_item_view_events_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contacts_contact_ref_view import ContactsContactRefView


T = TypeVar("T", bound="ContactGroupItemView")


@_attrs_define
class ContactGroupItemView:
    """One member: the contact's identifying projection plus its event selection."""

    contact: ContactsContactRefView | Unset = UNSET
    """ The minimal identifying projection of a contact, as embedded in relation reads. """
    events: list[ContactGroupItemViewEventsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item: str = events_item_data
                events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact is not UNSET:
            field_dict["contact"] = contact
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contacts_contact_ref_view import ContactsContactRefView

        d = dict(src_dict)
        _contact = d.pop("contact", UNSET)
        contact: ContactsContactRefView | Unset
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ContactsContactRefView.from_dict(_contact)

        _events = d.pop("events", UNSET)
        events: list[ContactGroupItemViewEventsItem] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = check_contact_group_item_view_events_item(events_item_data)

                events.append(events_item)

        contact_group_item_view = cls(
            contact=contact,
            events=events,
        )

        contact_group_item_view.additional_properties = d
        return contact_group_item_view

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
