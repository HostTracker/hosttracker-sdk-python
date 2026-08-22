from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_settings_dnsbl_attached import MonitorSettingsDnsblAttached


T = TypeVar("T", bound="MonitorSettingsNetAttachedChecks")


@_attrs_define
class MonitorSettingsNetAttachedChecks:
    """Sub-checks attachable to a Ping or Port monitor."""

    dnsbl: MonitorSettingsDnsblAttached | Unset = UNSET
    """ Blacklist checking as a sub-check of another monitor - by far its commonest form. """

    def to_dict(self) -> dict[str, Any]:
        dnsbl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dnsbl, Unset):
            dnsbl = self.dnsbl.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dnsbl is not UNSET:
            field_dict["dnsbl"] = dnsbl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_settings_dnsbl_attached import MonitorSettingsDnsblAttached

        d = dict(src_dict)
        _dnsbl = d.pop("dnsbl", UNSET)
        dnsbl: MonitorSettingsDnsblAttached | Unset
        if isinstance(_dnsbl, Unset):
            dnsbl = UNSET
        else:
            dnsbl = MonitorSettingsDnsblAttached.from_dict(_dnsbl)

        monitor_settings_net_attached_checks = cls(
            dnsbl=dnsbl,
        )

        return monitor_settings_net_attached_checks
