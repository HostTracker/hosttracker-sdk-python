from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.webhook_contact_confirmed_via import WebhookContactConfirmedVia, check_webhook_contact_confirmed_via

T = TypeVar("T", bound="WebhookContactConfirmed")


@_attrs_define
class WebhookContactConfirmed:
    """A contact became confirmed and can now receive alerts."""

    contact_id: UUID
    """ The contact's id - what GET /contact/{id} takes. """
    type_: str
    """ The contact-type token (email, sms, telegram, …). """
    address: str
    """ The delivery address that was confirmed. """
    confirmed_at: int
    """ When it was confirmed. Unix seconds. """
    via: WebhookContactConfirmedVia
    """ `code` - a confirmation code was submitted; `inherit` - the account had already confirmed this address. """

    def to_dict(self) -> dict[str, Any]:
        contact_id = str(self.contact_id)

        type_ = self.type_

        address = self.address

        confirmed_at = self.confirmed_at

        via: str = self.via

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "contactId": contact_id,
                "type": type_,
                "address": address,
                "confirmedAt": confirmed_at,
                "via": via,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contact_id = UUID(d.pop("contactId"))

        type_ = d.pop("type")

        address = d.pop("address")

        confirmed_at = d.pop("confirmedAt")

        via = check_webhook_contact_confirmed_via(d.pop("via"))

        webhook_contact_confirmed = cls(
            contact_id=contact_id,
            type_=type_,
            address=address,
            confirmed_at=confirmed_at,
            via=via,
        )

        return webhook_contact_confirmed
