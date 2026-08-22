from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ContactPushSubscription")


@_attrs_define
class ContactPushSubscription:
    """The browser push subscription a `webPush` contact is created from - the three values the Push API hands a page: the
    subscription's endpoint and its two keys. Required for `webPush` and refused for every other type. The server pushes
    a verification message to the endpoint before the contact is written, so an unreachable subscription is refused
    rather than stored. Create only: pointing a contact at another browser is a new contact, not an edit. It is never
    returned by a read - the stored subscription is named by the contact's `botId`.

    """

    endpoint: str
    """ The push service URL the browser issued for this subscription. """
    p256dh: str
    """ The subscription's P-256 ECDH public key, base64url. """
    auth: str
    """ The subscription's authentication secret, base64url. """

    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint

        p256dh = self.p256dh

        auth = self.auth

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "endpoint": endpoint,
                "p256dh": p256dh,
                "auth": auth,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        endpoint = d.pop("endpoint")

        p256dh = d.pop("p256dh")

        auth = d.pop("auth")

        contact_push_subscription = cls(
            endpoint=endpoint,
            p256dh=p256dh,
            auth=auth,
        )

        return contact_push_subscription
