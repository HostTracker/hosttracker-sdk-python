from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_active_period_days_item import ContactActivePeriodDaysItem, check_contact_active_period_days_item
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactActivePeriod")


@_attrs_define
class ContactActivePeriod:
    """The daily window during which this contact accepts delivery. Send null to remove the restriction, which is also the
    default: every day, all day.

    """

    start: str | Unset = UNSET
    """ When the window opens, as a clock time - `"08:00:00"`. Absent means midnight. """
    end: str | Unset = UNSET
    """ When the window closes, as a clock time. Absent means the end of the day. """
    days: list[ContactActivePeriodDaysItem] | Unset = UNSET
    """ Which days the window applies on. Omitting this member means every day; an empty array selects no days and
    stops delivery through this window; an unknown day name is refused, not ignored. """
    timezone: str | Unset = UNSET
    """ The zone the window's clock times are read in. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        end = self.end

        days: list[str] | Unset = UNSET
        if not isinstance(self.days, Unset):
            days = []
            for days_item_data in self.days:
                days_item: str = days_item_data
                days.append(days_item)

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if days is not UNSET:
            field_dict["days"] = days
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        _days = d.pop("days", UNSET)
        days: list[ContactActivePeriodDaysItem] | Unset = UNSET
        if _days is not UNSET:
            days = []
            for days_item_data in _days:
                days_item = check_contact_active_period_days_item(days_item_data)

                days.append(days_item)

        timezone = d.pop("timezone", UNSET)

        contact_active_period = cls(
            start=start,
            end=end,
            days=days,
            timezone=timezone,
        )

        contact_active_period.additional_properties = d
        return contact_active_period

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
