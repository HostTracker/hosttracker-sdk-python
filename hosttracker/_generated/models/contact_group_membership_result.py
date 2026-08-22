from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_group_membership_view import ContactGroupMembershipView
    from ..models.contacts_contact_ref_view import ContactsContactRefView


T = TypeVar("T", bound="ContactGroupMembershipResult")


@_attrs_define
class ContactGroupMembershipResult:
    """What the contact's membership now is - the same element the read side lands under `expand=group`, so a caller can
    confirm the write against the shape it will read back.

    """

    contact: ContactsContactRefView | Unset = UNSET
    """ The minimal identifying projection of a contact, as embedded in relation reads. """
    groups: list[ContactGroupMembershipView] | Unset = UNSET
    """ Every group the contact is now in, name-ordered. An empty array means it is in none. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact is not UNSET:
            field_dict["contact"] = contact
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_group_membership_view import ContactGroupMembershipView
        from ..models.contacts_contact_ref_view import ContactsContactRefView

        d = dict(src_dict)
        _contact = d.pop("contact", UNSET)
        contact: ContactsContactRefView | Unset
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ContactsContactRefView.from_dict(_contact)

        _groups = d.pop("groups", UNSET)
        groups: list[ContactGroupMembershipView] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = ContactGroupMembershipView.from_dict(groups_item_data)

                groups.append(groups_item)

        contact_group_membership_result = cls(
            contact=contact,
            groups=groups,
        )

        contact_group_membership_result.additional_properties = d
        return contact_group_membership_result

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
