from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.job_callback_on import JobCallbackOn, check_job_callback_on
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobCallback")


@_attrs_define
class JobCallback:
    """A webhook to call when the job finishes, carrying the terminal job document and its first page of results. Send null
    for none.

    """

    webhook_id: UUID | Unset = UNSET
    """ The registered, enabled webhook to call. An unknown, disabled or unowned id is refused at submit rather than
    dropped silently. """
    on: JobCallbackOn | Unset = UNSET
    """ Which deliveries to send. "completed" (the default) is the single terminal call; "progress" adds throttled
    interim reports while the job runs, and still ends with exactly one terminal call. """

    def to_dict(self) -> dict[str, Any]:
        webhook_id: str | Unset = UNSET
        if not isinstance(self.webhook_id, Unset):
            webhook_id = str(self.webhook_id)

        on: str | Unset = UNSET
        if not isinstance(self.on, Unset):
            on = self.on

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if webhook_id is not UNSET:
            field_dict["webhookId"] = webhook_id
        if on is not UNSET:
            field_dict["on"] = on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _webhook_id = d.pop("webhookId", UNSET)
        webhook_id: UUID | Unset
        if isinstance(_webhook_id, Unset):
            webhook_id = UNSET
        else:
            webhook_id = UUID(_webhook_id)

        _on = d.pop("on", UNSET)
        on: JobCallbackOn | Unset
        if isinstance(_on, Unset):
            on = UNSET
        else:
            on = check_job_callback_on(_on)

        job_callback = cls(
            webhook_id=webhook_id,
            on=on,
        )

        return job_callback
