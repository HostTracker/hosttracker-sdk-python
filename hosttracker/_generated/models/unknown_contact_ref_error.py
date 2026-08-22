from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnknownContactRefError")


@_attrs_define
class UnknownContactRefError:
    pointer: str | Unset = UNSET
    """ Where the offending value is. """
    ref: str | Unset = UNSET
    """ The reference that could not be resolved. """
    declared: list[str] | Unset = UNSET
    """ The references the request did declare. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        ref = self.ref

        declared: list[str] | Unset = UNSET
        if not isinstance(self.declared, Unset):
            declared = self.declared

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if ref is not UNSET:
            field_dict["ref"] = ref
        if declared is not UNSET:
            field_dict["declared"] = declared

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        ref = d.pop("ref", UNSET)

        declared = cast(list[str], d.pop("declared", UNSET))

        unknown_contact_ref_error = cls(
            pointer=pointer,
            ref=ref,
            declared=declared,
        )

        unknown_contact_ref_error.additional_properties = d
        return unknown_contact_ref_error

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
