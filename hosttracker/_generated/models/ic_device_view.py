from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IcDeviceView")


@_attrs_define
class IcDeviceView:
    """One device profile a page-loading check can be run as - the browser is emulated as that device, which changes the
    viewport, the pixel density and the user agent the target sees.

    """

    priority: int
    """ How prominently a picker should offer this profile - the higher the number, the nearer the top. The list
    already arrives in that order, so a client that just renders it in the order given is doing the right thing; the
    number is here for one that merges the profiles into a list of its own. """
    device: str | Unset = UNSET
    """ The profile's name, and the value to send: it is what a waterfall check's `deviceEmulation` setting takes,
    on an instant check and on a monitor alike. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        priority = self.priority

        device = self.device

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "priority": priority,
            }
        )
        if device is not UNSET:
            field_dict["device"] = device

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        priority = d.pop("priority")

        device = d.pop("device", UNSET)

        ic_device_view = cls(
            priority=priority,
            device=device,
        )

        ic_device_view.additional_properties = d
        return ic_device_view

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
