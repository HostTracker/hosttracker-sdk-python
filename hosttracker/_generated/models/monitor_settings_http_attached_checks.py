from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_settings_dnsbl_attached import MonitorSettingsDnsblAttached
    from ..models.monitor_settings_domain_exp_attached import MonitorSettingsDomainExpAttached
    from ..models.monitor_settings_ssl_exp_attached import MonitorSettingsSslExpAttached
    from ..models.monitor_settings_web_risk_attached import MonitorSettingsWebRiskAttached


T = TypeVar("T", bound="MonitorSettingsHttpAttachedChecks")


@_attrs_define
class MonitorSettingsHttpAttachedChecks:
    """Sub-checks attached to this monitor. An absent member means the sub-check is off."""

    dnsbl: MonitorSettingsDnsblAttached | Unset = UNSET
    """ Blacklist checking as a sub-check of another monitor - by far its commonest form. """
    ssl_exp: MonitorSettingsSslExpAttached | Unset = UNSET
    """ Certificate-expiry watching as a sub-check of another monitor - by far its commonest form. """
    domain_exp: MonitorSettingsDomainExpAttached | Unset = UNSET
    """ Domain-expiry watching as a sub-check of another monitor - its commonest form. """
    web_risk: MonitorSettingsWebRiskAttached | Unset = UNSET
    """ Web Risk reputation checking as a sub-check of another monitor - by far its commonest form. """

    def to_dict(self) -> dict[str, Any]:
        dnsbl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dnsbl, Unset):
            dnsbl = self.dnsbl.to_dict()

        ssl_exp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssl_exp, Unset):
            ssl_exp = self.ssl_exp.to_dict()

        domain_exp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.domain_exp, Unset):
            domain_exp = self.domain_exp.to_dict()

        web_risk: dict[str, Any] | Unset = UNSET
        if not isinstance(self.web_risk, Unset):
            web_risk = self.web_risk.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dnsbl is not UNSET:
            field_dict["dnsbl"] = dnsbl
        if ssl_exp is not UNSET:
            field_dict["sslExp"] = ssl_exp
        if domain_exp is not UNSET:
            field_dict["domainExp"] = domain_exp
        if web_risk is not UNSET:
            field_dict["webRisk"] = web_risk

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_settings_dnsbl_attached import MonitorSettingsDnsblAttached
        from ..models.monitor_settings_domain_exp_attached import MonitorSettingsDomainExpAttached
        from ..models.monitor_settings_ssl_exp_attached import MonitorSettingsSslExpAttached
        from ..models.monitor_settings_web_risk_attached import MonitorSettingsWebRiskAttached

        d = dict(src_dict)
        _dnsbl = d.pop("dnsbl", UNSET)
        dnsbl: MonitorSettingsDnsblAttached | Unset
        if isinstance(_dnsbl, Unset):
            dnsbl = UNSET
        else:
            dnsbl = MonitorSettingsDnsblAttached.from_dict(_dnsbl)

        _ssl_exp = d.pop("sslExp", UNSET)
        ssl_exp: MonitorSettingsSslExpAttached | Unset
        if isinstance(_ssl_exp, Unset):
            ssl_exp = UNSET
        else:
            ssl_exp = MonitorSettingsSslExpAttached.from_dict(_ssl_exp)

        _domain_exp = d.pop("domainExp", UNSET)
        domain_exp: MonitorSettingsDomainExpAttached | Unset
        if isinstance(_domain_exp, Unset):
            domain_exp = UNSET
        else:
            domain_exp = MonitorSettingsDomainExpAttached.from_dict(_domain_exp)

        _web_risk = d.pop("webRisk", UNSET)
        web_risk: MonitorSettingsWebRiskAttached | Unset
        if isinstance(_web_risk, Unset):
            web_risk = UNSET
        else:
            web_risk = MonitorSettingsWebRiskAttached.from_dict(_web_risk)

        monitor_settings_http_attached_checks = cls(
            dnsbl=dnsbl,
            ssl_exp=ssl_exp,
            domain_exp=domain_exp,
            web_risk=web_risk,
        )

        return monitor_settings_http_attached_checks
