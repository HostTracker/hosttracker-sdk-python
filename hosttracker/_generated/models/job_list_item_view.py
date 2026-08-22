from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_list_item_view_state import JobListItemViewState, check_job_list_item_view_state
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_progress_view import JobProgressView
    from ..models.job_summary_view import JobSummaryView


T = TypeVar("T", bound="JobListItemView")


@_attrs_define
class JobListItemView:
    """**X1b's row** - one job in `GET /job`, WITHOUT `results[]`. **Why the list is lean.** A page of 50 jobs carrying 50
    first-pages of receipts would be the most expensive read on the surface, and it would answer a question the list is
    not for: the list exists to FIND a job (the lost-jobId gap), and `GET /job/{id}` is where its receipts live.

    """

    id: UUID
    cancel_requested: bool
    created: int
    """ The job's own creation stamp - `created`, like every other resource's. Unix seconds. """
    expires_at: int
    """ Unix seconds. """
    resumed_count: int
    kind: str | Unset = UNSET
    scope: str | Unset = UNSET
    state: JobListItemViewState | Unset = UNSET
    progress: JobProgressView | Unset = UNSET
    summary: JobSummaryView | Unset = UNSET
    started_at: int | None | Unset = UNSET
    """ Unix seconds. """
    finished_at: int | None | Unset = UNSET
    """ Unix seconds. """
    interrupted_at: int | None | Unset = UNSET
    """ Unix seconds. """
    results_url: str | Unset = UNSET
    """ Where this job's full representation - including `results[]` - is read. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        cancel_requested = self.cancel_requested

        created = self.created

        expires_at = self.expires_at

        resumed_count = self.resumed_count

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

        interrupted_at: int | None | Unset
        if isinstance(self.interrupted_at, Unset):
            interrupted_at = UNSET
        else:
            interrupted_at = self.interrupted_at

        results_url = self.results_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "cancelRequested": cancel_requested,
                "created": created,
                "expiresAt": expires_at,
                "resumedCount": resumed_count,
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
        if interrupted_at is not UNSET:
            field_dict["interruptedAt"] = interrupted_at
        if results_url is not UNSET:
            field_dict["resultsUrl"] = results_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_progress_view import JobProgressView
        from ..models.job_summary_view import JobSummaryView

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        cancel_requested = d.pop("cancelRequested")

        created = d.pop("created")

        expires_at = d.pop("expiresAt")

        resumed_count = d.pop("resumedCount")

        kind = d.pop("kind", UNSET)

        scope = d.pop("scope", UNSET)

        _state = d.pop("state", UNSET)
        state: JobListItemViewState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_job_list_item_view_state(_state)

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

        def _parse_interrupted_at(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        interrupted_at = _parse_interrupted_at(d.pop("interruptedAt", UNSET))

        results_url = d.pop("resultsUrl", UNSET)

        job_list_item_view = cls(
            id=id,
            cancel_requested=cancel_requested,
            created=created,
            expires_at=expires_at,
            resumed_count=resumed_count,
            kind=kind,
            scope=scope,
            state=state,
            progress=progress,
            summary=summary,
            started_at=started_at,
            finished_at=finished_at,
            interrupted_at=interrupted_at,
            results_url=results_url,
        )

        job_list_item_view.additional_properties = d
        return job_list_item_view

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
