from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.monitor_inline_contact_type import MonitorInlineContactType, check_monitor_inline_contact_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorInlineContact")


@_attrs_define
class MonitorInlineContact:
    """A contact to create (or bind, if the address already exists) alongside this monitor, addressable from the
    subscription blocks below by its `ref`.

    """

    ref: str
    """ A name for this entry, unique within the request. The subscription blocks reference it instead of an id that
    does not exist yet. """
    type_: MonitorInlineContactType
    """ Which kind of contact to create. """
    address: str
    """ The email address, phone number or url to deliver to. """
    name: None | str | Unset = UNSET
    """ A display name for the contact. """
    language: None | str | Unset = UNSET
    """ The language notifications are rendered in. """
    gateway: None | str | Unset = UNSET
    """ Which delivery gateway carries the message, for types that offer a choice. """
    alert_delay: int | Unset = UNSET
    """ How long a failure must persist before this contact hears about it, in MINUTES. """

    def to_dict(self) -> dict[str, Any]:
        ref = self.ref

        type_: str = self.type_

        address = self.address

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        gateway: None | str | Unset
        if isinstance(self.gateway, Unset):
            gateway = UNSET
        else:
            gateway = self.gateway

        alert_delay = self.alert_delay

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ref": ref,
                "type": type_,
                "address": address,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if language is not UNSET:
            field_dict["language"] = language
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if alert_delay is not UNSET:
            field_dict["alertDelay"] = alert_delay

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ref = d.pop("ref")

        type_ = check_monitor_inline_contact_type(d.pop("type"))

        address = d.pop("address")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_gateway(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gateway = _parse_gateway(d.pop("gateway", UNSET))

        alert_delay = d.pop("alertDelay", UNSET)

        monitor_inline_contact = cls(
            ref=ref,
            type_=type_,
            address=address,
            name=name,
            language=language,
            gateway=gateway,
            alert_delay=alert_delay,
        )

        return monitor_inline_contact
