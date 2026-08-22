from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentIpView")


@_attrs_define
class AgentIpView:
    added_at: int
    """ When the address entered the fleet, Unix seconds - so a firewall script can diff. Unix seconds. """
    ip: str | Unset = UNSET
    family: str | Unset = UNSET
    """ The IP family - `ipv4` or `ipv6` - so a firewall script can build its v4 and v6 rule sets from one list.
    Filter one family at a time with `?family=`; the envelope `summary` carries the count of each. """
    country: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added_at = self.added_at

        ip = self.ip

        family = self.family

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "addedAt": added_at,
            }
        )
        if ip is not UNSET:
            field_dict["ip"] = ip
        if family is not UNSET:
            field_dict["family"] = family
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        added_at = d.pop("addedAt")

        ip = d.pop("ip", UNSET)

        family = d.pop("family", UNSET)

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        agent_ip_view = cls(
            added_at=added_at,
            ip=ip,
            family=family,
            country=country,
        )

        agent_ip_view.additional_properties = d
        return agent_ip_view

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
