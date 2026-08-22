from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.contact_group_item import ContactGroupItem


T = TypeVar("T", bound="ContactGroupWriteRequest")


@_attrs_define
class ContactGroupWriteRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    items: list[ContactGroupItem]
    """ The group's WHOLE membership. On an update it replaces the snapshot rather than merging into it, because a
    group IS a snapshot. """
    name: str
    """ The group's name, unique per account and matched case-insensitively. """

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "items": items,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_group_item import ContactGroupItem

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ContactGroupItem.from_dict(items_item_data)

            items.append(items_item)

        name = d.pop("name")

        contact_group_write_request = cls(
            items=items,
            name=name,
        )

        return contact_group_write_request
