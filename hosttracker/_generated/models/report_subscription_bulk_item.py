from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.report_subscription_bulk_item_frequencies_item import (
    ReportSubscriptionBulkItemFrequenciesItem,
    check_report_subscription_bulk_item_frequencies_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportSubscriptionBulkItem")


@_attrs_define
class ReportSubscriptionBulkItem:
    """One schedule to add: every named frequency, from every named monitor, to every named contact."""

    frequencies: list[ReportSubscriptionBulkItemFrequenciesItem]
    """ At least one. """
    monitor_ids: list[UUID] | Unset = UNSET
    """ The monitors. Required unless the request sets `allMonitors`. """
    contact_ids: list[UUID] | Unset = UNSET
    """ The contacts. Required unless the request sets `allContacts`. """

    def to_dict(self) -> dict[str, Any]:
        frequencies = []
        for frequencies_item_data in self.frequencies:
            frequencies_item: str = frequencies_item_data
            frequencies.append(frequencies_item)

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
                "frequencies": frequencies,
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
        frequencies = []
        _frequencies = d.pop("frequencies")
        for frequencies_item_data in _frequencies:
            frequencies_item = check_report_subscription_bulk_item_frequencies_item(frequencies_item_data)

            frequencies.append(frequencies_item)

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

        report_subscription_bulk_item = cls(
            frequencies=frequencies,
            monitor_ids=monitor_ids,
            contact_ids=contact_ids,
        )

        return report_subscription_bulk_item
