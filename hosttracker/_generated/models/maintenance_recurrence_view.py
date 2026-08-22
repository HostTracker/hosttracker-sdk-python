from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaintenanceRecurrenceView")


@_attrs_define
class MaintenanceRecurrenceView:
    """The weekly recurrence, or absent for a one-time window."""

    week_days: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        week_days: list[str] | Unset = UNSET
        if not isinstance(self.week_days, Unset):
            week_days = self.week_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if week_days is not UNSET:
            field_dict["weekDays"] = week_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        week_days = cast(list[str], d.pop("weekDays", UNSET))

        maintenance_recurrence_view = cls(
            week_days=week_days,
        )

        maintenance_recurrence_view.additional_properties = d
        return maintenance_recurrence_view

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
