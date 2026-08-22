from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.maintenance_monitor import MaintenanceMonitor
    from ..models.maintenance_recurrence import MaintenanceRecurrence
    from ..models.maintenance_suppress import MaintenanceSuppress


T = TypeVar("T", bound="MaintenancePatchRequest")


@_attrs_define
class MaintenancePatchRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored. Every member is optional:
    what the body omits is left exactly as it was.

    """

    duration_sec: int | Unset = UNSET
    """ How long the window lasts, in SECONDS. Give the window's length once - as this, or as `to`, never both. On a
    create one of the two is required; on an update, sending neither leaves the length as it was. """
    enabled: bool | Unset = UNSET
    """ Whether this is currently running. """
    from_: int | Unset = UNSET
    """ The start of the time window, in Unix seconds. """
    monitor_ids: list[UUID] | Unset = UNSET
    """ The monitors this window covers, all of them getting the `suppress` sent beside this member (alerts only,
    when it is omitted on a create). The shorthand for `monitors`; sending both is refused. On an update it REPLACES
    the previous set - a monitor already covered keeps its own suppression, and adding one to a window whose
    monitors do not all agree needs `suppress` or `monitors` in the same request. """
    monitors: list[MaintenanceMonitor] | Unset = UNSET
    """ The window's coverage, stated per monitor. Use this when the window treats its monitors differently; use
    `monitorIds` with a single `suppress` when they all get the same treatment. Sending both is refused. On an
    update it REPLACES the whole coverage, it does not add to it. """
    name: str | Unset = UNSET
    """ A display name. Never an identifier. """
    recurrence: MaintenanceRecurrence | Unset = UNSET
    """ How the window repeats. Send null to turn a recurring window back into a one-off. """
    suppress: MaintenanceSuppress | Unset = UNSET
    """ What the maintenance window suppresses. At least one of the two must be true - a window that suppresses
    neither does nothing and is refused. """
    timezone: str | Unset = UNSET
    """ The zone this request's clock times are read in, as an IANA zone id - "Europe/Berlin", not "W. Europe
    Standard Time". A Windows spelling is refused with the exact IANA id to send in the problem's `expected`. It is
    also the spelling returned - with one documented exception: several IANA zones share one stored zone, so a value
    read back can be the group's representative rather than the id you sent ("Europe/Rome" reads back as
    "Europe/Berlin"). The clock and the daylight-saving rules are the ones you asked for; only the label can be re-
    spelled. """
    to: int | Unset = UNSET
    """ When the window ends, in Unix seconds. Give the window's length once - as this, or as `durationSec`, never
    both. On a create one of the two is required; on an update, sending neither leaves the length as it was. """

    def to_dict(self) -> dict[str, Any]:
        duration_sec = self.duration_sec

        enabled = self.enabled

        from_ = self.from_

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

        name = self.name

        recurrence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recurrence, Unset):
            recurrence = self.recurrence.to_dict()

        suppress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suppress, Unset):
            suppress = self.suppress.to_dict()

        timezone = self.timezone

        to = self.to

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if duration_sec is not UNSET:
            field_dict["durationSec"] = duration_sec
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if from_ is not UNSET:
            field_dict["from"] = from_
        if monitor_ids is not UNSET:
            field_dict["monitorIds"] = monitor_ids
        if monitors is not UNSET:
            field_dict["monitors"] = monitors
        if name is not UNSET:
            field_dict["name"] = name
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence
        if suppress is not UNSET:
            field_dict["suppress"] = suppress
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.maintenance_monitor import MaintenanceMonitor
        from ..models.maintenance_recurrence import MaintenanceRecurrence
        from ..models.maintenance_suppress import MaintenanceSuppress

        d = dict(src_dict)
        duration_sec = d.pop("durationSec", UNSET)

        enabled = d.pop("enabled", UNSET)

        from_ = d.pop("from", UNSET)

        _monitor_ids = d.pop("monitorIds", UNSET)
        monitor_ids: list[UUID] | Unset = UNSET
        if _monitor_ids is not UNSET:
            monitor_ids = []
            for monitor_ids_item_data in _monitor_ids:
                monitor_ids_item = UUID(monitor_ids_item_data)

                monitor_ids.append(monitor_ids_item)

        _monitors = d.pop("monitors", UNSET)
        monitors: list[MaintenanceMonitor] | Unset = UNSET
        if _monitors is not UNSET:
            monitors = []
            for monitors_item_data in _monitors:
                monitors_item = MaintenanceMonitor.from_dict(monitors_item_data)

                monitors.append(monitors_item)

        name = d.pop("name", UNSET)

        _recurrence = d.pop("recurrence", UNSET)
        recurrence: MaintenanceRecurrence | Unset
        if isinstance(_recurrence, Unset):
            recurrence = UNSET
        else:
            recurrence = MaintenanceRecurrence.from_dict(_recurrence)

        _suppress = d.pop("suppress", UNSET)
        suppress: MaintenanceSuppress | Unset
        if isinstance(_suppress, Unset):
            suppress = UNSET
        else:
            suppress = MaintenanceSuppress.from_dict(_suppress)

        timezone = d.pop("timezone", UNSET)

        to = d.pop("to", UNSET)

        maintenance_patch_request = cls(
            duration_sec=duration_sec,
            enabled=enabled,
            from_=from_,
            monitor_ids=monitor_ids,
            monitors=monitors,
            name=name,
            recurrence=recurrence,
            suppress=suppress,
            timezone=timezone,
            to=to,
        )

        return maintenance_patch_request
