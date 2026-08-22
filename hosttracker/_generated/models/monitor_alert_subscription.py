from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.monitor_alert_subscription_alert_types_item import (
    MonitorAlertSubscriptionAlertTypesItem,
    check_monitor_alert_subscription_alert_types_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorAlertSubscription")


@_attrs_define
class MonitorAlertSubscription:
    """One alert wiring: notify these contacts about these state changes on THIS monitor."""

    contact_ids: list[UUID] | Unset = UNSET
    """ An existing contact to notify. """
    contact_refs: list[str] | Unset = UNSET
    """ The `ref` of a contact this same request creates. """
    alert_types: list[MonitorAlertSubscriptionAlertTypesItem] | Unset = UNSET
    """ Which state changes to notify about. """

    def to_dict(self) -> dict[str, Any]:
        contact_ids: list[str] | Unset = UNSET
        if not isinstance(self.contact_ids, Unset):
            contact_ids = []
            for contact_ids_item_data in self.contact_ids:
                contact_ids_item = str(contact_ids_item_data)
                contact_ids.append(contact_ids_item)

        contact_refs: list[str] | Unset = UNSET
        if not isinstance(self.contact_refs, Unset):
            contact_refs = self.contact_refs

        alert_types: list[str] | Unset = UNSET
        if not isinstance(self.alert_types, Unset):
            alert_types = []
            for alert_types_item_data in self.alert_types:
                alert_types_item: str = alert_types_item_data
                alert_types.append(alert_types_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if contact_ids is not UNSET:
            field_dict["contactIds"] = contact_ids
        if contact_refs is not UNSET:
            field_dict["contactRefs"] = contact_refs
        if alert_types is not UNSET:
            field_dict["alertTypes"] = alert_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _contact_ids = d.pop("contactIds", UNSET)
        contact_ids: list[UUID] | Unset = UNSET
        if _contact_ids is not UNSET:
            contact_ids = []
            for contact_ids_item_data in _contact_ids:
                contact_ids_item = UUID(contact_ids_item_data)

                contact_ids.append(contact_ids_item)

        contact_refs = cast(list[str], d.pop("contactRefs", UNSET))

        _alert_types = d.pop("alertTypes", UNSET)
        alert_types: list[MonitorAlertSubscriptionAlertTypesItem] | Unset = UNSET
        if _alert_types is not UNSET:
            alert_types = []
            for alert_types_item_data in _alert_types:
                alert_types_item = check_monitor_alert_subscription_alert_types_item(alert_types_item_data)

                alert_types.append(alert_types_item)

        monitor_alert_subscription = cls(
            contact_ids=contact_ids,
            contact_refs=contact_refs,
            alert_types=alert_types,
        )

        return monitor_alert_subscription
