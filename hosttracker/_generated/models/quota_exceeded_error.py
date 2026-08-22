from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuotaExceededError")


@_attrs_define
class QuotaExceededError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    limit: int | Unset = UNSET
    """ The ceiling that was hit. """
    remaining: int | Unset = UNSET
    """ How much headroom is left. """
    reset_at: int | Unset = UNSET
    """ When the window rolls over, in Unix seconds. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        limit = self.limit

        remaining = self.remaining

        reset_at = self.reset_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if limit is not UNSET:
            field_dict["limit"] = limit
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if reset_at is not UNSET:
            field_dict["resetAt"] = reset_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        limit = d.pop("limit", UNSET)

        remaining = d.pop("remaining", UNSET)

        reset_at = d.pop("resetAt", UNSET)

        quota_exceeded_error = cls(
            pointer=pointer,
            limit=limit,
            remaining=remaining,
            reset_at=reset_at,
        )

        quota_exceeded_error.additional_properties = d
        return quota_exceeded_error

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
