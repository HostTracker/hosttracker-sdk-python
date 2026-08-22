from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.contact_group_membership_entry import ContactGroupMembershipEntry


T = TypeVar("T", bound="ContactGroupMembershipRequest")


@_attrs_define
class ContactGroupMembershipRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    groups: list[ContactGroupMembershipEntry]
    """ The contact's WHOLE desired membership. A group this array omits is one the contact leaves, and an empty
    array removes it from every group. """

    def to_dict(self) -> dict[str, Any]:
        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "groups": groups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_group_membership_entry import ContactGroupMembershipEntry

        d = dict(src_dict)
        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = ContactGroupMembershipEntry.from_dict(groups_item_data)

            groups.append(groups_item)

        contact_group_membership_request = cls(
            groups=groups,
        )

        return contact_group_membership_request
