from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvalidLimitError")


@_attrs_define
class InvalidLimitError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    parameter: str | Unset = UNSET
    """ The query parameter involved. """
    value: bool | float | str | Unset = UNSET
    """ The value that was rejected, echoed back. """
    min_: float | Unset = UNSET
    """ The smallest accepted value. """
    max_: float | Unset = UNSET
    """ The largest accepted value. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        parameter = self.parameter

        value: bool | float | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        min_ = self.min_

        max_ = self.max_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if parameter is not UNSET:
            field_dict["parameter"] = parameter
        if value is not UNSET:
            field_dict["value"] = value
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_

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

        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        invalid_limit_error = cls(
            pointer=pointer,
            parameter=parameter,
            value=value,
            min_=min_,
            max_=max_,
        )

        invalid_limit_error.additional_properties = d
        return invalid_limit_error

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
