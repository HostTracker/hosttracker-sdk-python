from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.monitor_report_subscription_frequency import (
    MonitorReportSubscriptionFrequency,
    check_monitor_report_subscription_frequency,
)
from ..models.monitor_report_subscription_type import (
    MonitorReportSubscriptionType,
    check_monitor_report_subscription_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorReportSubscription")


@_attrs_define
class MonitorReportSubscription:
    """One scheduled-report wiring for THIS monitor."""

    contact_ids: list[UUID] | Unset = UNSET
    """ An existing contact to deliver to. """
    contact_refs: list[str] | Unset = UNSET
    """ The `ref` of a contact this same request creates. """
    frequency: MonitorReportSubscriptionFrequency | Unset = UNSET
    """ How often the report is delivered. """
    type_: MonitorReportSubscriptionType | Unset = UNSET
    """ An accepted synonym for `frequency`, honoured only when `frequency` is absent. """

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

        frequency: str | Unset = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if contact_ids is not UNSET:
            field_dict["contactIds"] = contact_ids
        if contact_refs is not UNSET:
            field_dict["contactRefs"] = contact_refs
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if type_ is not UNSET:
            field_dict["type"] = type_

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

        _frequency = d.pop("frequency", UNSET)
        frequency: MonitorReportSubscriptionFrequency | Unset
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = check_monitor_report_subscription_frequency(_frequency)

        _type_ = d.pop("type", UNSET)
        type_: MonitorReportSubscriptionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_monitor_report_subscription_type(_type_)

        monitor_report_subscription = cls(
            contact_ids=contact_ids,
            contact_refs=contact_refs,
            frequency=frequency,
            type_=type_,
        )

        return monitor_report_subscription
