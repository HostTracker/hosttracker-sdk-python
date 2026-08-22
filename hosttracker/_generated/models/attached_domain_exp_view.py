from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachedDomainExpView")


@_attrs_define
class AttachedDomainExpView:
    """`attached.domainExp` - the domain registration's expiry."""

    shared_domain: bool
    """ Always `true` - see the class remarks. """
    expires_at: int | None | Unset = UNSET
    """ Unix seconds. """
    days_left: int | None | Unset = UNSET
    domain: None | str | Unset = UNSET
    """ The domain the answer is about, when the row records one. """
    checked_at: int | None | Unset = UNSET
    """ Unix seconds. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shared_domain = self.shared_domain

        expires_at: int | None | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        days_left: int | None | Unset
        if isinstance(self.days_left, Unset):
            days_left = UNSET
        else:
            days_left = self.days_left

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        checked_at: int | None | Unset
        if isinstance(self.checked_at, Unset):
            checked_at = UNSET
        else:
            checked_at = self.checked_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sharedDomain": shared_domain,
            }
        )
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if days_left is not UNSET:
            field_dict["daysLeft"] = days_left
        if domain is not UNSET:
            field_dict["domain"] = domain
        if checked_at is not UNSET:
            field_dict["checkedAt"] = checked_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        shared_domain = d.pop("sharedDomain")

        def _parse_expires_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))

        def _parse_days_left(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_left = _parse_days_left(d.pop("daysLeft", UNSET))

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        def _parse_checked_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        checked_at = _parse_checked_at(d.pop("checkedAt", UNSET))

        attached_domain_exp_view = cls(
            shared_domain=shared_domain,
            expires_at=expires_at,
            days_left=days_left,
            domain=domain,
            checked_at=checked_at,
        )

        attached_domain_exp_view.additional_properties = d
        return attached_domain_exp_view

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
