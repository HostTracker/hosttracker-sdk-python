from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_resend_receipt_frequency import (
    NotificationResendReceiptFrequency,
    check_notification_resend_receipt_frequency,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationResendReceipt")


@_attrs_define
class NotificationResendReceipt:
    accepted: bool
    """ Always true: the rebuild runs on the report service and the send follows. """
    at: int
    """ The period's instant, echoed back in Unix seconds. Unix seconds. """
    frequency: NotificationResendReceiptFrequency | Unset = UNSET
    """ The report schedule that will be rebuilt. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepted = self.accepted

        at = self.at

        frequency: str | Unset = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accepted": accepted,
                "at": at,
            }
        )
        if frequency is not UNSET:
            field_dict["frequency"] = frequency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accepted = d.pop("accepted")

        at = d.pop("at")

        _frequency = d.pop("frequency", UNSET)
        frequency: NotificationResendReceiptFrequency | Unset
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = check_notification_resend_receipt_frequency(_frequency)

        notification_resend_receipt = cls(
            accepted=accepted,
            at=at,
            frequency=frequency,
        )

        notification_resend_receipt.additional_properties = d
        return notification_resend_receipt

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
