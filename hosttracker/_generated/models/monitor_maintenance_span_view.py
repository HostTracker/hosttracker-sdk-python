from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MonitorMaintenanceSpanView")


@_attrs_define
class MonitorMaintenanceSpanView:
    """One maintenance OCCURRENCE intersecting the window, clipped to it."""

    from_: int
    """ Unix seconds. """
    to: int
    """ Unix seconds. """
    maintenance_id: UUID
    """ The maintenance window this occurrence belongs to - the id `GET /maintenance/{id}` takes. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        maintenance_id = str(self.maintenance_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "maintenanceId": maintenance_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = d.pop("from")

        to = d.pop("to")

        maintenance_id = UUID(d.pop("maintenanceId"))

        monitor_maintenance_span_view = cls(
            from_=from_,
            to=to,
            maintenance_id=maintenance_id,
        )

        monitor_maintenance_span_view.additional_properties = d
        return monitor_maintenance_span_view

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
