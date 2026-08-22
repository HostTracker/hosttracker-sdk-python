from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountFlagsView")


@_attrs_define
class AccountFlagsView:
    enabled: bool
    active: bool
    overlimited: bool
    api_enabled: bool
    """ **Whether this account may use the API at all** - the package carries the `api` entitlement AND the billing
    profile's `apiPolicy` is not negative. It is the same predicate `POST /User/jwt` gates the token mint on,
    published so a client can SAY "the API is not enabled for this account" instead of inferring it from an empty
    quota document. **It informs; it never blocks.** Every read on this surface answers 200 with the account's real
    rows whether or not this is true - an unentitled account is told, not refused. What an unentitled account cannot
    do is MINT a token, which is a different door (`POST /User/jwt`, answering 403 with the reason). """
    disable_reason: None | str | Unset = UNSET
    stopped_at: int | None | Unset = UNSET
    """ When monitoring was stopped, Unix seconds. Omitted while it is running. Unix seconds. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        active = self.active

        overlimited = self.overlimited

        api_enabled = self.api_enabled

        disable_reason: None | str | Unset
        if isinstance(self.disable_reason, Unset):
            disable_reason = UNSET
        else:
            disable_reason = self.disable_reason

        stopped_at: int | None | Unset
        if isinstance(self.stopped_at, Unset):
            stopped_at = UNSET
        else:
            stopped_at = self.stopped_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "active": active,
                "overlimited": overlimited,
                "apiEnabled": api_enabled,
            }
        )
        if disable_reason is not UNSET:
            field_dict["disableReason"] = disable_reason
        if stopped_at is not UNSET:
            field_dict["stoppedAt"] = stopped_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        active = d.pop("active")

        overlimited = d.pop("overlimited")

        api_enabled = d.pop("apiEnabled")

        def _parse_disable_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disable_reason = _parse_disable_reason(d.pop("disableReason", UNSET))

        def _parse_stopped_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        stopped_at = _parse_stopped_at(d.pop("stoppedAt", UNSET))

        account_flags_view = cls(
            enabled=enabled,
            active=active,
            overlimited=overlimited,
            api_enabled=api_enabled,
            disable_reason=disable_reason,
            stopped_at=stopped_at,
        )

        account_flags_view.additional_properties = d
        return account_flags_view

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
