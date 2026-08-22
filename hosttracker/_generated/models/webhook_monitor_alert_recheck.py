from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.webhook_monitor_alert_recheck_state import (
    WebhookMonitorAlertRecheckState,
    check_webhook_monitor_alert_recheck_state,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_error_ref import WebhookErrorRef
    from ..models.webhook_location_ref import WebhookLocationRef


T = TypeVar("T", bound="WebhookMonitorAlertRecheck")


@_attrs_define
class WebhookMonitorAlertRecheck:
    """One location's verdict during the recheck."""

    location: WebhookLocationRef
    """ A check location - the same members the results feed renders as `location`. """
    state: WebhookMonitorAlertRecheckState
    """ `up` or `down` - what THIS location saw. """
    error: WebhookErrorRef | Unset = UNSET
    """ A failed check's error, typed the same way the results feed types it. """

    def to_dict(self) -> dict[str, Any]:
        location = self.location.to_dict()

        state: str = self.state

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "location": location,
                "state": state,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_error_ref import WebhookErrorRef
        from ..models.webhook_location_ref import WebhookLocationRef

        d = dict(src_dict)
        location = WebhookLocationRef.from_dict(d.pop("location"))

        state = check_webhook_monitor_alert_recheck_state(d.pop("state"))

        _error = d.pop("error", UNSET)
        error: WebhookErrorRef | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = WebhookErrorRef.from_dict(_error)

        webhook_monitor_alert_recheck = cls(
            location=location,
            state=state,
            error=error,
        )

        return webhook_monitor_alert_recheck
