from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.attached_dnsbl_view import AttachedDnsblView
    from ..models.attached_domain_exp_view import AttachedDomainExpView
    from ..models.attached_ssl_exp_view import AttachedSslExpView
    from ..models.attached_web_risk_view import AttachedWebRiskView


T = TypeVar("T", bound="MonitorAttachedView")


@_attrs_define
class MonitorAttachedView:
    dnsbl: AttachedDnsblView
    """ `attached.dnsbl` - what the last DNSBL sweep found, and when. """
    ssl_exp: AttachedSslExpView
    """ `attached.sslExp` - the certificate's expiry as the last check observed it. """
    domain_exp: AttachedDomainExpView
    """ `attached.domainExp` - the domain registration's expiry. """
    web_risk: AttachedWebRiskView
    """ `attached.webRisk` - Google Web Risk's verdict for the monitor's url. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dnsbl = self.dnsbl.to_dict()

        ssl_exp = self.ssl_exp.to_dict()

        domain_exp = self.domain_exp.to_dict()

        web_risk = self.web_risk.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dnsbl": dnsbl,
                "sslExp": ssl_exp,
                "domainExp": domain_exp,
                "webRisk": web_risk,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attached_dnsbl_view import AttachedDnsblView
        from ..models.attached_domain_exp_view import AttachedDomainExpView
        from ..models.attached_ssl_exp_view import AttachedSslExpView
        from ..models.attached_web_risk_view import AttachedWebRiskView

        d = dict(src_dict)
        dnsbl = AttachedDnsblView.from_dict(d.pop("dnsbl"))

        ssl_exp = AttachedSslExpView.from_dict(d.pop("sslExp"))

        domain_exp = AttachedDomainExpView.from_dict(d.pop("domainExp"))

        web_risk = AttachedWebRiskView.from_dict(d.pop("webRisk"))

        monitor_attached_view = cls(
            dnsbl=dnsbl,
            ssl_exp=ssl_exp,
            domain_exp=domain_exp,
            web_risk=web_risk,
        )

        monitor_attached_view.additional_properties = d
        return monitor_attached_view

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
