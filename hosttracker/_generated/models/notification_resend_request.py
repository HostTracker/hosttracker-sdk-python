from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.notification_resend_request_frequency import (
    NotificationResendRequestFrequency,
    check_notification_resend_request_frequency,
)

T = TypeVar("T", bound="NotificationResendRequest")


@_attrs_define
class NotificationResendRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    at: int
    """ Any instant inside the period to resend, Unix seconds. Within the last three years. """
    frequency: NotificationResendRequestFrequency
    """ How often a scheduled delivery happens. """

    def to_dict(self) -> dict[str, Any]:
        at = self.at

        frequency: str = self.frequency

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
                "frequency": frequency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        at = d.pop("at")

        frequency = check_notification_resend_request_frequency(d.pop("frequency"))

        notification_resend_request = cls(
            at=at,
            frequency=frequency,
        )

        return notification_resend_request
