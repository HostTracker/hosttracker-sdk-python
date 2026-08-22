from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_test_exchange import ContactTestExchange


T = TypeVar("T", bound="ContactTestResult")


@_attrs_define
class ContactTestResult:
    """The outcome of a test delivery."""

    contact_id: UUID
    """ The contact the test was sent to. """
    alert_type: str
    """ The alert type that was rendered. """
    outcome: str
    """ The delivery outcome as the pipeline reported it. """
    origin: str
    """ Which delivery path handled the send - the production pipeline, or the local fallback used when it is
    unreachable. """
    notification_id: str | Unset = UNSET
    """ This delivery's own identifier, matching the alert log. """
    external_id: str | Unset = UNSET
    """ The identifier the downstream gateway assigned, when it returned one. """
    error: str | Unset = UNSET
    """ The failure detail, when the send did not succeed. """
    exchange: ContactTestExchange | Unset = UNSET
    """ The raw HTTP exchange, for an `http` contact: what was sent to the endpoint and what came back. Absent for
    every other contact type. Both strings are capped by the sender's capture limit, so a large response cannot
    inflate this body. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact_id = str(self.contact_id)

        alert_type = self.alert_type

        outcome = self.outcome

        origin = self.origin

        notification_id = self.notification_id

        external_id = self.external_id

        error = self.error

        exchange: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exchange, Unset):
            exchange = self.exchange.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contactId": contact_id,
                "alertType": alert_type,
                "outcome": outcome,
                "origin": origin,
            }
        )
        if notification_id is not UNSET:
            field_dict["notificationId"] = notification_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if error is not UNSET:
            field_dict["error"] = error
        if exchange is not UNSET:
            field_dict["exchange"] = exchange

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_test_exchange import ContactTestExchange

        d = dict(src_dict)
        contact_id = UUID(d.pop("contactId"))

        alert_type = d.pop("alertType")

        outcome = d.pop("outcome")

        origin = d.pop("origin")

        notification_id = d.pop("notificationId", UNSET)

        external_id = d.pop("externalId", UNSET)

        error = d.pop("error", UNSET)

        _exchange = d.pop("exchange", UNSET)
        exchange: ContactTestExchange | Unset
        if isinstance(_exchange, Unset):
            exchange = UNSET
        else:
            exchange = ContactTestExchange.from_dict(_exchange)

        contact_test_result = cls(
            contact_id=contact_id,
            alert_type=alert_type,
            outcome=outcome,
            origin=origin,
            notification_id=notification_id,
            external_id=external_id,
            error=error,
            exchange=exchange,
        )

        contact_test_result.additional_properties = d
        return contact_test_result

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
