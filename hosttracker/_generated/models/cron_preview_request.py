from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CronPreviewRequest")


@_attrs_define
class CronPreviewRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    cron_schedule: str
    """ The cron expression to check - standard 5-field, or 6-field with seconds. Required, and a blank string is
    refused: there would be no schedule to judge. """

    def to_dict(self) -> dict[str, Any]:
        cron_schedule = self.cron_schedule

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cronSchedule": cron_schedule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cron_schedule = d.pop("cronSchedule")

        cron_preview_request = cls(
            cron_schedule=cron_schedule,
        )

        return cron_preview_request
