from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.certificate_expiring_envelope_event import (
    CertificateExpiringEnvelopeEvent,
    check_certificate_expiring_envelope_event,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_certificate_expiring import WebhookCertificateExpiring


T = TypeVar("T", bound="CertificateExpiringEnvelope")


@_attrs_define
class CertificateExpiringEnvelope:
    """A `certificate.expiring` delivery. An sslExp check crosses its warning threshold."""

    event: CertificateExpiringEnvelopeEvent
    """ The event type, e.g. `monitor.down`. """
    data: WebhookCertificateExpiring
    """ A certificate check crossed one of its warning thresholds. """
    id: str | Unset = UNSET
    """ The delivery id, `d_<32 hex>` - the same token as the HT-Delivery header, stable across retries. """
    occurred_at: int | Unset = UNSET
    """ When the event happened, Unix seconds. """
    api_version: str | Unset = UNSET
    """ Always `v2`. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event: str = self.event

        data = self.data.to_dict()

        id = self.id

        occurred_at = self.occurred_at

        api_version = self.api_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
                "data": data,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if occurred_at is not UNSET:
            field_dict["occurredAt"] = occurred_at
        if api_version is not UNSET:
            field_dict["apiVersion"] = api_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_certificate_expiring import WebhookCertificateExpiring

        d = dict(src_dict)
        event = check_certificate_expiring_envelope_event(d.pop("event"))

        data = WebhookCertificateExpiring.from_dict(d.pop("data"))

        id = d.pop("id", UNSET)

        occurred_at = d.pop("occurredAt", UNSET)

        api_version = d.pop("apiVersion", UNSET)

        certificate_expiring_envelope = cls(
            event=event,
            data=data,
            id=id,
            occurred_at=occurred_at,
            api_version=api_version,
        )

        certificate_expiring_envelope.additional_properties = d
        return certificate_expiring_envelope

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
