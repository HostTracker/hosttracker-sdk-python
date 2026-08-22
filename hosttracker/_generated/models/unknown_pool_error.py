from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnknownPoolError")


@_attrs_define
class UnknownPoolError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    pool: str | Unset = UNSET
    """ The pool the request named. """
    valid: list[str] | Unset = UNSET
    """ The pools that do exist, up to a cap. """
    valid_count: int | Unset = UNSET
    """ How many pools exist in total, when the list above was capped. """
    valid_truncated: bool | Unset = UNSET
    """ True when the list above is a prefix rather than the whole set. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        pool = self.pool

        valid: list[str] | Unset = UNSET
        if not isinstance(self.valid, Unset):
            valid = self.valid

        valid_count = self.valid_count

        valid_truncated = self.valid_truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if pool is not UNSET:
            field_dict["pool"] = pool
        if valid is not UNSET:
            field_dict["valid"] = valid
        if valid_count is not UNSET:
            field_dict["validCount"] = valid_count
        if valid_truncated is not UNSET:
            field_dict["validTruncated"] = valid_truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        pool = d.pop("pool", UNSET)

        valid = cast(list[str], d.pop("valid", UNSET))

        valid_count = d.pop("validCount", UNSET)

        valid_truncated = d.pop("validTruncated", UNSET)

        unknown_pool_error = cls(
            pointer=pointer,
            pool=pool,
            valid=valid,
            valid_count=valid_count,
            valid_truncated=valid_truncated,
        )

        unknown_pool_error.additional_properties = d
        return unknown_pool_error

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
