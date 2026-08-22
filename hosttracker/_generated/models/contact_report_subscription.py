from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.contact_report_subscription_frequency import (
    ContactReportSubscriptionFrequency,
    check_contact_report_subscription_frequency,
)

T = TypeVar("T", bound="ContactReportSubscription")


@_attrs_define
class ContactReportSubscription:
    """One scheduled-report wiring for THIS contact."""

    monitor_ids: list[UUID]
    """ A monitor to report on. At least one is required. """
    frequency: ContactReportSubscriptionFrequency
    """ How often the report is delivered. """

    def to_dict(self) -> dict[str, Any]:
        monitor_ids = []
        for monitor_ids_item_data in self.monitor_ids:
            monitor_ids_item = str(monitor_ids_item_data)
            monitor_ids.append(monitor_ids_item)

        frequency: str = self.frequency

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "monitorIds": monitor_ids,
                "frequency": frequency,
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

        frequency = check_contact_report_subscription_frequency(d.pop("frequency"))

        contact_report_subscription = cls(
            monitor_ids=monitor_ids,
            frequency=frequency,
        )

        return contact_report_subscription
