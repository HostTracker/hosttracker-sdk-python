from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_job_progress_counts import WebhookJobProgressCounts
    from ..models.webhook_job_result import WebhookJobResult
    from ..models.webhook_job_summary import WebhookJobSummary


T = TypeVar("T", bound="WebhookJobCompleted")


@_attrs_define
class WebhookJobCompleted:
    """An async job reached a terminal state, with the first page of its per-item receipts."""

    job_id: UUID
    """ The job's id - what GET /job/{id} takes. """
    kind: str
    """ What the job does (monitor.bulkCreate, contact.bulkWrite, …). """
    state: str
    """ succeeded, partial, failed or cancelled - the same word the job read publishes. """
    summary: WebhookJobSummary
    """ How much an async job changed - the same five counts GET /job/{id} publishes. """
    progress: WebhookJobProgressCounts
    """ How far an async job has got. """
    results_url: str
    """ Where to read every item's receipt, paged. """
    results: list[WebhookJobResult]
    """ The first page of item receipts. """
    results_truncated: bool
    """ True when the job produced more receipts than this payload carries. """
    created: int | Unset = UNSET
    """ When the job was submitted. Unix seconds. """
    finished_at: int | Unset = UNSET
    """ When it concluded. Unix seconds. """
    error: str | Unset = UNSET
    """ Why the job as a whole failed. Absent when it did not. """

    def to_dict(self) -> dict[str, Any]:
        job_id = str(self.job_id)

        kind = self.kind

        state = self.state

        summary = self.summary.to_dict()

        progress = self.progress.to_dict()

        results_url = self.results_url

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        results_truncated = self.results_truncated

        created = self.created

        finished_at = self.finished_at

        error = self.error

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "jobId": job_id,
                "kind": kind,
                "state": state,
                "summary": summary,
                "progress": progress,
                "resultsUrl": results_url,
                "results": results,
                "resultsTruncated": results_truncated,
            }
        )
        if created is not UNSET:
            field_dict["created"] = created
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_job_progress_counts import WebhookJobProgressCounts
        from ..models.webhook_job_result import WebhookJobResult
        from ..models.webhook_job_summary import WebhookJobSummary

        d = dict(src_dict)
        job_id = UUID(d.pop("jobId"))

        kind = d.pop("kind")

        state = d.pop("state")

        summary = WebhookJobSummary.from_dict(d.pop("summary"))

        progress = WebhookJobProgressCounts.from_dict(d.pop("progress"))

        results_url = d.pop("resultsUrl")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = WebhookJobResult.from_dict(results_item_data)

            results.append(results_item)

        results_truncated = d.pop("resultsTruncated")

        created = d.pop("created", UNSET)

        finished_at = d.pop("finishedAt", UNSET)

        error = d.pop("error", UNSET)

        webhook_job_completed = cls(
            job_id=job_id,
            kind=kind,
            state=state,
            summary=summary,
            progress=progress,
            results_url=results_url,
            results=results,
            results_truncated=results_truncated,
            created=created,
            finished_at=finished_at,
            error=error,
        )

        return webhook_job_completed
