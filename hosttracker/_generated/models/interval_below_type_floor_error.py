from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IntervalBelowTypeFloorError")


@_attrs_define
class IntervalBelowTypeFloorError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    type_: str | Unset = UNSET
    """ The type the request named. """
    min_interval: int | Unset = UNSET
    """ The smallest interval this type accepts, in seconds. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        type_ = self.type_

        min_interval = self.min_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if type_ is not UNSET:
            field_dict["type"] = type_
        if min_interval is not UNSET:
            field_dict["minInterval"] = min_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        type_ = d.pop("type", UNSET)

        min_interval = d.pop("minInterval", UNSET)

        interval_below_type_floor_error = cls(
            pointer=pointer,
            type_=type_,
            min_interval=min_interval,
        )

        interval_below_type_floor_error.additional_properties = d
        return interval_below_type_floor_error

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
