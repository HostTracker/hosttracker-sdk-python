from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.contact_alert_subscription_alert_types_item import (
    ContactAlertSubscriptionAlertTypesItem,
    check_contact_alert_subscription_alert_types_item,
)

T = TypeVar("T", bound="ContactAlertSubscription")


@_attrs_define
class ContactAlertSubscription:
    """One alert wiring for THIS contact: notify it about these state changes on these monitors."""

    monitor_ids: list[UUID]
    """ A monitor to watch. At least one is required. """
    alert_types: list[ContactAlertSubscriptionAlertTypesItem]
    """ Which state changes to notify about. At least one is required. """

    def to_dict(self) -> dict[str, Any]:
        monitor_ids = []
        for monitor_ids_item_data in self.monitor_ids:
            monitor_ids_item = str(monitor_ids_item_data)
            monitor_ids.append(monitor_ids_item)

        alert_types = []
        for alert_types_item_data in self.alert_types:
            alert_types_item: str = alert_types_item_data
            alert_types.append(alert_types_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "monitorIds": monitor_ids,
                "alertTypes": alert_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monitor_ids = []
        _monitor_ids = d.pop("monitorIds")
        for monitor_ids_item_data in _monitor_ids:
            monitor_ids_item = UUID(monitor_ids_item_data)

            monitor_ids.append(monitor_ids_item)

        alert_types = []
        _alert_types = d.pop("alertTypes")
        for alert_types_item_data in _alert_types:
            alert_types_item = check_contact_alert_subscription_alert_types_item(alert_types_item_data)

            alert_types.append(alert_types_item)

        contact_alert_subscription = cls(
            monitor_ids=monitor_ids,
            alert_types=alert_types,
        )

        return contact_alert_subscription
