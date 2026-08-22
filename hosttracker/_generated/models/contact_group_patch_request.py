from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_group_item import ContactGroupItem


T = TypeVar("T", bound="ContactGroupPatchRequest")


@_attrs_define
class ContactGroupPatchRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored. Every member is optional:
    what the body omits is left exactly as it was.

    """

    items: list[ContactGroupItem] | Unset = UNSET
    """ The group's WHOLE membership. On an update it replaces the snapshot rather than merging into it, because a
    group IS a snapshot. """
    name: str | Unset = UNSET
    """ The group's name, unique per account and matched case-insensitively. """

    def to_dict(self) -> dict[str, Any]:
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_group_item import ContactGroupItem

        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[ContactGroupItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = ContactGroupItem.from_dict(items_item_data)

                items.append(items_item)

        name = d.pop("name", UNSET)

        contact_group_patch_request = cls(
            items=items,
            name=name,
        )

        return contact_group_patch_request
