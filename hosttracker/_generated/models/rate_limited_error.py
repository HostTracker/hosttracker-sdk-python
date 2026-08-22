from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RateLimitedError")


@_attrs_define
class RateLimitedError:
    pointer: str | Unset = UNSET
    """ Where the offending value is - a JSON Pointer, or `/<name>` for a query parameter. """
    limit: int | Unset = UNSET
    """ The ceiling that was hit. """
    window: int | Unset = UNSET
    """ The rate-limit window, in seconds. """
    retry_after: int | Unset = UNSET
    """ Seconds to wait before retrying. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pointer = self.pointer

        limit = self.limit

        window = self.window

        retry_after = self.retry_after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pointer is not UNSET:
            field_dict["pointer"] = pointer
        if limit is not UNSET:
            field_dict["limit"] = limit
        if window is not UNSET:
            field_dict["window"] = window
        if retry_after is not UNSET:
            field_dict["retryAfter"] = retry_after

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pointer = d.pop("pointer", UNSET)

        limit = d.pop("limit", UNSET)

        window = d.pop("window", UNSET)

        retry_after = d.pop("retryAfter", UNSET)

        rate_limited_error = cls(
            pointer=pointer,
            limit=limit,
            window=window,
            retry_after=retry_after,
        )

        rate_limited_error.additional_properties = d
        return rate_limited_error

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
