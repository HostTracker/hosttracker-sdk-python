from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.maintenance_view_state import MaintenanceViewState, check_maintenance_view_state
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.maintenance_monitor_view import MaintenanceMonitorView
    from ..models.maintenance_recurrence_view import MaintenanceRecurrenceView
    from ..models.maintenance_suppress_view import MaintenanceSuppressView


T = TypeVar("T", bound="MaintenanceView")


@_attrs_define
class MaintenanceView:
    """**The v2 maintenance-window resource**. **Dates are UTC Unix seconds, and the timezone travels with them**."""

    id: UUID
    from_: int
    """ The first occurrence's start, Unix seconds. Unix seconds. """
    to: int
    """ The first occurrence's end, Unix seconds - always `from` plus `durationSec` of REAL ELAPSED TIME (an
    absolute instant), never "the wall clock reads this". """
    duration_sec: int
    """ The window's length in real elapsed seconds. """
    enabled: bool
    overlimited: bool
    created: int
    """ Unix seconds. """
    updated: int
    name: None | str | Unset = UNSET
    timezone: str | Unset = UNSET
    """ The zone the stored wall clock is expressed in, as an **IANA** id (`Europe/Berlin`) - the same spelling `GET
    /account` publishes, and the only spelling this field accepts on a write. ⚠ **It is not always the id you
    sent.** Storage keeps the Windows name SQL's `AT TIME ZONE` requires, and that map is one-to-many: seventeen
    IANA zones share `W. Europe Standard Time`, so a window written as `Europe/Rome` reads back as `Europe/Berlin`.
    The two keep the same clock and the same daylight-saving rules - only the label collapses to the group's
    representative. """
    recurrence: MaintenanceRecurrenceView | None | Unset = UNSET
    """ The weekly recurrence, or absent for a one-time window. """
    state: MaintenanceViewState | Unset = UNSET
    suppress: MaintenanceSuppressView | None | Unset = UNSET
    """ What the window suppresses. **Present only when every monitor it covers shares one suppression, and omitted
    when they differ** - the per-monitor answer is always in `monitors`. """
    monitor_ids: list[UUID] | Unset = UNSET
    """ The window's resolved monitor set - always present, because a window scoped to nothing is a window that does
    nothing and a caller must be able to see that without a second read. """
    monitors: list[MaintenanceMonitorView] | Unset = UNSET
    """ **The window's coverage, one entry per monitor, always present** - each with the suppression that monitor
    really carries. This is the member to read and to send back: it is the storage model's own shape, so it survives
    a round trip whatever the window looks like. `expand=monitor` deepens each entry with the monitor's identifying
    projection. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.maintenance_recurrence_view import MaintenanceRecurrenceView
        from ..models.maintenance_suppress_view import MaintenanceSuppressView

        id = str(self.id)

        from_ = self.from_

        to = self.to

        duration_sec = self.duration_sec

        enabled = self.enabled

        overlimited = self.overlimited

        created = self.created

        updated = self.updated

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        timezone = self.timezone

        recurrence: dict[str, Any] | None | Unset
        if isinstance(self.recurrence, Unset):
            recurrence = UNSET
        elif isinstance(self.recurrence, MaintenanceRecurrenceView):
            recurrence = self.recurrence.to_dict()
        else:
            recurrence = self.recurrence

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        suppress: dict[str, Any] | None | Unset
        if isinstance(self.suppress, Unset):
            suppress = UNSET
        elif isinstance(self.suppress, MaintenanceSuppressView):
            suppress = self.suppress.to_dict()
        else:
            suppress = self.suppress

        monitor_ids: list[str] | Unset = UNSET
        if not isinstance(self.monitor_ids, Unset):
            monitor_ids = []
            for monitor_ids_item_data in self.monitor_ids:
                monitor_ids_item = str(monitor_ids_item_data)
                monitor_ids.append(monitor_ids_item)

        monitors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.monitors, Unset):
            monitors = []
            for monitors_item_data in self.monitors:
                monitors_item = monitors_item_data.to_dict()
                monitors.append(monitors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "from": from_,
                "to": to,
                "durationSec": duration_sec,
                "enabled": enabled,
                "overlimited": overlimited,
                "created": created,
                "updated": updated,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence
        if state is not UNSET:
            field_dict["state"] = state
        if suppress is not UNSET:
            field_dict["suppress"] = suppress
        if monitor_ids is not UNSET:
            field_dict["monitorIds"] = monitor_ids
        if monitors is not UNSET:
            field_dict["monitors"] = monitors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.maintenance_monitor_view import MaintenanceMonitorView
        from ..models.maintenance_recurrence_view import MaintenanceRecurrenceView
        from ..models.maintenance_suppress_view import MaintenanceSuppressView

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        from_ = d.pop("from")

        to = d.pop("to")

        duration_sec = d.pop("durationSec")

        enabled = d.pop("enabled")

        overlimited = d.pop("overlimited")

        created = d.pop("created")

        updated = d.pop("updated")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        timezone = d.pop("timezone", UNSET)

        def _parse_recurrence(data: object) -> MaintenanceRecurrenceView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                recurrence_type_0 = MaintenanceRecurrenceView.from_dict(data)

                return recurrence_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MaintenanceRecurrenceView | None | Unset, data)

        recurrence = _parse_recurrence(d.pop("recurrence", UNSET))

        _state = d.pop("state", UNSET)
        state: MaintenanceViewState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_maintenance_view_state(_state)

        def _parse_suppress(data: object) -> MaintenanceSuppressView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                suppress_type_0 = MaintenanceSuppressView.from_dict(data)

                return suppress_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MaintenanceSuppressView | None | Unset, data)

        suppress = _parse_suppress(d.pop("suppress", UNSET))

        _monitor_ids = d.pop("monitorIds", UNSET)
        monitor_ids: list[UUID] | Unset = UNSET
        if _monitor_ids is not UNSET:
            monitor_ids = []
            for monitor_ids_item_data in _monitor_ids:
                monitor_ids_item = UUID(monitor_ids_item_data)

                monitor_ids.append(monitor_ids_item)

        _monitors = d.pop("monitors", UNSET)
        monitors: list[MaintenanceMonitorView] | Unset = UNSET
        if _monitors is not UNSET:
            monitors = []
            for monitors_item_data in _monitors:
                monitors_item = MaintenanceMonitorView.from_dict(monitors_item_data)

                monitors.append(monitors_item)

        maintenance_view = cls(
            id=id,
            from_=from_,
            to=to,
            duration_sec=duration_sec,
            enabled=enabled,
            overlimited=overlimited,
            created=created,
            updated=updated,
            name=name,
            timezone=timezone,
            recurrence=recurrence,
            state=state,
            suppress=suppress,
            monitor_ids=monitor_ids,
            monitors=monitors,
        )

        maintenance_view.additional_properties = d
        return maintenance_view

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
