from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountUsageItemView")


@_attrs_define
class AccountUsageItemView:
    """One usage dimension: what the account has, and what its package allows."""

    used: int
    allowed: int | None | Unset = UNSET
    """ The package's cap, or **`null` for "no limit"** - never a fabricated 0, and never the sentinel `-1` it used
    to publish. A sentinel integer is a number a client can compare against by accident: `used > allowed` reads as
    "over the cap" for every unlimited dimension, and `allowed - used` reports negative headroom on an account that
    has no ceiling at all. JSON has a value for "there is no number here, and its absence is meaningful", so this
    member uses it. `0` keeps its own meaning - a real cap of nothing, which is how an unentitled feature reads. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        used = self.used

        allowed: int | None | Unset
        if isinstance(self.allowed, Unset):
            allowed = UNSET
        else:
            allowed = self.allowed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "used": used,
            }
        )
        if allowed is not UNSET:
            field_dict["allowed"] = allowed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        used = d.pop("used")

        def _parse_allowed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        allowed = _parse_allowed(d.pop("allowed", UNSET))

        account_usage_item_view = cls(
            used=used,
            allowed=allowed,
        )

        account_usage_item_view.additional_properties = d
        return account_usage_item_view

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
