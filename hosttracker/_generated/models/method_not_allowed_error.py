from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodNotAllowedError")


@_attrs_define
class MethodNotAllowedError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    method: str | Unset = UNSET
    """ The method that was used. """
    allowed: list[str] | Unset = UNSET
    """ The values that would have been accepted. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        method = self.method

        allowed: list[str] | Unset = UNSET
        if not isinstance(self.allowed, Unset):
            allowed = self.allowed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if method is not UNSET:
            field_dict["method"] = method
        if allowed is not UNSET:
            field_dict["allowed"] = allowed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        method = d.pop("method", UNSET)

        allowed = cast(list[str], d.pop("allowed", UNSET))

        method_not_allowed_error = cls(
            pointer=pointer,
            method=method,
            allowed=allowed,
        )

        method_not_allowed_error.additional_properties = d
        return method_not_allowed_error

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
