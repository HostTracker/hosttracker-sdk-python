from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.maintenance_delete_cascade import MaintenanceDeleteCascade


T = TypeVar("T", bound="MaintenanceDeleteReceipt")


@_attrs_define
class MaintenanceDeleteReceipt:
    id: UUID
    deleted: bool
    was_active: bool
    """ True when the window was RUNNING at the moment it was cancelled. """
    type_: str | Unset = UNSET
    name: None | str | Unset = UNSET
    cascaded: MaintenanceDeleteCascade | Unset = UNSET
    """ What went with the window. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        deleted = self.deleted

        was_active = self.was_active

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
                "wasActive": was_active,
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
        from ..models.maintenance_delete_cascade import MaintenanceDeleteCascade

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        deleted = d.pop("deleted")

        was_active = d.pop("wasActive")

        type_ = d.pop("type", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _cascaded = d.pop("cascaded", UNSET)
        cascaded: MaintenanceDeleteCascade | Unset
        if isinstance(_cascaded, Unset):
            cascaded = UNSET
        else:
            cascaded = MaintenanceDeleteCascade.from_dict(_cascaded)

        maintenance_delete_receipt = cls(
            id=id,
            deleted=deleted,
            was_active=was_active,
            type_=type_,
            name=name,
            cascaded=cascaded,
        )

        maintenance_delete_receipt.additional_properties = d
        return maintenance_delete_receipt

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
