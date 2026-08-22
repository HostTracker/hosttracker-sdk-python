from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_view_state import JobViewState, check_job_view_state
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_item_view import JobItemView
    from ..models.job_progress_view import JobProgressView
    from ..models.job_summary_view import JobSummaryView
    from ..models.job_view_error_type_0 import JobViewErrorType0
    from ..models.job_view_result_summary_type_0 import JobViewResultSummaryType0


T = TypeVar("T", bound="JobView")


@_attrs_define
class JobView:
    id: UUID
    cancel_requested: bool
    created: int
    """ Unix seconds. """
    expires_at: int
    """ When the job stops being readable. Unix seconds. """
    resumed_count: int
    """ How many times this job has been resumed. Always present (`0` for the common case): the other half of the
    auto-resume guardrail is a cap on this number, and a member that appears only sometimes is one a client forgets
    to handle. """
    has_more: bool
    kind: str | Unset = UNSET
    """ The operation this job performs, e.g. `monitor.bulkCreate`. """
    scope: str | Unset = UNSET
    """ The domain scope that created it - the scope a reader must also hold. """
    state: JobViewState | Unset = UNSET
    """ Where the job is in its lifecycle. `queued` and `running` are live - keep polling; `succeeded`, `partial`,
    `failed` and `cancelled` are terminal, and the job will not change again. `partial` means the batch ran to the
    end with some items failed, so read `summary` and the per-item `results` rather than treating it as a whole-job
    failure. """
    progress: JobProgressView | Unset = UNSET
    summary: JobSummaryView | Unset = UNSET
    started_at: int | None | Unset = UNSET
    """ Unix seconds. """
    finished_at: int | None | Unset = UNSET
    """ Unix seconds. """
    error: JobViewErrorType0 | None | Unset = UNSET
    """ An RFC 9457 problem OBJECT when the job itself faulted - the same shape a synchronous failure would have
    returned. Absent otherwise. """
    result_summary: JobViewResultSummaryType0 | None | Unset = UNSET
    """ Job-level extras the kind produced (e.g. a report download url). Absent when there are none. """
    interrupted_at: int | None | Unset = UNSET
    """ When the job was last INTERRUPTED - a host restart or a hard death the janitor found. Absent for a job that
    never was. Published because it is what a client's auto-resume guardrail measures: resume silently only while
    the interruption is recent (an old job springing back to life is the real surprise), and show the card
    otherwise. Unix seconds. """
    results: list[JobItemView] | Unset = UNSET
    """ This page of per-item results, in `itemIndex` order. """
    next_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.job_view_error_type_0 import JobViewErrorType0
        from ..models.job_view_result_summary_type_0 import JobViewResultSummaryType0

        id = str(self.id)

        cancel_requested = self.cancel_requested

        created = self.created

        expires_at = self.expires_at

        resumed_count = self.resumed_count

        has_more = self.has_more

        kind = self.kind

        scope = self.scope

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress.to_dict()

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        started_at: int | None | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        finished_at: int | None | Unset
        if isinstance(self.finished_at, Unset):
            finished_at = UNSET
        else:
            finished_at = self.finished_at

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, JobViewErrorType0):
            error = self.error.to_dict()
        else:
            error = self.error

        result_summary: dict[str, Any] | None | Unset
        if isinstance(self.result_summary, Unset):
            result_summary = UNSET
        elif isinstance(self.result_summary, JobViewResultSummaryType0):
            result_summary = self.result_summary.to_dict()
        else:
            result_summary = self.result_summary

        interrupted_at: int | None | Unset
        if isinstance(self.interrupted_at, Unset):
            interrupted_at = UNSET
        else:
            interrupted_at = self.interrupted_at

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "cancelRequested": cancel_requested,
                "created": created,
                "expiresAt": expires_at,
                "resumedCount": resumed_count,
                "hasMore": has_more,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if scope is not UNSET:
            field_dict["scope"] = scope
        if state is not UNSET:
            field_dict["state"] = state
        if progress is not UNSET:
            field_dict["progress"] = progress
        if summary is not UNSET:
            field_dict["summary"] = summary
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at
        if error is not UNSET:
            field_dict["error"] = error
        if result_summary is not UNSET:
            field_dict["resultSummary"] = result_summary
        if interrupted_at is not UNSET:
            field_dict["interruptedAt"] = interrupted_at
        if results is not UNSET:
            field_dict["results"] = results
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_item_view import JobItemView
        from ..models.job_progress_view import JobProgressView
        from ..models.job_summary_view import JobSummaryView
        from ..models.job_view_error_type_0 import JobViewErrorType0
        from ..models.job_view_result_summary_type_0 import JobViewResultSummaryType0

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        cancel_requested = d.pop("cancelRequested")

        created = d.pop("created")

        expires_at = d.pop("expiresAt")

        resumed_count = d.pop("resumedCount")

        has_more = d.pop("hasMore")

        kind = d.pop("kind", UNSET)

        scope = d.pop("scope", UNSET)

        _state = d.pop("state", UNSET)
        state: JobViewState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_job_view_state(_state)

        _progress = d.pop("progress", UNSET)
        progress: JobProgressView | Unset
        if isinstance(_progress, Unset):
            progress = UNSET
        else:
            progress = JobProgressView.from_dict(_progress)

        _summary = d.pop("summary", UNSET)
        summary: JobSummaryView | Unset
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = JobSummaryView.from_dict(_summary)

        def _parse_started_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        started_at = _parse_started_at(d.pop("startedAt", UNSET))

        def _parse_finished_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        finished_at = _parse_finished_at(d.pop("finishedAt", UNSET))

        def _parse_error(data: object) -> JobViewErrorType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = JobViewErrorType0.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobViewErrorType0 | None | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_result_summary(data: object) -> JobViewResultSummaryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_summary_type_0 = JobViewResultSummaryType0.from_dict(data)

                return result_summary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobViewResultSummaryType0 | None | Unset, data)

        result_summary = _parse_result_summary(d.pop("resultSummary", UNSET))

        def _parse_interrupted_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        interrupted_at = _parse_interrupted_at(d.pop("interruptedAt", UNSET))

        _results = d.pop("results", UNSET)
        results: list[JobItemView] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = JobItemView.from_dict(results_item_data)

                results.append(results_item)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        job_view = cls(
            id=id,
            cancel_requested=cancel_requested,
            created=created,
            expires_at=expires_at,
            resumed_count=resumed_count,
            has_more=has_more,
            kind=kind,
            scope=scope,
            state=state,
            progress=progress,
            summary=summary,
            started_at=started_at,
            finished_at=finished_at,
            error=error,
            result_summary=result_summary,
            interrupted_at=interrupted_at,
            results=results,
            next_cursor=next_cursor,
        )

        job_view.additional_properties = d
        return job_view

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
