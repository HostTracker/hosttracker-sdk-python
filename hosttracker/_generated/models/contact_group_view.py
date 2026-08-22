from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_group_item_view import ContactGroupItemView


T = TypeVar("T", bound="ContactGroupView")


@_attrs_define
class ContactGroupView:
    id: UUID
    created: int
    """ Unix seconds. """
    name: str | Unset = UNSET
    items: list[ContactGroupItemView] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created = self.created

        name = self.name

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_group_item_view import ContactGroupItemView

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created = d.pop("created")

        name = d.pop("name", UNSET)

        _items = d.pop("items", UNSET)
        items: list[ContactGroupItemView] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = ContactGroupItemView.from_dict(items_item_data)

                items.append(items_item)

        contact_group_view = cls(
            id=id,
            created=created,
            name=name,
            items=items,
        )

        contact_group_view.additional_properties = d
        return contact_group_view

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
