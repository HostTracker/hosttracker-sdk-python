from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UptimeCheckCounts")


@_attrs_define
class UptimeCheckCounts:
    """The checks recorded in a bucket, split by outcome and by whether they ran inside a maintenance window. The four
    splits are disjoint and add up to the total.

    """

    total: int
    """ Every check recorded in the bucket - the sum of the four splits below. """
    up: int
    """ Checks that passed, outside any maintenance window. """
    down: int
    """ Checks that failed, outside any maintenance window. """
    maintenance_up: int
    """ Checks that passed while a maintenance window was open. """
    maintenance_down: int
    """ Checks that failed while a maintenance window was open - the failures the uptime figure excuses. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        up = self.up

        down = self.down

        maintenance_up = self.maintenance_up

        maintenance_down = self.maintenance_down

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "up": up,
                "down": down,
                "maintenanceUp": maintenance_up,
                "maintenanceDown": maintenance_down,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        up = d.pop("up")

        down = d.pop("down")

        maintenance_up = d.pop("maintenanceUp")

        maintenance_down = d.pop("maintenanceDown")

        uptime_check_counts = cls(
            total=total,
            up=up,
            down=down,
            maintenance_up=maintenance_up,
            maintenance_down=maintenance_down,
        )

        uptime_check_counts.additional_properties = d
        return uptime_check_counts

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
