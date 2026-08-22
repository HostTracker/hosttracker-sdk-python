from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DomainExpirationSettings")


@_attrs_define
class DomainExpirationSettings:
    """Watches a domain's registration expiry over whois/RDAP and alerts before it lapses. It always runs from a fixed
    internal check network rather than the public agent fleet, so there is no location to choose - `locations.pools` is
    refused if sent; omit `locations` entirely when creating this type.

    """

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        domain_expiration_settings = cls()

        return domain_expiration_settings
