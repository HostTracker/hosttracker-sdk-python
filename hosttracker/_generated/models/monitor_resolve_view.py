from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_resolve_address_view import MonitorResolveAddressView


T = TypeVar("T", bound="MonitorResolveView")


@_attrs_define
class MonitorResolveView:
    """**What the resolution found.** The url as the product reads it, the host it resolves, and the addresses that host
    currently answers with.

    """

    url: str | Unset = UNSET
    """ The url that was resolved - the caller's text made absolute, so a bare host comes back with the scheme a
    check would assume. """
    host: str | Unset = UNSET
    """ The host the addresses were looked up for. """
    addresses: list[MonitorResolveAddressView] | Unset = UNSET
    """ The addresses the host resolves to right now. **Empty means the name has no address records**, not that the
    lookup failed - a lookup that could not be completed answers `503` instead. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        host = self.host

        addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()
                addresses.append(addresses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if host is not UNSET:
            field_dict["host"] = host
        if addresses is not UNSET:
            field_dict["addresses"] = addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_resolve_address_view import MonitorResolveAddressView

        d = dict(src_dict)
        url = d.pop("url", UNSET)

        host = d.pop("host", UNSET)

        _addresses = d.pop("addresses", UNSET)
        addresses: list[MonitorResolveAddressView] | Unset = UNSET
        if _addresses is not UNSET:
            addresses = []
            for addresses_item_data in _addresses:
                addresses_item = MonitorResolveAddressView.from_dict(addresses_item_data)

                addresses.append(addresses_item)

        monitor_resolve_view = cls(
            url=url,
            host=host,
            addresses=addresses,
        )

        monitor_resolve_view.additional_properties = d
        return monitor_resolve_view

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
