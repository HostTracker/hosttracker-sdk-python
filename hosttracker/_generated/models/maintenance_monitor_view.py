from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.maintenance_suppress_view import MaintenanceSuppressView
    from ..models.results_monitor_ref_view import ResultsMonitorRefView


T = TypeVar("T", bound="MaintenanceMonitorView")


@_attrs_define
class MaintenanceMonitorView:
    """**One monitor the window covers, with what it suppresses FOR THAT MONITOR.** A window can hold back alerting for one
    monitor and only keep another out of the statistics, so its suppression is per monitor - that is what this list
    carries. The window-level `suppress` beside it is a convenience that exists only while every monitor agrees; when
    they do not, it is omitted and this list is the only place the answer lives. `monitorId` and the expandable
    `monitor` object are the same pair every monitor-derived row on this surface carries (a result, an incident): the id
    is always there, the identifying projection - and, through `expand=monitor.<value>`, the monitor's own blocks -
    arrive only when asked for.

    """

    monitor_id: UUID
    """ The monitor this entry is about. """
    suppress: MaintenanceSuppressView | Unset = UNSET
    """ What a window suppresses while it is active, for one monitor. """
    monitor: None | ResultsMonitorRefView | Unset = UNSET
    """ `expand=monitor` - the monitor's identifying projection, plus any `monitor.<value>` blocks asked for. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.results_monitor_ref_view import ResultsMonitorRefView

        monitor_id = str(self.monitor_id)

        suppress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suppress, Unset):
            suppress = self.suppress.to_dict()

        monitor: dict[str, Any] | None | Unset
        if isinstance(self.monitor, Unset):
            monitor = UNSET
        elif isinstance(self.monitor, ResultsMonitorRefView):
            monitor = self.monitor.to_dict()
        else:
            monitor = self.monitor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "monitorId": monitor_id,
            }
        )
        if suppress is not UNSET:
            field_dict["suppress"] = suppress
        if monitor is not UNSET:
            field_dict["monitor"] = monitor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.maintenance_suppress_view import MaintenanceSuppressView
        from ..models.results_monitor_ref_view import ResultsMonitorRefView

        d = dict(src_dict)
        monitor_id = UUID(d.pop("monitorId"))

        _suppress = d.pop("suppress", UNSET)
        suppress: MaintenanceSuppressView | Unset
        if isinstance(_suppress, Unset):
            suppress = UNSET
        else:
            suppress = MaintenanceSuppressView.from_dict(_suppress)

        def _parse_monitor(data: object) -> None | ResultsMonitorRefView | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                monitor_type_0 = ResultsMonitorRefView.from_dict(data)

                return monitor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResultsMonitorRefView | Unset, data)

        monitor = _parse_monitor(d.pop("monitor", UNSET))

        maintenance_monitor_view = cls(
            monitor_id=monitor_id,
            suppress=suppress,
            monitor=monitor,
        )

        maintenance_monitor_view.additional_properties = d
        return maintenance_monitor_view

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
