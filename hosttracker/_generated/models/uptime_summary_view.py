from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.uptime_summary_view_scope import UptimeSummaryViewScope, check_uptime_summary_view_scope
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.results_monitor_ref_view import ResultsMonitorRefView
    from ..models.uptime_check_counts import UptimeCheckCounts
    from ..models.uptime_incident_counts import UptimeIncidentCounts
    from ..models.uptime_maintenance_seconds import UptimeMaintenanceSeconds
    from ..models.uptime_summary_view_metrics_type_0 import UptimeSummaryViewMetricsType0


T = TypeVar("T", bound="UptimeSummaryView")


@_attrs_define
class UptimeSummaryView:
    from_: int
    """ Bucket start (== the request's `from` when `bucket=none`). Unix seconds. """
    to: int
    """ Bucket end (== the request's `to` when `bucket=none`). Unix seconds. """
    up_sec: int
    """ Seconds the monitor was UP inside the bucket, maintenance included. Maintenance is not carved out of this
    figure: a monitor that answered normally during a scheduled window really was up, and the part of this number
    that fell inside a window is published separately as `maintenance.upSec`. Subtract that member to get up-time
    outside maintenance. """
    down_sec: int
    """ Seconds the monitor was DOWN inside the bucket, maintenance included. The part of it that fell inside a
    maintenance window is published separately as `maintenance.downSec`, and that part alone is what the uptime
    figure excuses. Subtract it to get down-time the monitor is answerable for. """
    total_sec: int
    """ Seconds of the bucket the monitor has a recorded state for - `upSec + downSec`. It is normally the bucket's
    own length, and is SHORTER when the monitor did not exist, was paused, or has no stored history for part of the
    bucket. That distinction is what makes an uptime figure computed from these members honest: the denominator is
    measured time, never wall-clock time. """
    down_spans: int
    """ Down spans intersecting the bucket. """
    monitor_id: None | Unset | UUID = UNSET
    """ The monitor this row measures. Absent on an account roll-up row, which measures the whole selection rather
    than one monitor. """
    monitor: None | ResultsMonitorRefView | Unset = UNSET
    maintenance: UptimeMaintenanceSeconds | Unset = UNSET
    """ How much of a bucket fell inside a maintenance window, split by what the monitor was doing at the time. This
    replaced a single `maintenanceSec` total, which could not answer the question the figure exists for. Only the
    part of a window that overlapped real DOWNTIME is excused from the uptime figure - a window scheduled while the
    monitor was answering normally excuses nothing - so one combined number left a client unable to reproduce, or
    even sanity-check, the percentage beside it. """
    checks: UptimeCheckCounts | Unset = UNSET
    """ The checks recorded in a bucket, split by outcome and by whether they ran inside a maintenance window. The
    four splits are disjoint and add up to the total. """
    uptime_percent: float | None | Unset = UNSET
    """ Uptime for the bucket, percent - `upSec / (totalSec - maintenance.downSec)`, so downtime inside a
    maintenance window is excused and up-time inside one still counts. Null when nothing was measured. **Read this
    member rather than recomputing it.** It is the figure the product itself reports, and on the whole-window
    aggregate it comes from the stored daily statistics rather than from the seconds beside it, which are derived
    from the state spans - the two agree to within rounding, but the stored answer is the authoritative one. A
    client that divides the seconds itself will drift from every other surface the moment either source is refined.
    """
    sla_target: float | None | Unset = UNSET
    """ The monitor's OWN target, or the request-level `sla=` override. On an account roll-up it is present only
    when the request named one, because the monitors in the roll-up may each carry a different target and there is
    no meaningful average of targets. """
    sla_met: bool | None | Unset = UNSET
    """ Whether the uptime percentage met the target. Absent when no target applies. """
    error_budget_sec_remaining: int | None | Unset = UNSET
    """ Seconds of downtime still affordable inside the bucket before the target is missed. Negative ⇒ overspent.
    """
    incidents: None | Unset | UptimeIncidentCounts = UNSET
    """ `expand=incidentCounts` - how many episodes opened and closed inside the bucket. """
    metrics: None | Unset | UptimeSummaryViewMetricsType0 = UNSET
    """ `metrics=responseTime,dns,…` - one series per requested metric, each point `{t, value, p95, samples}`. Typed
    objects, not untyped number pairs. """
    monitors: int | None | Unset = UNSET
    """ How many monitors this row aggregates. Present only on an account roll-up, where it is the answer to "over
    how many monitors". """
    scope: UptimeSummaryViewScope | Unset = UNSET
    """ What the roll-up covered: `account` when the request named no monitors and the row therefore spans the whole
    account, `selection` when it spans only the monitors the request named. Present only on an account roll-up. """
    sampled: bool | None | Unset = UNSET
    """ True when the timing metrics on this row were computed from a bounded sample rather than from every check in
    the bucket - so a client can label the chart honestly. The uptime and second figures are never sampled. Present
    only on an account roll-up. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.results_monitor_ref_view import ResultsMonitorRefView
        from ..models.uptime_incident_counts import UptimeIncidentCounts
        from ..models.uptime_summary_view_metrics_type_0 import UptimeSummaryViewMetricsType0

        from_ = self.from_

        to = self.to

        up_sec = self.up_sec

        down_sec = self.down_sec

        total_sec = self.total_sec

        down_spans = self.down_spans

        monitor_id: None | str | Unset
        if isinstance(self.monitor_id, Unset):
            monitor_id = UNSET
        elif isinstance(self.monitor_id, UUID):
            monitor_id = str(self.monitor_id)
        else:
            monitor_id = self.monitor_id

        monitor: dict[str, Any] | None | Unset
        if isinstance(self.monitor, Unset):
            monitor = UNSET
        elif isinstance(self.monitor, ResultsMonitorRefView):
            monitor = self.monitor.to_dict()
        else:
            monitor = self.monitor

        maintenance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.maintenance, Unset):
            maintenance = self.maintenance.to_dict()

        checks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.checks, Unset):
            checks = self.checks.to_dict()

        uptime_percent: float | None | Unset
        if isinstance(self.uptime_percent, Unset):
            uptime_percent = UNSET
        else:
            uptime_percent = self.uptime_percent

        sla_target: float | None | Unset
        if isinstance(self.sla_target, Unset):
            sla_target = UNSET
        else:
            sla_target = self.sla_target

        sla_met: bool | None | Unset
        if isinstance(self.sla_met, Unset):
            sla_met = UNSET
        else:
            sla_met = self.sla_met

        error_budget_sec_remaining: int | None | Unset
        if isinstance(self.error_budget_sec_remaining, Unset):
            error_budget_sec_remaining = UNSET
        else:
            error_budget_sec_remaining = self.error_budget_sec_remaining

        incidents: dict[str, Any] | None | Unset
        if isinstance(self.incidents, Unset):
            incidents = UNSET
        elif isinstance(self.incidents, UptimeIncidentCounts):
            incidents = self.incidents.to_dict()
        else:
            incidents = self.incidents

        metrics: dict[str, Any] | None | Unset
        if isinstance(self.metrics, Unset):
            metrics = UNSET
        elif isinstance(self.metrics, UptimeSummaryViewMetricsType0):
            metrics = self.metrics.to_dict()
        else:
            metrics = self.metrics

        monitors: int | None | Unset
        if isinstance(self.monitors, Unset):
            monitors = UNSET
        else:
            monitors = self.monitors

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

        sampled: bool | None | Unset
        if isinstance(self.sampled, Unset):
            sampled = UNSET
        else:
            sampled = self.sampled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
                "upSec": up_sec,
                "downSec": down_sec,
                "totalSec": total_sec,
                "downSpans": down_spans,
            }
        )
        if monitor_id is not UNSET:
            field_dict["monitorId"] = monitor_id
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if maintenance is not UNSET:
            field_dict["maintenance"] = maintenance
        if checks is not UNSET:
            field_dict["checks"] = checks
        if uptime_percent is not UNSET:
            field_dict["uptimePercent"] = uptime_percent
        if sla_target is not UNSET:
            field_dict["slaTarget"] = sla_target
        if sla_met is not UNSET:
            field_dict["slaMet"] = sla_met
        if error_budget_sec_remaining is not UNSET:
            field_dict["errorBudgetSecRemaining"] = error_budget_sec_remaining
        if incidents is not UNSET:
            field_dict["incidents"] = incidents
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if monitors is not UNSET:
            field_dict["monitors"] = monitors
        if scope is not UNSET:
            field_dict["scope"] = scope
        if sampled is not UNSET:
            field_dict["sampled"] = sampled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.results_monitor_ref_view import ResultsMonitorRefView
        from ..models.uptime_check_counts import UptimeCheckCounts
        from ..models.uptime_incident_counts import UptimeIncidentCounts
        from ..models.uptime_maintenance_seconds import UptimeMaintenanceSeconds
        from ..models.uptime_summary_view_metrics_type_0 import UptimeSummaryViewMetricsType0

        d = dict(src_dict)
        from_ = d.pop("from")

        to = d.pop("to")

        up_sec = d.pop("upSec")

        down_sec = d.pop("downSec")

        total_sec = d.pop("totalSec")

        down_spans = d.pop("downSpans")

        def _parse_monitor_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                monitor_id_type_0 = UUID(data)

                return monitor_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        monitor_id = _parse_monitor_id(d.pop("monitorId", UNSET))

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

        _maintenance = d.pop("maintenance", UNSET)
        maintenance: UptimeMaintenanceSeconds | Unset
        if isinstance(_maintenance, Unset):
            maintenance = UNSET
        else:
            maintenance = UptimeMaintenanceSeconds.from_dict(_maintenance)

        _checks = d.pop("checks", UNSET)
        checks: UptimeCheckCounts | Unset
        if isinstance(_checks, Unset):
            checks = UNSET
        else:
            checks = UptimeCheckCounts.from_dict(_checks)

        def _parse_uptime_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        uptime_percent = _parse_uptime_percent(d.pop("uptimePercent", UNSET))

        def _parse_sla_target(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sla_target = _parse_sla_target(d.pop("slaTarget", UNSET))

        def _parse_sla_met(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sla_met = _parse_sla_met(d.pop("slaMet", UNSET))

        def _parse_error_budget_sec_remaining(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        error_budget_sec_remaining = _parse_error_budget_sec_remaining(d.pop("errorBudgetSecRemaining", UNSET))

        def _parse_incidents(data: object) -> None | Unset | UptimeIncidentCounts:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                incidents_type_0 = UptimeIncidentCounts.from_dict(data)

                return incidents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UptimeIncidentCounts, data)

        incidents = _parse_incidents(d.pop("incidents", UNSET))

        def _parse_metrics(data: object) -> None | Unset | UptimeSummaryViewMetricsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metrics_type_0 = UptimeSummaryViewMetricsType0.from_dict(data)

                return metrics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UptimeSummaryViewMetricsType0, data)

        metrics = _parse_metrics(d.pop("metrics", UNSET))

        def _parse_monitors(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        monitors = _parse_monitors(d.pop("monitors", UNSET))

        _scope = d.pop("scope", UNSET)
        scope: UptimeSummaryViewScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = check_uptime_summary_view_scope(_scope)

        def _parse_sampled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sampled = _parse_sampled(d.pop("sampled", UNSET))

        uptime_summary_view = cls(
            from_=from_,
            to=to,
            up_sec=up_sec,
            down_sec=down_sec,
            total_sec=total_sec,
            down_spans=down_spans,
            monitor_id=monitor_id,
            monitor=monitor,
            maintenance=maintenance,
            checks=checks,
            uptime_percent=uptime_percent,
            sla_target=sla_target,
            sla_met=sla_met,
            error_budget_sec_remaining=error_budget_sec_remaining,
            incidents=incidents,
            metrics=metrics,
            monitors=monitors,
            scope=scope,
            sampled=sampled,
        )

        uptime_summary_view.additional_properties = d
        return uptime_summary_view

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
