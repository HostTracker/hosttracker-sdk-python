from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_delete_cascade import MonitorDeleteCascade


T = TypeVar("T", bound="MonitorDeleteReceipt")


@_attrs_define
class MonitorDeleteReceipt:
    id: UUID
    deleted: bool
    type_: str | Unset = UNSET
    """ The monitor's identity at the moment it was deleted, so a receipt is readable on its own. """
    name: None | str | Unset = UNSET
    url: str | Unset = UNSET
    cascaded: MonitorDeleteCascade | Unset = UNSET
    """ What went with the monitor. """
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

        url = self.url

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
        if url is not UNSET:
            field_dict["url"] = url
        if cascaded is not UNSET:
            field_dict["cascaded"] = cascaded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_delete_cascade import MonitorDeleteCascade

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

        url = d.pop("url", UNSET)

        _cascaded = d.pop("cascaded", UNSET)
        cascaded: MonitorDeleteCascade | Unset
        if isinstance(_cascaded, Unset):
            cascaded = UNSET
        else:
            cascaded = MonitorDeleteCascade.from_dict(_cascaded)

        monitor_delete_receipt = cls(
            id=id,
            deleted=deleted,
            type_=type_,
            name=name,
            url=url,
            cascaded=cascaded,
        )

        monitor_delete_receipt.additional_properties = d
        return monitor_delete_receipt

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
