from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_group_delete_cascade import ContactGroupDeleteCascade


T = TypeVar("T", bound="ContactGroupDeleteReceipt")


@_attrs_define
class ContactGroupDeleteReceipt:
    """The delete receipt - the same `{id, deleted, type, …identity, cascaded}` shape every other v2 delete answers with.
    It used to be a bare `{"deleted": true}`, which named neither the group that went nor how many memberships went with
    it.

    """

    id: UUID
    deleted: bool
    type_: str | Unset = UNSET
    """ The resource kind this receipt describes - always `"contactGroup"`, the same token this surface's own 404
    uses. """
    name: None | str | Unset = UNSET
    """ The group's name at the moment it was deleted, so a receipt is readable on its own. The name is free for
    another group after this. """
    cascaded: ContactGroupDeleteCascade | Unset = UNSET
    """ What went with the group. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        deleted = self.deleted

        type_ = self.type_

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        cascaded: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cascaded, Unset):
            cascaded = self.cascaded.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "deleted": deleted,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if cascaded is not UNSET:
            field_dict["cascaded"] = cascaded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_group_delete_cascade import ContactGroupDeleteCascade

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        deleted = d.pop("deleted")

        type_ = d.pop("type", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _cascaded = d.pop("cascaded", UNSET)
        cascaded: ContactGroupDeleteCascade | Unset
        if isinstance(_cascaded, Unset):
            cascaded = UNSET
        else:
            cascaded = ContactGroupDeleteCascade.from_dict(_cascaded)

        contact_group_delete_receipt = cls(
            id=id,
            deleted=deleted,
            type_=type_,
            name=name,
            cascaded=cascaded,
        )

        contact_group_delete_receipt.additional_properties = d
        return contact_group_delete_receipt

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
