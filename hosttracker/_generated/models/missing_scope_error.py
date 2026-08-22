from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MissingScopeError")


@_attrs_define
class MissingScopeError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    required: str | Unset = UNSET
    """ What the operation needed. """
    granted: list[str] | Unset = UNSET
    """ What the caller actually holds. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        required = self.required

        granted: list[str] | Unset = UNSET
        if not isinstance(self.granted, Unset):
            granted = self.granted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if required is not UNSET:
            field_dict["required"] = required
        if granted is not UNSET:
            field_dict["granted"] = granted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        required = d.pop("required", UNSET)

        granted = cast(list[str], d.pop("granted", UNSET))

        missing_scope_error = cls(
            pointer=pointer,
            required=required,
            granted=granted,
        )

        missing_scope_error.additional_properties = d
        return missing_scope_error

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
