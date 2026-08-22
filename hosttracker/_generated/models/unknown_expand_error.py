from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnknownExpandError")


@_attrs_define
class UnknownExpandError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    parameter: str | Unset = UNSET
    """ The query parameter involved. """
    value: bool | float | str | Unset = UNSET
    """ The value that was rejected, echoed back. """
    allowed: list[str] | Unset = UNSET
    """ The values that would have been accepted. """
    did_you_mean: str | Unset = UNSET
    """ The name this one is probably a misspelling of. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        parameter = self.parameter

        value: bool | float | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        allowed: list[str] | Unset = UNSET
        if not isinstance(self.allowed, Unset):
            allowed = self.allowed

        did_you_mean = self.did_you_mean

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if parameter is not UNSET:
            field_dict["parameter"] = parameter
        if value is not UNSET:
            field_dict["value"] = value
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if did_you_mean is not UNSET:
            field_dict["didYouMean"] = did_you_mean

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        parameter = d.pop("parameter", UNSET)

        def _parse_value(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        allowed = cast(list[str], d.pop("allowed", UNSET))

        did_you_mean = d.pop("didYouMean", UNSET)

        unknown_expand_error = cls(
            pointer=pointer,
            parameter=parameter,
            value=value,
            allowed=allowed,
            did_you_mean=did_you_mean,
        )

        unknown_expand_error.additional_properties = d
        return unknown_expand_error

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
