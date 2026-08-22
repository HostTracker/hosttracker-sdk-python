from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_event_view_kind import IncidentEventViewKind, check_incident_event_view_kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_view import LocationView
    from ..models.result_error_view import ResultErrorView
    from ..models.result_recheck_view import ResultRecheckView


T = TypeVar("T", bound="IncidentEventView")


@_attrs_define
class IncidentEventView:
    at: int
    """ Unix seconds. """
    check_number: int
    under_maintenance: bool
    result_id: str | Unset = UNSET
    kind: IncidentEventViewKind | Unset = UNSET
    """ `enter` (the monitor went down) | `exit` (it came back). """
    location: LocationView | None | Unset = UNSET
    """ A check location. Always the identifying projection, never a bare agent id. """
    error: None | ResultErrorView | Unset = UNSET
    """ The error taxonomy of a failed check - typed members, never a prose blob. """
    recheck: None | ResultRecheckView | Unset = UNSET
    """ The per-location verdicts of the recheck that confirmed (or refuted) this boundary. """
    assert_fails: list[str] | None | Unset = UNSET
    """ The assertion rules this check evaluated to a failure, each as the rule expression itself (`status eq 500`).
    Present only when the agent recorded any - a check that failed for a network or protocol reason has none, and an
    empty list is not published. The stored form is the rendered rule, not a decomposition of it: the executor
    records WHICH rows failed, and there is no per-row actual/expected pair behind them to publish. """
    assert_ev: list[str] | None | Unset = UNSET
    """ The per-row `obtained: ...` evidence, PARALLEL to `assertFails` (same order and length; an empty string
    where a row has nothing safe to say) - sanitized, capped, redaction-aware plain text the executor builds. """
    policy_violations: list[str] | None | Unset = UNSET
    """ The policy codes this check violated, as the executor recorded them (for example `https-not-enforced`).
    Present only when the monitor runs policies and any were violated. The codes are stored agent output rather than
    a vocabulary this API mints, so a code outside today's set is published as it stands instead of being dropped.
    """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.location_view import LocationView
        from ..models.result_error_view import ResultErrorView
        from ..models.result_recheck_view import ResultRecheckView

        at = self.at

        check_number = self.check_number

        under_maintenance = self.under_maintenance

        result_id = self.result_id

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

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
                "at": at,
                "checkNumber": check_number,
                "underMaintenance": under_maintenance,
            }
        )
        if result_id is not UNSET:
            field_dict["resultId"] = result_id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if location is not UNSET:
            field_dict["location"] = location
        if error is not UNSET:
            field_dict["error"] = error
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

        d = dict(src_dict)
        at = d.pop("at")

        check_number = d.pop("checkNumber")

        under_maintenance = d.pop("underMaintenance")

        result_id = d.pop("resultId", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: IncidentEventViewKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_incident_event_view_kind(_kind)

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

        incident_event_view = cls(
            at=at,
            check_number=check_number,
            under_maintenance=under_maintenance,
            result_id=result_id,
            kind=kind,
            location=location,
            error=error,
            recheck=recheck,
            assert_fails=assert_fails,
            assert_ev=assert_ev,
            policy_violations=policy_violations,
        )

        incident_event_view.additional_properties = d
        return incident_event_view

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
