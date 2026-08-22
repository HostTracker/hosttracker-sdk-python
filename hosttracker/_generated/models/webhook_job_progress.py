from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webhook_job_progress_counts import WebhookJobProgressCounts
    from ..models.webhook_job_summary import WebhookJobSummary


T = TypeVar("T", bound="WebhookJobProgress")


@_attrs_define
class WebhookJobProgress:
    """A throttled interim report for a running job - counts only, no per-item receipts."""

    job_id: UUID
    """ The job's id - what GET /job/{id} takes. """
    kind: str
    """ What the job does (monitor.bulkCreate, contact.bulkWrite, …). """
    state: str
    """ queued or running - and the terminal word on the flush that concludes the job. """
    progress: WebhookJobProgressCounts
    """ How far an async job has got. """
    summary: WebhookJobSummary
    """ How much an async job changed - the same five counts GET /job/{id} publishes. """
    results_url: str
    """ Where to read every item's receipt, paged. """

    def to_dict(self) -> dict[str, Any]:
        job_id = str(self.job_id)

        kind = self.kind

        state = self.state

        progress = self.progress.to_dict()

        summary = self.summary.to_dict()

        results_url = self.results_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "jobId": job_id,
                "kind": kind,
                "state": state,
                "progress": progress,
                "summary": summary,
                "resultsUrl": results_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_job_progress_counts import WebhookJobProgressCounts
        from ..models.webhook_job_summary import WebhookJobSummary

        d = dict(src_dict)
        job_id = UUID(d.pop("jobId"))

        kind = d.pop("kind")

        state = d.pop("state")

        progress = WebhookJobProgressCounts.from_dict(d.pop("progress"))

        summary = WebhookJobSummary.from_dict(d.pop("summary"))

        results_url = d.pop("resultsUrl")

        webhook_job_progress = cls(
            job_id=job_id,
            kind=kind,
            state=state,
            progress=progress,
            summary=summary,
            results_url=results_url,
        )

        return webhook_job_progress
