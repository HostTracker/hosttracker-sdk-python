from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypeImmutableError")


@_attrs_define
class TypeImmutableError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    current: bool | float | str | Unset = UNSET
    """ The value the resource currently holds. """
    requested: bool | float | str | Unset = UNSET
    """ The value the request asked for. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        current: bool | float | str | Unset
        if isinstance(self.current, Unset):
            current = UNSET
        else:
            current = self.current

        requested: bool | float | str | Unset
        if isinstance(self.requested, Unset):
            requested = UNSET
        else:
            requested = self.requested

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if current is not UNSET:
            field_dict["current"] = current
        if requested is not UNSET:
            field_dict["requested"] = requested

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        def _parse_current(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        current = _parse_current(d.pop("current", UNSET))

        def _parse_requested(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        requested = _parse_requested(d.pop("requested", UNSET))

        type_immutable_error = cls(
            pointer=pointer,
            current=current,
            requested=requested,
        )

        type_immutable_error.additional_properties = d
        return type_immutable_error

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
