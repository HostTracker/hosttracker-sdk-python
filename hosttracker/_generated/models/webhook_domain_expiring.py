from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebhookDomainExpiring")


@_attrs_define
class WebhookDomainExpiring:
    """A domain check crossed one of its warning thresholds."""

    monitor_id: UUID
    """ The monitor whose domain registration is expiring. """
    expires_at: int
    """ When the registration expires. Unix seconds. """
    days_left: int
    """ Days until expiry. """
    registrar: str
    """ The registrar, when the warning carried one. """
    shared_domain: str
    """ The domain the expiry is keyed by - the same expiry can answer for several monitors. """
    threshold: int
    """ The warning threshold this notice crossed, in days. """

    def to_dict(self) -> dict[str, Any]:
        monitor_id = str(self.monitor_id)

        expires_at = self.expires_at

        days_left = self.days_left

        registrar = self.registrar

        shared_domain = self.shared_domain

        threshold = self.threshold

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "monitorId": monitor_id,
                "expiresAt": expires_at,
                "daysLeft": days_left,
                "registrar": registrar,
                "sharedDomain": shared_domain,
                "threshold": threshold,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monitor_id = UUID(d.pop("monitorId"))

        expires_at = d.pop("expiresAt")

        days_left = d.pop("daysLeft")

        registrar = d.pop("registrar")

        shared_domain = d.pop("sharedDomain")

        threshold = d.pop("threshold")

        webhook_domain_expiring = cls(
            monitor_id=monitor_id,
            expires_at=expires_at,
            days_left=days_left,
            registrar=registrar,
            shared_domain=shared_domain,
            threshold=threshold,
        )

        return webhook_domain_expiring
