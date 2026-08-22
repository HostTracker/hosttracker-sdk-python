from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_view_severity import IncidentViewSeverity, check_incident_view_severity
from ..models.incident_view_state import IncidentViewState, check_incident_view_state
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_event_view import IncidentEventView
    from ..models.incident_recheck_view import IncidentRecheckView
    from ..models.result_error_view import ResultErrorView
    from ..models.results_monitor_ref_view import ResultsMonitorRefView


T = TypeVar("T", bound="IncidentView")


@_attrs_define
class IncidentView:
    monitor_id: UUID
    start: int
    """ When the episode started. Unix seconds. Unix seconds. """
    end: int
    """ When it ended. For an OPEN episode this is the last moment the monitor was observed down - present, not
    null, so a client can render a duration without special-casing; `state` is what says it is still running. Unix
    seconds. """
    duration_sec: int
    under_maintenance: bool
    """ True when the opening transition happened inside a maintenance window. """
    check_count: int
    """ Checks recorded inside the episode. """
    id: str | Unset = UNSET
    """ The incident's opaque id. Treat it as a token: address the incident with it, do not parse it. """
    monitor: None | ResultsMonitorRefView | Unset = UNSET
    state: IncidentViewState | Unset = UNSET
    """ `open` | `resolved`. """
    severity: IncidentViewSeverity | Unset = UNSET
    """ The severity band, derived from how long the outage lasted: `minor` | `major` | `critical`. """
    cause: None | ResultErrorView | Unset = UNSET
    """ The error that opened the episode, from the transition that started it. """
    comment: None | str | Unset = UNSET
    """ The operator's annotation. Empty string when none - never absent, so a client can bind it. """
    timeline: list[IncidentEventView] | None | Unset = UNSET
    recheck: IncidentRecheckView | None | Unset = UNSET
    """ The recheck constellation that opened the episode (`expand=recheck`): which location saw it first, which
    locations confirmed it and with which error, and which locations still saw the target up. Absent when the
    episode has no opening transition recorded. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.incident_recheck_view import IncidentRecheckView
        from ..models.result_error_view import ResultErrorView
        from ..models.results_monitor_ref_view import ResultsMonitorRefView

        monitor_id = str(self.monitor_id)

        start = self.start

        end = self.end

        duration_sec = self.duration_sec

        under_maintenance = self.under_maintenance

        check_count = self.check_count

        id = self.id

        monitor: dict[str, Any] | None | Unset
        if isinstance(self.monitor, Unset):
            monitor = UNSET
        elif isinstance(self.monitor, ResultsMonitorRefView):
            monitor = self.monitor.to_dict()
        else:
            monitor = self.monitor

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity

        cause: dict[str, Any] | None | Unset
        if isinstance(self.cause, Unset):
            cause = UNSET
        elif isinstance(self.cause, ResultErrorView):
            cause = self.cause.to_dict()
        else:
            cause = self.cause

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        timeline: list[dict[str, Any]] | None | Unset
        if isinstance(self.timeline, Unset):
            timeline = UNSET
        elif isinstance(self.timeline, list):
            timeline = []
            for timeline_type_0_item_data in self.timeline:
                timeline_type_0_item = timeline_type_0_item_data.to_dict()
                timeline.append(timeline_type_0_item)

        else:
            timeline = self.timeline

        recheck: dict[str, Any] | None | Unset
        if isinstance(self.recheck, Unset):
            recheck = UNSET
        elif isinstance(self.recheck, IncidentRecheckView):
            recheck = self.recheck.to_dict()
        else:
            recheck = self.recheck

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "monitorId": monitor_id,
                "start": start,
                "end": end,
                "durationSec": duration_sec,
                "underMaintenance": under_maintenance,
                "checkCount": check_count,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if state is not UNSET:
            field_dict["state"] = state
        if severity is not UNSET:
            field_dict["severity"] = severity
        if cause is not UNSET:
            field_dict["cause"] = cause
        if comment is not UNSET:
            field_dict["comment"] = comment
        if timeline is not UNSET:
            field_dict["timeline"] = timeline
        if recheck is not UNSET:
            field_dict["recheck"] = recheck

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.incident_event_view import IncidentEventView
        from ..models.incident_recheck_view import IncidentRecheckView
        from ..models.result_error_view import ResultErrorView
        from ..models.results_monitor_ref_view import ResultsMonitorRefView

        d = dict(src_dict)
        monitor_id = UUID(d.pop("monitorId"))

        start = d.pop("start")

        end = d.pop("end")

        duration_sec = d.pop("durationSec")

        under_maintenance = d.pop("underMaintenance")

        check_count = d.pop("checkCount")

        id = d.pop("id", UNSET)

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

        _state = d.pop("state", UNSET)
        state: IncidentViewState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_incident_view_state(_state)

        _severity = d.pop("severity", UNSET)
        severity: IncidentViewSeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = check_incident_view_severity(_severity)

        def _parse_cause(data: object) -> None | ResultErrorView | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cause_type_0 = ResultErrorView.from_dict(data)

                return cause_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResultErrorView | Unset, data)

        cause = _parse_cause(d.pop("cause", UNSET))

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_timeline(data: object) -> list[IncidentEventView] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                timeline_type_0 = []
                _timeline_type_0 = data
                for timeline_type_0_item_data in _timeline_type_0:
                    timeline_type_0_item = IncidentEventView.from_dict(timeline_type_0_item_data)

                    timeline_type_0.append(timeline_type_0_item)

                return timeline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IncidentEventView] | None | Unset, data)

        timeline = _parse_timeline(d.pop("timeline", UNSET))

        def _parse_recheck(data: object) -> IncidentRecheckView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                recheck_type_0 = IncidentRecheckView.from_dict(data)

                return recheck_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IncidentRecheckView | None | Unset, data)

        recheck = _parse_recheck(d.pop("recheck", UNSET))

        incident_view = cls(
            monitor_id=monitor_id,
            start=start,
            end=end,
            duration_sec=duration_sec,
            under_maintenance=under_maintenance,
            check_count=check_count,
            id=id,
            monitor=monitor,
            state=state,
            severity=severity,
            cause=cause,
            comment=comment,
            timeline=timeline,
            recheck=recheck,
        )

        incident_view.additional_properties = d
        return incident_view

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
