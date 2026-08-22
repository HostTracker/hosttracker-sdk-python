from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebhookCertificateExpiring")


@_attrs_define
class WebhookCertificateExpiring:
    """A certificate check crossed one of its warning thresholds."""

    monitor_id: UUID
    """ The monitor whose certificate is expiring. """
    not_after: int
    """ When the certificate expires. Unix seconds. """
    days_left: int
    """ Days until expiry. """
    issuer: str
    """ The issuing authority, when the warning carried one. """
    threshold: int
    """ The warning threshold this notice crossed, in days. """
    endpoint: str
    """ The endpoint as host:port. """

    def to_dict(self) -> dict[str, Any]:
        monitor_id = str(self.monitor_id)

        not_after = self.not_after

        days_left = self.days_left

        issuer = self.issuer

        threshold = self.threshold

        endpoint = self.endpoint

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "monitorId": monitor_id,
                "notAfter": not_after,
                "daysLeft": days_left,
                "issuer": issuer,
                "threshold": threshold,
                "endpoint": endpoint,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monitor_id = UUID(d.pop("monitorId"))

        not_after = d.pop("notAfter")

        days_left = d.pop("daysLeft")

        issuer = d.pop("issuer")

        threshold = d.pop("threshold")

        endpoint = d.pop("endpoint")

        webhook_certificate_expiring = cls(
            monitor_id=monitor_id,
            not_after=not_after,
            days_left=days_left,
            issuer=issuer,
            threshold=threshold,
            endpoint=endpoint,
        )

        return webhook_certificate_expiring
