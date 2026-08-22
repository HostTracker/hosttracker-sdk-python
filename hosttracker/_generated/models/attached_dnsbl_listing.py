from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachedDnsblListing")


@_attrs_define
class AttachedDnsblListing:
    """One blacklist listing."""

    ttl_sec: int
    """ The listing's TTL in SECONDS. """
    weight: int
    """ Severity as the live catalogue rates the zone: `0` info-only (never flips state), `1` normal, `2` major. The
    LIVE `DnsBlackListNames` row wins over the check-time snapshot so a catalogue re-tune shows on old results too.
    """
    muted: bool
    name: str | Unset = UNSET
    host: None | str | Unset = UNSET
    """ The listed endpoint when it is not the web A-record (an MX exchanger); absent for the web IP. """
    txt: None | str | Unset = UNSET
    """ The zone's TXT explanation, when it returned one. """
    removal_url: None | str | Unset = UNSET
    """ Where to request delisting, when the catalogue (or the snapshot) knows. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ttl_sec = self.ttl_sec

        weight = self.weight

        muted = self.muted

        name = self.name

        host: None | str | Unset
        if isinstance(self.host, Unset):
            host = UNSET
        else:
            host = self.host

        txt: None | str | Unset
        if isinstance(self.txt, Unset):
            txt = UNSET
        else:
            txt = self.txt

        removal_url: None | str | Unset
        if isinstance(self.removal_url, Unset):
            removal_url = UNSET
        else:
            removal_url = self.removal_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ttlSec": ttl_sec,
                "weight": weight,
                "muted": muted,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if host is not UNSET:
            field_dict["host"] = host
        if txt is not UNSET:
            field_dict["txt"] = txt
        if removal_url is not UNSET:
            field_dict["removalUrl"] = removal_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ttl_sec = d.pop("ttlSec")

        weight = d.pop("weight")

        muted = d.pop("muted")

        name = d.pop("name", UNSET)

        def _parse_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host = _parse_host(d.pop("host", UNSET))

        def _parse_txt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        txt = _parse_txt(d.pop("txt", UNSET))

        def _parse_removal_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        removal_url = _parse_removal_url(d.pop("removalUrl", UNSET))

        attached_dnsbl_listing = cls(
            ttl_sec=ttl_sec,
            weight=weight,
            muted=muted,
            name=name,
            host=host,
            txt=txt,
            removal_url=removal_url,
        )

        attached_dnsbl_listing.additional_properties = d
        return attached_dnsbl_listing

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
