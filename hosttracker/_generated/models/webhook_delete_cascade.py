from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebhookDeleteCascade")


@_attrs_define
class WebhookDeleteCascade:
    """What went with the webhook."""

    alert_subscriptions: int
    """ The monitor bindings the scope had resolved to - one per monitor this webhook was addressed to
    (`api.WebhookMonitor`), and 0 for an `all`-scoped webhook, which is a FORM rather than a set of rows. """
    report_subscriptions: int
    """ Report subscriptions on the row. Structurally 0 for a webhook - reports are not deliverable to an `http`
    contact (`unsupported_report_channel`) - but reported rather than omitted, so the two doors' receipts carry the
    same members and an absent member never has to be interpreted. """
    pending_deliveries: int
    """ Deliveries still queued for retry, which are DROPPED by the delete. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_subscriptions = self.alert_subscriptions

        report_subscriptions = self.report_subscriptions

        pending_deliveries = self.pending_deliveries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alertSubscriptions": alert_subscriptions,
                "reportSubscriptions": report_subscriptions,
                "pendingDeliveries": pending_deliveries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alert_subscriptions = d.pop("alertSubscriptions")

        report_subscriptions = d.pop("reportSubscriptions")

        pending_deliveries = d.pop("pendingDeliveries")

        webhook_delete_cascade = cls(
            alert_subscriptions=alert_subscriptions,
            report_subscriptions=report_subscriptions,
            pending_deliveries=pending_deliveries,
        )

        webhook_delete_cascade.additional_properties = d
        return webhook_delete_cascade

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
