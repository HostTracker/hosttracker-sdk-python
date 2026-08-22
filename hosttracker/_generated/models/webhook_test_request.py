from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookTestRequest")


@_attrs_define
class WebhookTestRequest:
    """Which event the test delivery should carry."""

    event: str | Unset = UNSET
    """ The event type to render. Defaults to a monitor-down event. """

    def to_dict(self) -> dict[str, Any]:
        event = self.event

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event = d.pop("event", UNSET)

        webhook_test_request = cls(
            event=event,
        )

        return webhook_test_request
