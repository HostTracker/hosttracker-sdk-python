from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.dnsbl_check_settings_scope import DNSBLCheckSettingsScope, check_dnsbl_check_settings_scope
from ..types import UNSET, Unset

T = TypeVar("T", bound="DNSBLCheckSettings")


@_attrs_define
class DNSBLCheckSettings:
    """Looks a domain or IP up in the DNS blacklists and alerts on a listing. It always runs from a fixed internal check
    network rather than the public agent fleet, so there is no location to choose - `locations.pools` is refused if
    sent; omit `locations` entirely when creating this type.

    """

    scope: DNSBLCheckSettingsScope | Unset = "firstWebIp"
    """ Which addresses of the monitored host are looked up in the blacklists. """

    def to_dict(self) -> dict[str, Any]:
        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _scope = d.pop("scope", UNSET)
        scope: DNSBLCheckSettingsScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = check_dnsbl_check_settings_scope(_scope)

        dnsbl_check_settings = cls(
            scope=scope,
        )

        return dnsbl_check_settings
