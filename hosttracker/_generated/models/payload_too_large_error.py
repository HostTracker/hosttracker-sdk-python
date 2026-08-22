from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PayloadTooLargeError")


@_attrs_define
class PayloadTooLargeError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    limit: int | Unset = UNSET
    """ The ceiling that was hit. """
    actual: bool | float | str | Unset = UNSET
    """ What it found instead. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        limit = self.limit

        actual: bool | float | str | Unset
        if isinstance(self.actual, Unset):
            actual = UNSET
        else:
            actual = self.actual

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if limit is not UNSET:
            field_dict["limit"] = limit
        if actual is not UNSET:
            field_dict["actual"] = actual

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        limit = d.pop("limit", UNSET)

        def _parse_actual(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        actual = _parse_actual(d.pop("actual", UNSET))

        payload_too_large_error = cls(
            pointer=pointer,
            limit=limit,
            actual=actual,
        )

        payload_too_large_error.additional_properties = d
        return payload_too_large_error

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
