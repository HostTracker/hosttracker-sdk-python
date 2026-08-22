from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorSettingsWebRiskAttached")


@_attrs_define
class MonitorSettingsWebRiskAttached:
    """Web Risk reputation checking as a sub-check of another monitor - by far its commonest form."""

    enabled: bool | Unset = False
    """ Whether the Web Risk sub-check runs alongside this monitor's own check. Absent inside a sent object means
    ON, exactly as for the three sibling flags; `false` turns it off. """
    interval: int | Unset = 43200
    """ Seconds between Web Risk lookups for this monitor. The default is 12 hours; only a negative value is
    refused, so no minimum is enforced on the attached form. """

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        interval = self.interval

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if interval is not UNSET:
            field_dict["interval"] = interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        interval = d.pop("interval", UNSET)

        monitor_settings_web_risk_attached = cls(
            enabled=enabled,
            interval=interval,
        )

        return monitor_settings_web_risk_attached
