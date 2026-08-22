from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.maintenance_recurrence_week_days_item import (
    MaintenanceRecurrenceWeekDaysItem,
    check_maintenance_recurrence_week_days_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MaintenanceRecurrence")


@_attrs_define
class MaintenanceRecurrence:
    """How the window repeats. Send null to turn a recurring window back into a one-off."""

    week_days: list[MaintenanceRecurrenceWeekDaysItem] | Unset = UNSET
    """ The days the window repeats on, in the window's own time zone. """

    def to_dict(self) -> dict[str, Any]:
        week_days: list[str] | Unset = UNSET
        if not isinstance(self.week_days, Unset):
            week_days = []
            for week_days_item_data in self.week_days:
                week_days_item: str = week_days_item_data
                week_days.append(week_days_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if week_days is not UNSET:
            field_dict["weekDays"] = week_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _week_days = d.pop("weekDays", UNSET)
        week_days: list[MaintenanceRecurrenceWeekDaysItem] | Unset = UNSET
        if _week_days is not UNSET:
            week_days = []
            for week_days_item_data in _week_days:
                week_days_item = check_maintenance_recurrence_week_days_item(week_days_item_data)

                week_days.append(week_days_item)

        maintenance_recurrence = cls(
            week_days=week_days,
        )

        return maintenance_recurrence
