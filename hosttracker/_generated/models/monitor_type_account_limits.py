from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MonitorTypeAccountLimits")


@_attrs_define
class MonitorTypeAccountLimits:
    """The per-type account block `accountLimits` - what THIS caller's package actually allows."""

    min_interval: int
    """ The account's EFFECTIVE interval floor for the type, in seconds - the larger of the product floor
    (`minInterval`) and the package's own floor. A 10-minute-tier account reads 600 here while `minInterval` still
    says the product floor. """
    available: bool
    """ False when the caller's package does not sell this type at all (a create would be refused with
    `package_limit`). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_interval = self.min_interval

        available = self.available

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "minInterval": min_interval,
                "available": available,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_interval = d.pop("minInterval")

        available = d.pop("available")

        monitor_type_account_limits = cls(
            min_interval=min_interval,
            available=available,
        )

        monitor_type_account_limits.additional_properties = d
        return monitor_type_account_limits

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
