from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cron_preview_view_reason import CronPreviewViewReason, check_cron_preview_view_reason
from ..types import UNSET, Unset

T = TypeVar("T", bound="CronPreviewView")


@_attrs_define
class CronPreviewView:
    """**The cron preview's answer.** `valid` is the verdict; `reason` says why not, and `next` shows the schedule the
    caller is about to save actually doing what they meant.

    """

    valid: bool
    """ True when a monitor write would accept this schedule for this account. """
    reason: CronPreviewViewReason | Unset = UNSET
    """ Why it would not be accepted. Omitted when it would. """
    next_: list[int] | Unset = UNSET
    """ The next few times the schedule fires, Unix seconds, soonest first - empty when it is not valid. The list is
    the half a caller cannot compute from a boolean: a cron expression that parses is still routinely not the one
    its author meant, and seeing the first five fires is what catches it. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        valid = self.valid

        reason: str | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason

        next_: list[int] | Unset = UNSET
        if not isinstance(self.next_, Unset):
            next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valid": valid,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        valid = d.pop("valid")

        _reason = d.pop("reason", UNSET)
        reason: CronPreviewViewReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = check_cron_preview_view_reason(_reason)

        next_ = cast(list[int], d.pop("next", UNSET))

        cron_preview_view = cls(
            valid=valid,
            reason=reason,
            next_=next_,
        )

        cron_preview_view.additional_properties = d
        return cron_preview_view

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
