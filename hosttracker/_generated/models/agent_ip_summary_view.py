from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AgentIpSummaryView")


@_attrs_define
class AgentIpSummaryView:
    ipv4: int
    """ How many IPv4 addresses the current country scope holds. """
    ipv6: int
    """ How many IPv6 addresses the current country scope holds. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipv4 = self.ipv4

        ipv6 = self.ipv6

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ipv4": ipv4,
                "ipv6": ipv6,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ipv4 = d.pop("ipv4")

        ipv6 = d.pop("ipv6")

        agent_ip_summary_view = cls(
            ipv4=ipv4,
            ipv6=ipv6,
        )

        agent_ip_summary_view.additional_properties = d
        return agent_ip_summary_view

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
