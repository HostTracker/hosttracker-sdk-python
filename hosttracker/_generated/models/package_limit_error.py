from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageLimitError")


@_attrs_define
class PackageLimitError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    feature: str | Unset = UNSET
    """ The entitlement that blocks the operation. """
    used: int | Unset = UNSET
    """ How much of the entitlement is already used. """
    allowed: list[str] | Unset = UNSET
    """ The values that would have been accepted. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        feature = self.feature

        used = self.used

        allowed: list[str] | Unset = UNSET
        if not isinstance(self.allowed, Unset):
            allowed = self.allowed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if feature is not UNSET:
            field_dict["feature"] = feature
        if used is not UNSET:
            field_dict["used"] = used
        if allowed is not UNSET:
            field_dict["allowed"] = allowed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        feature = d.pop("feature", UNSET)

        used = d.pop("used", UNSET)

        allowed = cast(list[str], d.pop("allowed", UNSET))

        package_limit_error = cls(
            pointer=pointer,
            feature=feature,
            used=used,
            allowed=allowed,
        )

        package_limit_error.additional_properties = d
        return package_limit_error

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
