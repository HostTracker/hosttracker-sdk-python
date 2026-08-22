from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebhookJobSummary")


@_attrs_define
class WebhookJobSummary:
    """How much an async job changed - the same five counts GET /job/{id} publishes."""

    created: int
    """ Items that created something. """
    updated: int
    """ Items that changed something. """
    skipped: int
    """ Items that needed no change. """
    failed: int
    """ Items that failed. """
    deleted: int
    """ Items that removed something. """

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        updated = self.updated

        skipped = self.skipped

        failed = self.failed

        deleted = self.deleted

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created": created,
                "updated": updated,
                "skipped": skipped,
                "failed": failed,
                "deleted": deleted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created")

        updated = d.pop("updated")

        skipped = d.pop("skipped")

        failed = d.pop("failed")

        deleted = d.pop("deleted")

        webhook_job_summary = cls(
            created=created,
            updated=updated,
            skipped=skipped,
            failed=failed,
            deleted=deleted,
        )

        return webhook_job_summary
