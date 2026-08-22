from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorSettingsDomainExpAttached")


@_attrs_define
class MonitorSettingsDomainExpAttached:
    """Domain-expiry watching as a sub-check of another monitor - its commonest form."""

    enabled: bool | Unset = False
    """ Watch the registration expiry of this monitor's domain. """

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        monitor_settings_domain_exp_attached = cls(
            enabled=enabled,
        )

        return monitor_settings_domain_exp_attached
