from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.monitor_deleted_envelope_event import MonitorDeletedEnvelopeEvent, check_monitor_deleted_envelope_event
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_delete_receipt import MonitorDeleteReceipt


T = TypeVar("T", bound="MonitorDeletedEnvelope")


@_attrs_define
class MonitorDeletedEnvelope:
    """A `monitor.deleted` delivery. A monitor is deleted - one event per monitor, including each monitor a bulk delete
    removes.

    """

    event: MonitorDeletedEnvelopeEvent
    """ The event type, e.g. `monitor.down`. """
    data: MonitorDeleteReceipt
    """ The event's own payload. Its shape is decided by `event` - see the per-event schemas this envelope's union
    names. """
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
        from ..models.monitor_delete_receipt import MonitorDeleteReceipt

        d = dict(src_dict)
        event = check_monitor_deleted_envelope_event(d.pop("event"))

        data = MonitorDeleteReceipt.from_dict(d.pop("data"))

        id = d.pop("id", UNSET)

        occurred_at = d.pop("occurredAt", UNSET)

        api_version = d.pop("apiVersion", UNSET)

        monitor_deleted_envelope = cls(
            event=event,
            data=data,
            id=id,
            occurred_at=occurred_at,
            api_version=api_version,
        )

        monitor_deleted_envelope.additional_properties = d
        return monitor_deleted_envelope

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
