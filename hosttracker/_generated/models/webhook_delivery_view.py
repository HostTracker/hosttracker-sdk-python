from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_delivery_view_outcome import WebhookDeliveryViewOutcome, check_webhook_delivery_view_outcome
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_delivery_attempt_view import WebhookDeliveryAttemptView


T = TypeVar("T", bound="WebhookDeliveryView")


@_attrs_define
class WebhookDeliveryView:
    occurred_at: int
    """ Unix seconds. """
    id: str | Unset = UNSET
    event: str | Unset = UNSET
    attempts: list[WebhookDeliveryAttemptView] | Unset = UNSET
    """ EVERY attempt of this delivery, oldest first - the retry ladder, readable. """
    outcome: WebhookDeliveryViewOutcome | Unset = UNSET
    """ `pending` | `delivered` | `failed` | `dropped`. """
    next_retry_at: int | None | Unset = UNSET
    """ When the next attempt is due. """
    payload_digest: None | str | Unset = UNSET
    """ SHA-256 of the delivered body - identity without storing the body. """
    resource_id: None | Unset | UUID = UNSET
    """ The monitor/contact/job the delivery was about, when the log recorded one. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        occurred_at = self.occurred_at

        id = self.id

        event = self.event

        attempts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attempts, Unset):
            attempts = []
            for attempts_item_data in self.attempts:
                attempts_item = attempts_item_data.to_dict()
                attempts.append(attempts_item)

        outcome: str | Unset = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome

        next_retry_at: int | None | Unset
        if isinstance(self.next_retry_at, Unset):
            next_retry_at = UNSET
        else:
            next_retry_at = self.next_retry_at

        payload_digest: None | str | Unset
        if isinstance(self.payload_digest, Unset):
            payload_digest = UNSET
        else:
            payload_digest = self.payload_digest

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        elif isinstance(self.resource_id, UUID):
            resource_id = str(self.resource_id)
        else:
            resource_id = self.resource_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "occurredAt": occurred_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if event is not UNSET:
            field_dict["event"] = event
        if attempts is not UNSET:
            field_dict["attempts"] = attempts
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if next_retry_at is not UNSET:
            field_dict["nextRetryAt"] = next_retry_at
        if payload_digest is not UNSET:
            field_dict["payloadDigest"] = payload_digest
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_delivery_attempt_view import WebhookDeliveryAttemptView

        d = dict(src_dict)
        occurred_at = d.pop("occurredAt")

        id = d.pop("id", UNSET)

        event = d.pop("event", UNSET)

        _attempts = d.pop("attempts", UNSET)
        attempts: list[WebhookDeliveryAttemptView] | Unset = UNSET
        if _attempts is not UNSET:
            attempts = []
            for attempts_item_data in _attempts:
                attempts_item = WebhookDeliveryAttemptView.from_dict(attempts_item_data)

                attempts.append(attempts_item)

        _outcome = d.pop("outcome", UNSET)
        outcome: WebhookDeliveryViewOutcome | Unset
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = check_webhook_delivery_view_outcome(_outcome)

        def _parse_next_retry_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        next_retry_at = _parse_next_retry_at(d.pop("nextRetryAt", UNSET))

        def _parse_payload_digest(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payload_digest = _parse_payload_digest(d.pop("payloadDigest", UNSET))

        def _parse_resource_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resource_id_type_0 = UUID(data)

                return resource_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        resource_id = _parse_resource_id(d.pop("resourceId", UNSET))

        webhook_delivery_view = cls(
            occurred_at=occurred_at,
            id=id,
            event=event,
            attempts=attempts,
            outcome=outcome,
            next_retry_at=next_retry_at,
            payload_digest=payload_digest,
            resource_id=resource_id,
        )

        webhook_delivery_view.additional_properties = d
        return webhook_delivery_view

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
