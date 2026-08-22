from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuotaWindowView")


@_attrs_define
class QuotaWindowView:
    """One configured quota window: its bound, what has been spent, and when the window rolls."""

    limit: int
    used: int
    remaining: int
    reset_at: int
    """ When the current window ends and `used` returns to zero, Unix seconds. Unix seconds. """
    window_sec: int
    success_only: bool
    """ True when only SUCCESSFUL requests are counted (the storage's `reqSucc`): a 4xx/5xx does not spend the
    quota. It changes what a client should do on failure, so it is on the wire. """
    scope: str | Unset = UNSET
    """ The scope the quota applies to (`check:write`, …). """
    quota: str | Unset = UNSET
    """ Which quota this is - the storage's `quotaId` (e.g. requests-per-minute, checks-per-month). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        used = self.used

        remaining = self.remaining

        reset_at = self.reset_at

        window_sec = self.window_sec

        success_only = self.success_only

        scope = self.scope

        quota = self.quota

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
                "used": used,
                "remaining": remaining,
                "resetAt": reset_at,
                "windowSec": window_sec,
                "successOnly": success_only,
            }
        )
        if scope is not UNSET:
            field_dict["scope"] = scope
        if quota is not UNSET:
            field_dict["quota"] = quota

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit = d.pop("limit")

        used = d.pop("used")

        remaining = d.pop("remaining")

        reset_at = d.pop("resetAt")

        window_sec = d.pop("windowSec")

        success_only = d.pop("successOnly")

        scope = d.pop("scope", UNSET)

        quota = d.pop("quota", UNSET)

        quota_window_view = cls(
            limit=limit,
            used=used,
            remaining=remaining,
            reset_at=reset_at,
            window_sec=window_sec,
            success_only=success_only,
            scope=scope,
            quota=quota,
        )

        quota_window_view.additional_properties = d
        return quota_window_view

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
