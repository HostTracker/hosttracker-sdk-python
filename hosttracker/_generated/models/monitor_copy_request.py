from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.monitor_copy_request_on_overlimit import (
    MonitorCopyRequestOnOverlimit,
    check_monitor_copy_request_on_overlimit,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_copy_overrides import MonitorCopyOverrides
    from ..models.monitor_copy_target import MonitorCopyTarget


T = TypeVar("T", bound="MonitorCopyRequest")


@_attrs_define
class MonitorCopyRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    urls: list[MonitorCopyTarget | str]
    """ The addresses to copy the monitor to, one new monitor each, in order. The same address twice is refused
    rather than half-applied. """
    include_alerts: bool | Unset = UNSET
    """ Give every copy the source's alert subscriptions - the same contacts, the same alert types. Default true.
    """
    include_maintenance: bool | Unset = UNSET
    """ Add every copy to the maintenance windows the source is covered by, with the same suppression the source has
    in each. Default true. """
    include_reports: bool | Unset = UNSET
    """ Give every copy the source's report subscriptions - the same contacts, the same frequencies. Default true.
    """
    name: str | Unset = UNSET
    """ The name every copy takes unless its own `urls` entry names one. Omit it and each copy inherits the source
    monitor's name; send an empty string to leave the copies unnamed. """
    on_overlimit: MonitorCopyRequestOnOverlimit | Unset = UNSET
    """ What to do when the account's package will not fit the copies. "fail" (the default) refuses the WHOLE
    request before anything is written; "disable" creates the copies that do not fit disabled, with a package-limit
    reason, so nothing is lost. """
    overrides: MonitorCopyOverrides | Unset = UNSET
    """ An edit applied to EVERY copy, in the same shape a partial update takes. `settings` merges onto the source's
    stored settings at the leaf rather than replacing them, so overriding one field keeps the rest - including the
    credentials a read never returns. The member vocabulary is closed. """

    def to_dict(self) -> dict[str, Any]:
        from ..models.monitor_copy_target import MonitorCopyTarget

        urls = []
        for urls_item_data in self.urls:
            urls_item: dict[str, Any] | str
            if isinstance(urls_item_data, MonitorCopyTarget):
                urls_item = urls_item_data.to_dict()
            else:
                urls_item = urls_item_data
            urls.append(urls_item)

        include_alerts = self.include_alerts

        include_maintenance = self.include_maintenance

        include_reports = self.include_reports

        name = self.name

        on_overlimit: str | Unset = UNSET
        if not isinstance(self.on_overlimit, Unset):
            on_overlimit = self.on_overlimit

        overrides: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overrides, Unset):
            overrides = self.overrides.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "urls": urls,
            }
        )
        if include_alerts is not UNSET:
            field_dict["includeAlerts"] = include_alerts
        if include_maintenance is not UNSET:
            field_dict["includeMaintenance"] = include_maintenance
        if include_reports is not UNSET:
            field_dict["includeReports"] = include_reports
        if name is not UNSET:
            field_dict["name"] = name
        if on_overlimit is not UNSET:
            field_dict["onOverlimit"] = on_overlimit
        if overrides is not UNSET:
            field_dict["overrides"] = overrides

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_copy_overrides import MonitorCopyOverrides
        from ..models.monitor_copy_target import MonitorCopyTarget

        d = dict(src_dict)
        urls = []
        _urls = d.pop("urls")
        for urls_item_data in _urls:

            def _parse_urls_item(data: object) -> MonitorCopyTarget | str:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    urls_item_type_1 = MonitorCopyTarget.from_dict(data)

                    return urls_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(MonitorCopyTarget | str, data)

            urls_item = _parse_urls_item(urls_item_data)

            urls.append(urls_item)

        include_alerts = d.pop("includeAlerts", UNSET)

        include_maintenance = d.pop("includeMaintenance", UNSET)

        include_reports = d.pop("includeReports", UNSET)

        name = d.pop("name", UNSET)

        _on_overlimit = d.pop("onOverlimit", UNSET)
        on_overlimit: MonitorCopyRequestOnOverlimit | Unset
        if isinstance(_on_overlimit, Unset):
            on_overlimit = UNSET
        else:
            on_overlimit = check_monitor_copy_request_on_overlimit(_on_overlimit)

        _overrides = d.pop("overrides", UNSET)
        overrides: MonitorCopyOverrides | Unset
        if isinstance(_overrides, Unset):
            overrides = UNSET
        else:
            overrides = MonitorCopyOverrides.from_dict(_overrides)

        monitor_copy_request = cls(
            urls=urls,
            include_alerts=include_alerts,
            include_maintenance=include_maintenance,
            include_reports=include_reports,
            name=name,
            on_overlimit=on_overlimit,
            overrides=overrides,
        )

        return monitor_copy_request
