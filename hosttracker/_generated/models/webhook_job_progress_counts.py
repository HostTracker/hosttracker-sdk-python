from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebhookJobProgressCounts")


@_attrs_define
class WebhookJobProgressCounts:
    """How far an async job has got."""

    done: int
    """ Items concluded so far. """
    total: int
    """ Items in the job. """

    def to_dict(self) -> dict[str, Any]:
        done = self.done

        total = self.total

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "done": done,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        done = d.pop("done")

        total = d.pop("total")

        webhook_job_progress_counts = cls(
            done=done,
            total=total,
        )

        return webhook_job_progress_counts
