from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachedSslExpView")


@_attrs_define
class AttachedSslExpView:
    """`attached.sslExp` - the certificate's expiry as the last check observed it."""

    revoked: bool
    """ True when the observation carried a revocation flag (unified: a `CertRevoked` TLS error). """
    not_after: int | None | Unset = UNSET
    """ Unix seconds. """
    not_before: int | None | Unset = UNSET
    """ When the certificate became valid - its issuance instant, which is what lets a client render the ELAPSED
    fraction of a validity window rather than only the days left. Omitted rather than nulled when the stored
    observation does not carry one: the field is ADDITIVE (only a new-enough agent build records it), so its absence
    means "this observation predates the field", not "this certificate has no start date" - and the satellite tier
    the reader falls back to has no such column at all. Unix seconds. """
    days_left: int | None | Unset = UNSET
    checked_at: int | None | Unset = UNSET
    """ Unix seconds. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revoked = self.revoked

        not_after: int | None | Unset
        if isinstance(self.not_after, Unset):
            not_after = UNSET
        else:
            not_after = self.not_after

        not_before: int | None | Unset
        if isinstance(self.not_before, Unset):
            not_before = UNSET
        else:
            not_before = self.not_before

        days_left: int | None | Unset
        if isinstance(self.days_left, Unset):
            days_left = UNSET
        else:
            days_left = self.days_left

        checked_at: int | None | Unset
        if isinstance(self.checked_at, Unset):
            checked_at = UNSET
        else:
            checked_at = self.checked_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "revoked": revoked,
            }
        )
        if not_after is not UNSET:
            field_dict["notAfter"] = not_after
        if not_before is not UNSET:
            field_dict["notBefore"] = not_before
        if days_left is not UNSET:
            field_dict["daysLeft"] = days_left
        if checked_at is not UNSET:
            field_dict["checkedAt"] = checked_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        revoked = d.pop("revoked")

        def _parse_not_after(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        not_after = _parse_not_after(d.pop("notAfter", UNSET))

        def _parse_not_before(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        not_before = _parse_not_before(d.pop("notBefore", UNSET))

        def _parse_days_left(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_left = _parse_days_left(d.pop("daysLeft", UNSET))

        def _parse_checked_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        checked_at = _parse_checked_at(d.pop("checkedAt", UNSET))

        attached_ssl_exp_view = cls(
            revoked=revoked,
            not_after=not_after,
            not_before=not_before,
            days_left=days_left,
            checked_at=checked_at,
        )

        attached_ssl_exp_view.additional_properties = d
        return attached_ssl_exp_view

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
