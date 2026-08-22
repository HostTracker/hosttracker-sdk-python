from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_attached_check import MonitorAttachedCheck


T = TypeVar("T", bound="MonitorAttached")


@_attrs_define
class MonitorAttached:
    """The sub-checks that run alongside this monitor. A kind's value is `true`/`false` to switch it on or off, or an
    object carrying that kind's own settings (with `enabled: false` to keep it configured but off). Whatever is set here
    must agree with `settings.attached` if both name the same kind.

    """

    dnsbl: bool | MonitorAttachedCheck | Unset = UNSET
    """ The `dnsbl` sub-check: `true`, `false`, or its settings object. """
    ssl_exp: bool | MonitorAttachedCheck | Unset = UNSET
    """ The `sslExp` sub-check: `true`, `false`, or its settings object. """
    domain_exp: bool | MonitorAttachedCheck | Unset = UNSET
    """ The `domainExp` sub-check: `true`, `false`, or its settings object. """
    web_risk: bool | MonitorAttachedCheck | Unset = UNSET
    """ The `webRisk` sub-check: `true`, `false`, or its settings object. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.monitor_attached_check import MonitorAttachedCheck

        dnsbl: bool | dict[str, Any] | Unset
        if isinstance(self.dnsbl, Unset):
            dnsbl = UNSET
        elif isinstance(self.dnsbl, MonitorAttachedCheck):
            dnsbl = self.dnsbl.to_dict()
        else:
            dnsbl = self.dnsbl

        ssl_exp: bool | dict[str, Any] | Unset
        if isinstance(self.ssl_exp, Unset):
            ssl_exp = UNSET
        elif isinstance(self.ssl_exp, MonitorAttachedCheck):
            ssl_exp = self.ssl_exp.to_dict()
        else:
            ssl_exp = self.ssl_exp

        domain_exp: bool | dict[str, Any] | Unset
        if isinstance(self.domain_exp, Unset):
            domain_exp = UNSET
        elif isinstance(self.domain_exp, MonitorAttachedCheck):
            domain_exp = self.domain_exp.to_dict()
        else:
            domain_exp = self.domain_exp

        web_risk: bool | dict[str, Any] | Unset
        if isinstance(self.web_risk, Unset):
            web_risk = UNSET
        elif isinstance(self.web_risk, MonitorAttachedCheck):
            web_risk = self.web_risk.to_dict()
        else:
            web_risk = self.web_risk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.monitor_attached_check import MonitorAttachedCheck

        d = dict(src_dict)

        def _parse_dnsbl(data: object) -> bool | MonitorAttachedCheck | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dnsbl_type_1 = MonitorAttachedCheck.from_dict(data)

                return dnsbl_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | MonitorAttachedCheck | Unset, data)

        dnsbl = _parse_dnsbl(d.pop("dnsbl", UNSET))

        def _parse_ssl_exp(data: object) -> bool | MonitorAttachedCheck | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ssl_exp_type_1 = MonitorAttachedCheck.from_dict(data)

                return ssl_exp_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | MonitorAttachedCheck | Unset, data)

        ssl_exp = _parse_ssl_exp(d.pop("sslExp", UNSET))

        def _parse_domain_exp(data: object) -> bool | MonitorAttachedCheck | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                domain_exp_type_1 = MonitorAttachedCheck.from_dict(data)

                return domain_exp_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | MonitorAttachedCheck | Unset, data)

        domain_exp = _parse_domain_exp(d.pop("domainExp", UNSET))

        def _parse_web_risk(data: object) -> bool | MonitorAttachedCheck | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                web_risk_type_1 = MonitorAttachedCheck.from_dict(data)

                return web_risk_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | MonitorAttachedCheck | Unset, data)

        web_risk = _parse_web_risk(d.pop("webRisk", UNSET))

        monitor_attached = cls(
            dnsbl=dnsbl,
            ssl_exp=ssl_exp,
            domain_exp=domain_exp,
            web_risk=web_risk,
        )

        monitor_attached.additional_properties = d
        return monitor_attached

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
