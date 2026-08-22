from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactDefaultSubscriptions")


@_attrs_define
class ContactDefaultSubscriptions:
    """Wire this contact to every monitor the account has, without listing them."""

    alerts: bool | Unset = UNSET
    """ Subscribe it to alerts on all monitors. """
    reports: bool | Unset = UNSET
    """ Subscribe it to reports on all monitors. """

    def to_dict(self) -> dict[str, Any]:
        alerts = self.alerts

        reports = self.reports

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if alerts is not UNSET:
            field_dict["alerts"] = alerts
        if reports is not UNSET:
            field_dict["reports"] = reports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alerts = d.pop("alerts", UNSET)

        reports = d.pop("reports", UNSET)

        contact_default_subscriptions = cls(
            alerts=alerts,
            reports=reports,
        )

        return contact_default_subscriptions
