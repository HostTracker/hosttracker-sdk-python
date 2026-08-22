from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.result_view_state import ResultViewState, check_result_view_state
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_view import LocationView
    from ..models.result_error_view import ResultErrorView
    from ..models.result_recheck_view import ResultRecheckView
    from ..models.result_view_metrics_type_0 import ResultViewMetricsType0
    from ..models.results_monitor_ref_view import ResultsMonitorRefView


T = TypeVar("T", bound="ResultView")


@_attrs_define
class ResultView:
    monitor_id: UUID
    at: int
    """ When the check STARTED. Unix seconds on the wire. Unix seconds. """
    duration_sec: int
    """ How long the check took, seconds. """
    check_number: int
    """ The check number within the monitor's series (the legacy `eventNumber`). """
    check_count: int
    """ How many raw checks this row aggregates (a quiet monitor stores runs of identical results as one row). """
    under_maintenance: bool
    """ True when the check ran inside a maintenance window - so a client never counts it as an outage. """
    has_snapshot: bool
    id: str | Unset = UNSET
    monitor: None | ResultsMonitorRefView | Unset = UNSET
    state: ResultViewState | Unset = UNSET
    location: LocationView | None | Unset = UNSET
    """ The agent that produced it - `location` in the request vocabulary. """
    error: None | ResultErrorView | Unset = UNSET
    """ The error taxonomy for a failed check; absent when `status:"up"`. """
    snapshot_url: None | str | Unset = UNSET
    metrics: None | ResultViewMetricsType0 | Unset = UNSET
    """ The decoded per-type measurements. Emitted as JSON, not as a quoted string - the stored blob is a JSON
    document and a client must not have to double-parse. """
    recheck: None | ResultRecheckView | Unset = UNSET
    """ The recheck constellation behind a confirmed failure: which locations disagreed and which confirmed, per
    error. """
    assert_fails: list[str] | None | Unset = UNSET
    """ The assertion rules this check evaluated to a definite failure, each as the rule expression itself (`status
    eq 500`, `body contains "marker"`). Carried only when `expand=metrics` is asked for: the values live inside the
    stored result document, which that expansion already decodes, so asking for them costs nothing extra and not
    asking keeps a result feed from unzipping a blob per row. Absent when the check recorded none. """
    assert_ev: list[str] | None | Unset = UNSET
    """ The per-row `obtained: ...` evidence, PARALLEL to `assertFails` (same order and length; an empty string
    where a row has nothing safe to say) - sanitized, capped, redaction-aware plain text built by the executor. Same
    expansion as its sibling (`expand=metrics`). """
    policy_violations: list[str] | None | Unset = UNSET
    """ The codes of the http policies this check violated. Carried under the same condition as the assertion list
    beside it - `expand=metrics`, whose decode already has the document open. Absent when the check recorded none.
    """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.location_view import LocationView
        from ..models.result_error_view import ResultErrorView
        from ..models.result_recheck_view import ResultRecheckView
        from ..models.result_view_metrics_type_0 import ResultViewMetricsType0
        from ..models.results_monitor_ref_view import ResultsMonitorRefView

        monitor_id = str(self.monitor_id)

        at = self.at

        duration_sec = self.duration_sec

        check_number = self.check_number

        check_count = self.check_count

        under_maintenance = self.under_maintenance

        has_snapshot = self.has_snapshot

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

        location: dict[str, Any] | None | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, LocationView):
            location = self.location.to_dict()
        else:
            location = self.location

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, ResultErrorView):
            error = self.error.to_dict()
        else:
            error = self.error

        snapshot_url: None | str | Unset
        if isinstance(self.snapshot_url, Unset):
            snapshot_url = UNSET
        else:
            snapshot_url = self.snapshot_url

        metrics: dict[str, Any] | None | Unset
        if isinstance(self.metrics, Unset):
            metrics = UNSET
        elif isinstance(self.metrics, ResultViewMetricsType0):
            metrics = self.metrics.to_dict()
        else:
            metrics = self.metrics

        recheck: dict[str, Any] | None | Unset
        if isinstance(self.recheck, Unset):
            recheck = UNSET
        elif isinstance(self.recheck, ResultRecheckView):
            recheck = self.recheck.to_dict()
        else:
            recheck = self.recheck

        assert_fails: list[str] | None | Unset
        if isinstance(self.assert_fails, Unset):
            assert_fails = UNSET
        elif isinstance(self.assert_fails, list):
            assert_fails = self.assert_fails

        else:
            assert_fails = self.assert_fails

        assert_ev: list[str] | None | Unset
        if isinstance(self.assert_ev, Unset):
            assert_ev = UNSET
        elif isinstance(self.assert_ev, list):
            assert_ev = self.assert_ev

        else:
            assert_ev = self.assert_ev

        policy_violations: list[str] | None | Unset
        if isinstance(self.policy_violations, Unset):
            policy_violations = UNSET
        elif isinstance(self.policy_violations, list):
            policy_violations = self.policy_violations

        else:
            policy_violations = self.policy_violations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "monitorId": monitor_id,
                "at": at,
                "durationSec": duration_sec,
                "checkNumber": check_number,
                "checkCount": check_count,
                "underMaintenance": under_maintenance,
                "hasSnapshot": has_snapshot,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if state is not UNSET:
            field_dict["state"] = state
        if location is not UNSET:
            field_dict["location"] = location
        if error is not UNSET:
            field_dict["error"] = error
        if snapshot_url is not UNSET:
            field_dict["snapshotUrl"] = snapshot_url
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if recheck is not UNSET:
            field_dict["recheck"] = recheck
        if assert_fails is not UNSET:
            field_dict["assertFails"] = assert_fails
        if assert_ev is not UNSET:
            field_dict["assertEv"] = assert_ev
        if policy_violations is not UNSET:
            field_dict["policyViolations"] = policy_violations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_view import LocationView
        from ..models.result_error_view import ResultErrorView
        from ..models.result_recheck_view import ResultRecheckView
        from ..models.result_view_metrics_type_0 import ResultViewMetricsType0
        from ..models.results_monitor_ref_view import ResultsMonitorRefView

        d = dict(src_dict)
        monitor_id = UUID(d.pop("monitorId"))

        at = d.pop("at")

        duration_sec = d.pop("durationSec")

        check_number = d.pop("checkNumber")

        check_count = d.pop("checkCount")

        under_maintenance = d.pop("underMaintenance")

        has_snapshot = d.pop("hasSnapshot")

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
        state: ResultViewState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_result_view_state(_state)

        def _parse_location(data: object) -> LocationView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = LocationView.from_dict(data)

                return location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LocationView | None | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_error(data: object) -> None | ResultErrorView | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = ResultErrorView.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResultErrorView | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_snapshot_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        snapshot_url = _parse_snapshot_url(d.pop("snapshotUrl", UNSET))

        def _parse_metrics(data: object) -> None | ResultViewMetricsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metrics_type_0 = ResultViewMetricsType0.from_dict(data)

                return metrics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResultViewMetricsType0 | Unset, data)

        metrics = _parse_metrics(d.pop("metrics", UNSET))

        def _parse_recheck(data: object) -> None | ResultRecheckView | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                recheck_type_0 = ResultRecheckView.from_dict(data)

                return recheck_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResultRecheckView | Unset, data)

        recheck = _parse_recheck(d.pop("recheck", UNSET))

        def _parse_assert_fails(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assert_fails_type_0 = cast(list[str], data)

                return assert_fails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        assert_fails = _parse_assert_fails(d.pop("assertFails", UNSET))

        def _parse_assert_ev(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assert_ev_type_0 = cast(list[str], data)

                return assert_ev_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        assert_ev = _parse_assert_ev(d.pop("assertEv", UNSET))

        def _parse_policy_violations(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                policy_violations_type_0 = cast(list[str], data)

                return policy_violations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        policy_violations = _parse_policy_violations(d.pop("policyViolations", UNSET))

        result_view = cls(
            monitor_id=monitor_id,
            at=at,
            duration_sec=duration_sec,
            check_number=check_number,
            check_count=check_count,
            under_maintenance=under_maintenance,
            has_snapshot=has_snapshot,
            id=id,
            monitor=monitor,
            state=state,
            location=location,
            error=error,
            snapshot_url=snapshot_url,
            metrics=metrics,
            recheck=recheck,
            assert_fails=assert_fails,
            assert_ev=assert_ev,
            policy_violations=policy_violations,
        )

        result_view.additional_properties = d
        return result_view

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
