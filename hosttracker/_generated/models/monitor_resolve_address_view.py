from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.monitor_resolve_address_view_family import (
    MonitorResolveAddressViewFamily,
    check_monitor_resolve_address_view_family,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorResolveAddressView")


@_attrs_define
class MonitorResolveAddressView:
    """One address a monitor's target currently resolves to."""

    ip: str | Unset = UNSET
    """ The address, as text. """
    family: MonitorResolveAddressViewFamily | Unset = UNSET
    """ The IP family - `ipv4` or `ipv6`, the same two words `GET /agent/ip` uses. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip = self.ip

        family: str | Unset = UNSET
        if not isinstance(self.family, Unset):
            family = self.family

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ip is not UNSET:
            field_dict["ip"] = ip
        if family is not UNSET:
            field_dict["family"] = family

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ip = d.pop("ip", UNSET)

        _family = d.pop("family", UNSET)
        family: MonitorResolveAddressViewFamily | Unset
        if isinstance(_family, Unset):
            family = UNSET
        else:
            family = check_monitor_resolve_address_view_family(_family)

        monitor_resolve_address_view = cls(
            ip=ip,
            family=family,
        )

        monitor_resolve_address_view.additional_properties = d
        return monitor_resolve_address_view

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
