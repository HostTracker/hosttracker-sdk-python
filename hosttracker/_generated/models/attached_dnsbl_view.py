from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attached_dnsbl_listing import AttachedDnsblListing


T = TypeVar("T", bound="AttachedDnsblView")


@_attrs_define
class AttachedDnsblView:
    """`attached.dnsbl` - what the last DNSBL sweep found, and when."""

    listings: list[AttachedDnsblListing] | Unset = UNSET
    checked_at: int | None | Unset = UNSET
    target_ip: None | str | Unset = UNSET
    """ The address the zones were queried for - the resolved web IP (or the MX exchanger) the sweep tested. Absent
    on rows that did not record one. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        listings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.listings, Unset):
            listings = []
            for listings_item_data in self.listings:
                listings_item = listings_item_data.to_dict()
                listings.append(listings_item)

        checked_at: int | None | Unset
        if isinstance(self.checked_at, Unset):
            checked_at = UNSET
        else:
            checked_at = self.checked_at

        target_ip: None | str | Unset
        if isinstance(self.target_ip, Unset):
            target_ip = UNSET
        else:
            target_ip = self.target_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if listings is not UNSET:
            field_dict["listings"] = listings
        if checked_at is not UNSET:
            field_dict["checkedAt"] = checked_at
        if target_ip is not UNSET:
            field_dict["targetIp"] = target_ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attached_dnsbl_listing import AttachedDnsblListing

        d = dict(src_dict)
        _listings = d.pop("listings", UNSET)
        listings: list[AttachedDnsblListing] | Unset = UNSET
        if _listings is not UNSET:
            listings = []
            for listings_item_data in _listings:
                listings_item = AttachedDnsblListing.from_dict(listings_item_data)

                listings.append(listings_item)

        def _parse_checked_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        checked_at = _parse_checked_at(d.pop("checkedAt", UNSET))

        def _parse_target_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_ip = _parse_target_ip(d.pop("targetIp", UNSET))

        attached_dnsbl_view = cls(
            listings=listings,
            checked_at=checked_at,
            target_ip=target_ip,
        )

        attached_dnsbl_view.additional_properties = d
        return attached_dnsbl_view

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
