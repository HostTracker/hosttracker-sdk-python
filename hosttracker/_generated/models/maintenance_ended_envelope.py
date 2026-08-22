from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.maintenance_ended_envelope_event import (
    MaintenanceEndedEnvelopeEvent,
    check_maintenance_ended_envelope_event,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_maintenance_ended import WebhookMaintenanceEnded


T = TypeVar("T", bound="MaintenanceEndedEnvelope")


@_attrs_define
class MaintenanceEndedEnvelope:
    """A `maintenance.ended` delivery. A maintenance window ends - either it expired on its own schedule, or it was
    cancelled early, which the payload marks with endedEarly:true.

    """

    event: MaintenanceEndedEnvelopeEvent
    """ The event type, e.g. `monitor.down`. """
    data: WebhookMaintenanceEnded
    """ A maintenance window stopped covering its monitors, by expiry or by an early cancel. """
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
        from ..models.webhook_maintenance_ended import WebhookMaintenanceEnded

        d = dict(src_dict)
        event = check_maintenance_ended_envelope_event(d.pop("event"))

        data = WebhookMaintenanceEnded.from_dict(d.pop("data"))

        id = d.pop("id", UNSET)

        occurred_at = d.pop("occurredAt", UNSET)

        api_version = d.pop("apiVersion", UNSET)

        maintenance_ended_envelope = cls(
            event=event,
            data=data,
            id=id,
            occurred_at=occurred_at,
            api_version=api_version,
        )

        maintenance_ended_envelope.additional_properties = d
        return maintenance_ended_envelope

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
