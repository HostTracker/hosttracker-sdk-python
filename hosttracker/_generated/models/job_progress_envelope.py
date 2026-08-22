from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_progress_envelope_event import JobProgressEnvelopeEvent, check_job_progress_envelope_event
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_job_progress import WebhookJobProgress


T = TypeVar("T", bound="JobProgressEnvelope")


@_attrs_define
class JobProgressEnvelope:
    """A `job.progress` delivery. An async job has made progress - a throttled interim report carrying its counts but no
    per-item results. Delivered only when the submitting request asked for callback:{webhookId, on:"progress"}; it
    cannot be subscribed to.

    """

    event: JobProgressEnvelopeEvent
    """ The event type, e.g. `monitor.down`. """
    data: WebhookJobProgress
    """ A throttled interim report for a running job - counts only, no per-item receipts. """
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
        from ..models.webhook_job_progress import WebhookJobProgress

        d = dict(src_dict)
        event = check_job_progress_envelope_event(d.pop("event"))

        data = WebhookJobProgress.from_dict(d.pop("data"))

        id = d.pop("id", UNSET)

        occurred_at = d.pop("occurredAt", UNSET)

        api_version = d.pop("apiVersion", UNSET)

        job_progress_envelope = cls(
            event=event,
            data=data,
            id=id,
            occurred_at=occurred_at,
            api_version=api_version,
        )

        job_progress_envelope.additional_properties = d
        return job_progress_envelope

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
