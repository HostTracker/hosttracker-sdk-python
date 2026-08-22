from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DnsblMuteBody")


@_attrs_define
class DnsblMuteBody:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored. Every member is optional:
    what the body omits is left exactly as it was.

    """

    listings: list[str] | Unset = UNSET
    """ The blacklist names to silence or restore, as the listing report spells them. 1 to 100, and never empty - an
    empty selection is not "all". """
    muted: bool | Unset = UNSET
    """ True to silence these listings, false to start alerting on them again. """

    def to_dict(self) -> dict[str, Any]:
        listings: list[str] | Unset = UNSET
        if not isinstance(self.listings, Unset):
            listings = self.listings

        muted = self.muted

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if listings is not UNSET:
            field_dict["listings"] = listings
        if muted is not UNSET:
            field_dict["muted"] = muted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listings = cast(list[str], d.pop("listings", UNSET))

        muted = d.pop("muted", UNSET)

        dnsbl_mute_body = cls(
            listings=listings,
            muted=muted,
        )

        return dnsbl_mute_body
