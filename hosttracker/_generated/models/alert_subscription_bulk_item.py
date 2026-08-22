from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.alert_subscription_bulk_item_alert_types_item import (
    AlertSubscriptionBulkItemAlertTypesItem,
    check_alert_subscription_bulk_item_alert_types_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertSubscriptionBulkItem")


@_attrs_define
class AlertSubscriptionBulkItem:
    """One wiring to add: every named alert type, from every named monitor, to every named contact."""

    alert_types: list[AlertSubscriptionBulkItemAlertTypesItem]
    """ At least one. """
    monitor_ids: list[UUID] | Unset = UNSET
    """ The monitors. Required unless the request sets `allMonitors`. """
    contact_ids: list[UUID] | Unset = UNSET
    """ The contacts. Required unless the request sets `allContacts`. """

    def to_dict(self) -> dict[str, Any]:
        alert_types = []
        for alert_types_item_data in self.alert_types:
            alert_types_item: str = alert_types_item_data
            alert_types.append(alert_types_item)

        monitor_ids: list[str] | Unset = UNSET
        if not isinstance(self.monitor_ids, Unset):
            monitor_ids = []
            for monitor_ids_item_data in self.monitor_ids:
                monitor_ids_item = str(monitor_ids_item_data)
                monitor_ids.append(monitor_ids_item)

        contact_ids: list[str] | Unset = UNSET
        if not isinstance(self.contact_ids, Unset):
            contact_ids = []
            for contact_ids_item_data in self.contact_ids:
                contact_ids_item = str(contact_ids_item_data)
                contact_ids.append(contact_ids_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "alertTypes": alert_types,
            }
        )
        if monitor_ids is not UNSET:
            field_dict["monitorIds"] = monitor_ids
        if contact_ids is not UNSET:
            field_dict["contactIds"] = contact_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alert_types = []
        _alert_types = d.pop("alertTypes")
        for alert_types_item_data in _alert_types:
            alert_types_item = check_alert_subscription_bulk_item_alert_types_item(alert_types_item_data)

            alert_types.append(alert_types_item)

        _monitor_ids = d.pop("monitorIds", UNSET)
        monitor_ids: list[UUID] | Unset = UNSET
        if _monitor_ids is not UNSET:
            monitor_ids = []
            for monitor_ids_item_data in _monitor_ids:
                monitor_ids_item = UUID(monitor_ids_item_data)

                monitor_ids.append(monitor_ids_item)

        _contact_ids = d.pop("contactIds", UNSET)
        contact_ids: list[UUID] | Unset = UNSET
        if _contact_ids is not UNSET:
            contact_ids = []
            for contact_ids_item_data in _contact_ids:
                contact_ids_item = UUID(contact_ids_item_data)

                contact_ids.append(contact_ids_item)

        alert_subscription_bulk_item = cls(
            alert_types=alert_types,
            monitor_ids=monitor_ids,
            contact_ids=contact_ids,
        )

        return alert_subscription_bulk_item
