from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.webhook_monitor_alert_state import WebhookMonitorAlertState, check_webhook_monitor_alert_state
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_error_ref import WebhookErrorRef
    from ..models.webhook_monitor_alert_recheck import WebhookMonitorAlertRecheck
    from ..models.webhook_monitor_ref import WebhookMonitorRef


T = TypeVar("T", bound="WebhookMonitorAlert")


@_attrs_define
class WebhookMonitorAlert:
    """An alert-grade state transition: the monitor, what happened, and the recheck constellation behind it."""

    monitor: WebhookMonitorRef
    """ The monitor, in the same identifying projection every v2 read renders: id, name, url and type. """
    state: WebhookMonitorAlertState
    """ `up` or `down` - the monitor's state as of this alert. Both `monitor.down` and `monitor.repeatedlyDown`
    carry `down`. """
    occurred_at: int
    """ When the alert was decided. Unix seconds. """
    recheck: list[WebhookMonitorAlertRecheck]
    """ What each location saw during the recheck that confirmed or refuted the failure. Empty on
    `monitor.repeatedlyDown`. """
    check_number: int | Unset = UNSET
    """ The check's number within the monitor's series. Absent when the engine could not supply one. """
    error: WebhookErrorRef | Unset = UNSET
    """ A failed check's error, typed the same way the results feed types it. """
    failed_at: int | Unset = UNSET
    """ When the failing check ran. `monitor.down` only. Unix seconds. """
    first_failed_at: int | Unset = UNSET
    """ When the outage began. `monitor.up` and `monitor.repeatedlyDown` only. Unix seconds. """
    last_failed_at: int | Unset = UNSET
    """ The last failing check of the outage. `monitor.up` and `monitor.repeatedlyDown` only. Unix seconds. """
    failed_checks: int | Unset = UNSET
    """ How many checks failed during the outage. `monitor.up` and `monitor.repeatedlyDown` only. """
    downtime_sec: int | Unset = UNSET
    """ How long the outage lasted, in seconds. """

    def to_dict(self) -> dict[str, Any]:
        monitor = self.monitor.to_dict()

        state: str = self.state

        occurred_at = self.occurred_at

        recheck = []
        for recheck_item_data in self.recheck:
            recheck_item = recheck_item_data.to_dict()
            recheck.append(recheck_item)

        check_number = self.check_number

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        failed_at = self.failed_at

        first_failed_at = self.first_failed_at

        last_failed_at = self.last_failed_at

        failed_checks = self.failed_checks

        downtime_sec = self.downtime_sec

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "monitor": monitor,
                "state": state,
                "occurredAt": occurred_at,
                "recheck": recheck,
            }
        )
        if check_number is not UNSET:
            field_dict["checkNumber"] = check_number
        if error is not UNSET:
            field_dict["error"] = error
        if failed_at is not UNSET:
            field_dict["failedAt"] = failed_at
        if first_failed_at is not UNSET:
            field_dict["firstFailedAt"] = first_failed_at
        if last_failed_at is not UNSET:
            field_dict["lastFailedAt"] = last_failed_at
        if failed_checks is not UNSET:
            field_dict["failedChecks"] = failed_checks
        if downtime_sec is not UNSET:
            field_dict["downtimeSec"] = downtime_sec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_error_ref import WebhookErrorRef
        from ..models.webhook_monitor_alert_recheck import WebhookMonitorAlertRecheck
        from ..models.webhook_monitor_ref import WebhookMonitorRef

        d = dict(src_dict)
        monitor = WebhookMonitorRef.from_dict(d.pop("monitor"))

        state = check_webhook_monitor_alert_state(d.pop("state"))

        occurred_at = d.pop("occurredAt")

        recheck = []
        _recheck = d.pop("recheck")
        for recheck_item_data in _recheck:
            recheck_item = WebhookMonitorAlertRecheck.from_dict(recheck_item_data)

            recheck.append(recheck_item)

        check_number = d.pop("checkNumber", UNSET)

        _error = d.pop("error", UNSET)
        error: WebhookErrorRef | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = WebhookErrorRef.from_dict(_error)

        failed_at = d.pop("failedAt", UNSET)

        first_failed_at = d.pop("firstFailedAt", UNSET)

        last_failed_at = d.pop("lastFailedAt", UNSET)

        failed_checks = d.pop("failedChecks", UNSET)

        downtime_sec = d.pop("downtimeSec", UNSET)

        webhook_monitor_alert = cls(
            monitor=monitor,
            state=state,
            occurred_at=occurred_at,
            recheck=recheck,
            check_number=check_number,
            error=error,
            failed_at=failed_at,
            first_failed_at=first_failed_at,
            last_failed_at=last_failed_at,
            failed_checks=failed_checks,
            downtime_sec=downtime_sec,
        )

        return webhook_monitor_alert
