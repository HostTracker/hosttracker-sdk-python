from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.alert_subscription_set_request_alert_types_item import (
    AlertSubscriptionSetRequestAlertTypesItem,
    check_alert_subscription_set_request_alert_types_item,
)

T = TypeVar("T", bound="AlertSubscriptionSetRequest")


@_attrs_define
class AlertSubscriptionSetRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    alert_types: list[AlertSubscriptionSetRequestAlertTypesItem]
    """ The EXACT set of alert types for this monitor-and-contact pair. At least one; use DELETE to remove. """

    def to_dict(self) -> dict[str, Any]:
        alert_types = []
        for alert_types_item_data in self.alert_types:
            alert_types_item: str = alert_types_item_data
            alert_types.append(alert_types_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "alertTypes": alert_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alert_types = []
        _alert_types = d.pop("alertTypes")
        for alert_types_item_data in _alert_types:
            alert_types_item = check_alert_subscription_set_request_alert_types_item(alert_types_item_data)

            alert_types.append(alert_types_item)

        alert_subscription_set_request = cls(
            alert_types=alert_types,
        )

        return alert_subscription_set_request
