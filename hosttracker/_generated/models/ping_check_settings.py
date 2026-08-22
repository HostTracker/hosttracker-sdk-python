from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_settings_net_attached_checks import MonitorSettingsNetAttachedChecks


T = TypeVar("T", bound="PingCheckSettings")


@_attrs_define
class PingCheckSettings:
    """ICMP reachability check for a site, server or any web-connected device."""

    dns: list[str] | Unset = UNSET
    """ Resolver IPs to use instead of the agent's own. At most 4. """
    public_dns: int | Unset = UNSET
    """ Use public-DNS-filtered locations. 0 means absent. """
    expected_dns: list[str] | Unset = UNSET
    """ Resolver IPs the lookup is expected to come from. """
    expected_ips: list[str] | Unset = UNSET
    """ IPs the host is expected to resolve to; anything else fails the check. """
    attached: MonitorSettingsNetAttachedChecks | Unset = UNSET
    """ Sub-checks attachable to a Ping or Port monitor. """

    def to_dict(self) -> dict[str, Any]:
        dns: list[str] | Unset = UNSET
        if not isinstance(self.dns, Unset):
            dns = self.dns

        public_dns = self.public_dns

        expected_dns: list[str] | Unset = UNSET
        if not isinstance(self.expected_dns, Unset):
            expected_dns = self.expected_dns

        expected_ips: list[str] | Unset = UNSET
        if not isinstance(self.expected_ips, Unset):
            expected_ips = self.expected_ips

        attached: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attached, Unset):
            attached = self.attached.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dns is not UNSET:
            field_dict["dns"] = dns
        if public_dns is not UNSET:
            field_dict["publicDns"] = public_dns
        if expected_dns is not UNSET:
            field_dict["expectedDns"] = expected_dns
        if expected_ips is not UNSET:
            field_dict["expectedIps"] = expected_ips
        if attached is not UNSET:
            field_dict["attached"] = attached

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_settings_net_attached_checks import MonitorSettingsNetAttachedChecks

        d = dict(src_dict)
        dns = cast(list[str], d.pop("dns", UNSET))

        public_dns = d.pop("publicDns", UNSET)

        expected_dns = cast(list[str], d.pop("expectedDns", UNSET))

        expected_ips = cast(list[str], d.pop("expectedIps", UNSET))

        _attached = d.pop("attached", UNSET)
        attached: MonitorSettingsNetAttachedChecks | Unset
        if isinstance(_attached, Unset):
            attached = UNSET
        else:
            attached = MonitorSettingsNetAttachedChecks.from_dict(_attached)

        ping_check_settings = cls(
            dns=dns,
            public_dns=public_dns,
            expected_dns=expected_dns,
            expected_ips=expected_ips,
            attached=attached,
        )

        return ping_check_settings
