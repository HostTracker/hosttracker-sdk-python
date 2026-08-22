from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_test_result_view_outcome import (
    WebhookTestResultViewOutcome,
    check_webhook_test_result_view_outcome,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certificate_expiring_envelope import CertificateExpiringEnvelope
    from ..models.contact_confirmed_envelope import ContactConfirmedEnvelope
    from ..models.contact_updated_envelope import ContactUpdatedEnvelope
    from ..models.domain_expiring_envelope import DomainExpiringEnvelope
    from ..models.incident_closed_envelope import IncidentClosedEnvelope
    from ..models.incident_opened_envelope import IncidentOpenedEnvelope
    from ..models.job_completed_envelope import JobCompletedEnvelope
    from ..models.job_progress_envelope import JobProgressEnvelope
    from ..models.maintenance_ended_envelope import MaintenanceEndedEnvelope
    from ..models.monitor_created_envelope import MonitorCreatedEnvelope
    from ..models.monitor_deleted_envelope import MonitorDeletedEnvelope
    from ..models.monitor_down_envelope import MonitorDownEnvelope
    from ..models.monitor_repeatedly_down_envelope import MonitorRepeatedlyDownEnvelope
    from ..models.monitor_up_envelope import MonitorUpEnvelope
    from ..models.monitor_updated_envelope import MonitorUpdatedEnvelope


T = TypeVar("T", bound="WebhookTestResultView")


@_attrs_define
class WebhookTestResultView:
    latency_ms: int
    delivery_id: str | Unset = UNSET
    event: str | Unset = UNSET
    status_code: int | None | Unset = UNSET
    response_excerpt: None | str | Unset = UNSET
    """ ≤ 1 KB of the integrator's own response - enough to see their 500 page, not a log warehouse. """
    signature_sent: str | Unset = UNSET
    """ The exact `HT-Signature` header value sent - so a developer can verify their own HMAC. """
    payload: (
        CertificateExpiringEnvelope
        | ContactConfirmedEnvelope
        | ContactUpdatedEnvelope
        | DomainExpiringEnvelope
        | IncidentClosedEnvelope
        | IncidentOpenedEnvelope
        | JobCompletedEnvelope
        | JobProgressEnvelope
        | MaintenanceEndedEnvelope
        | MonitorCreatedEnvelope
        | MonitorDeletedEnvelope
        | MonitorDownEnvelope
        | MonitorRepeatedlyDownEnvelope
        | MonitorUpdatedEnvelope
        | MonitorUpEnvelope
        | Unset
    ) = UNSET
    """ The body POSTed to a registered webhook endpoint - one shape per event, selected by `event`. Not a response
    of any operation: see the webhook entries at the document root for the request we make to you, and the webhook-
    consumer section of the endpoint reference for the signature headers that accompany it. """
    outcome: WebhookTestResultViewOutcome | Unset = UNSET
    """ `delivered` | `failed`. """
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.certificate_expiring_envelope import CertificateExpiringEnvelope
        from ..models.contact_confirmed_envelope import ContactConfirmedEnvelope
        from ..models.contact_updated_envelope import ContactUpdatedEnvelope
        from ..models.domain_expiring_envelope import DomainExpiringEnvelope
        from ..models.incident_closed_envelope import IncidentClosedEnvelope
        from ..models.incident_opened_envelope import IncidentOpenedEnvelope
        from ..models.job_completed_envelope import JobCompletedEnvelope
        from ..models.maintenance_ended_envelope import MaintenanceEndedEnvelope
        from ..models.monitor_created_envelope import MonitorCreatedEnvelope
        from ..models.monitor_deleted_envelope import MonitorDeletedEnvelope
        from ..models.monitor_down_envelope import MonitorDownEnvelope
        from ..models.monitor_repeatedly_down_envelope import MonitorRepeatedlyDownEnvelope
        from ..models.monitor_up_envelope import MonitorUpEnvelope
        from ..models.monitor_updated_envelope import MonitorUpdatedEnvelope

        latency_ms = self.latency_ms

        delivery_id = self.delivery_id

        event = self.event

        status_code: int | None | Unset
        if isinstance(self.status_code, Unset):
            status_code = UNSET
        else:
            status_code = self.status_code

        response_excerpt: None | str | Unset
        if isinstance(self.response_excerpt, Unset):
            response_excerpt = UNSET
        else:
            response_excerpt = self.response_excerpt

        signature_sent = self.signature_sent

        payload: dict[str, Any] | Unset
        if isinstance(self.payload, Unset):
            payload = UNSET
        elif isinstance(self.payload, MonitorDownEnvelope):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, MonitorUpEnvelope):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, MonitorRepeatedlyDownEnvelope):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, IncidentOpenedEnvelope):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, IncidentClosedEnvelope):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, MonitorCreatedEnvelope):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, MonitorUpdatedEnvelope):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, MonitorDeletedEnvelope):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, MaintenanceEndedEnvelope):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, CertificateExpiringEnvelope):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, DomainExpiringEnvelope):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, ContactConfirmedEnvelope):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, ContactUpdatedEnvelope):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, JobCompletedEnvelope):
            payload = self.payload.to_dict()
        else:
            payload = self.payload.to_dict()

        outcome: str | Unset = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "latencyMs": latency_ms,
            }
        )
        if delivery_id is not UNSET:
            field_dict["deliveryId"] = delivery_id
        if event is not UNSET:
            field_dict["event"] = event
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if response_excerpt is not UNSET:
            field_dict["responseExcerpt"] = response_excerpt
        if signature_sent is not UNSET:
            field_dict["signatureSent"] = signature_sent
        if payload is not UNSET:
            field_dict["payload"] = payload
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.certificate_expiring_envelope import CertificateExpiringEnvelope
        from ..models.contact_confirmed_envelope import ContactConfirmedEnvelope
        from ..models.contact_updated_envelope import ContactUpdatedEnvelope
        from ..models.domain_expiring_envelope import DomainExpiringEnvelope
        from ..models.incident_closed_envelope import IncidentClosedEnvelope
        from ..models.incident_opened_envelope import IncidentOpenedEnvelope
        from ..models.job_completed_envelope import JobCompletedEnvelope
        from ..models.job_progress_envelope import JobProgressEnvelope
        from ..models.maintenance_ended_envelope import MaintenanceEndedEnvelope
        from ..models.monitor_created_envelope import MonitorCreatedEnvelope
        from ..models.monitor_deleted_envelope import MonitorDeletedEnvelope
        from ..models.monitor_down_envelope import MonitorDownEnvelope
        from ..models.monitor_repeatedly_down_envelope import MonitorRepeatedlyDownEnvelope
        from ..models.monitor_up_envelope import MonitorUpEnvelope
        from ..models.monitor_updated_envelope import MonitorUpdatedEnvelope

        d = dict(src_dict)
        latency_ms = d.pop("latencyMs")

        delivery_id = d.pop("deliveryId", UNSET)

        event = d.pop("event", UNSET)

        def _parse_status_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        status_code = _parse_status_code(d.pop("statusCode", UNSET))

        def _parse_response_excerpt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        response_excerpt = _parse_response_excerpt(d.pop("responseExcerpt", UNSET))

        signature_sent = d.pop("signatureSent", UNSET)

        def _parse_payload(
            data: object,
        ) -> (
            CertificateExpiringEnvelope
            | ContactConfirmedEnvelope
            | ContactUpdatedEnvelope
            | DomainExpiringEnvelope
            | IncidentClosedEnvelope
            | IncidentOpenedEnvelope
            | JobCompletedEnvelope
            | JobProgressEnvelope
            | MaintenanceEndedEnvelope
            | MonitorCreatedEnvelope
            | MonitorDeletedEnvelope
            | MonitorDownEnvelope
            | MonitorRepeatedlyDownEnvelope
            | MonitorUpdatedEnvelope
            | MonitorUpEnvelope
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_webhook_envelope_type_0 = MonitorDownEnvelope.from_dict(data)

                return componentsschemas_webhook_envelope_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_webhook_envelope_type_1 = MonitorUpEnvelope.from_dict(data)

                return componentsschemas_webhook_envelope_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_webhook_envelope_type_2 = MonitorRepeatedlyDownEnvelope.from_dict(data)

                return componentsschemas_webhook_envelope_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_webhook_envelope_type_3 = IncidentOpenedEnvelope.from_dict(data)

                return componentsschemas_webhook_envelope_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_webhook_envelope_type_4 = IncidentClosedEnvelope.from_dict(data)

                return componentsschemas_webhook_envelope_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_webhook_envelope_type_5 = MonitorCreatedEnvelope.from_dict(data)

                return componentsschemas_webhook_envelope_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_webhook_envelope_type_6 = MonitorUpdatedEnvelope.from_dict(data)

                return componentsschemas_webhook_envelope_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_webhook_envelope_type_7 = MonitorDeletedEnvelope.from_dict(data)

                return componentsschemas_webhook_envelope_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_webhook_envelope_type_8 = MaintenanceEndedEnvelope.from_dict(data)

                return componentsschemas_webhook_envelope_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_webhook_envelope_type_9 = CertificateExpiringEnvelope.from_dict(data)

                return componentsschemas_webhook_envelope_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_webhook_envelope_type_10 = DomainExpiringEnvelope.from_dict(data)

                return componentsschemas_webhook_envelope_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_webhook_envelope_type_11 = ContactConfirmedEnvelope.from_dict(data)

                return componentsschemas_webhook_envelope_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_webhook_envelope_type_12 = ContactUpdatedEnvelope.from_dict(data)

                return componentsschemas_webhook_envelope_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_webhook_envelope_type_13 = JobCompletedEnvelope.from_dict(data)

                return componentsschemas_webhook_envelope_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_webhook_envelope_type_14 = JobProgressEnvelope.from_dict(data)

            return componentsschemas_webhook_envelope_type_14

        payload = _parse_payload(d.pop("payload", UNSET))

        _outcome = d.pop("outcome", UNSET)
        outcome: WebhookTestResultViewOutcome | Unset
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = check_webhook_test_result_view_outcome(_outcome)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        webhook_test_result_view = cls(
            latency_ms=latency_ms,
            delivery_id=delivery_id,
            event=event,
            status_code=status_code,
            response_excerpt=response_excerpt,
            signature_sent=signature_sent,
            payload=payload,
            outcome=outcome,
            error=error,
        )

        webhook_test_result_view.additional_properties = d
        return webhook_test_result_view

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
