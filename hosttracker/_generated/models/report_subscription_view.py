from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reports_contact_ref_view import ReportsContactRefView
    from ..models.results_monitor_ref_view import ResultsMonitorRefView


T = TypeVar("T", bound="ReportSubscriptionView")


@_attrs_define
class ReportSubscriptionView:
    overlimit: bool
    """ True when the account's package has this subscription over its limit - the row exists but is not delivered.
    Surfacing it is what makes "why did my report stop" answerable in one call. """
    monitor: ResultsMonitorRefView | Unset = UNSET
    contact: ReportsContactRefView | Unset = UNSET
    """ The identifying projection of a contact. """
    frequency: str | Unset = UNSET
    """ The frequency as a WORD (`daily`…`yearly`). """
    created: int | None | Unset = UNSET
    """ Unix seconds. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        overlimit = self.overlimit

        monitor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monitor, Unset):
            monitor = self.monitor.to_dict()

        contact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        frequency = self.frequency

        created: int | None | Unset
        if isinstance(self.created, Unset):
            created = UNSET
        else:
            created = self.created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "overlimit": overlimit,
            }
        )
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if contact is not UNSET:
            field_dict["contact"] = contact
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reports_contact_ref_view import ReportsContactRefView
        from ..models.results_monitor_ref_view import ResultsMonitorRefView

        d = dict(src_dict)
        overlimit = d.pop("overlimit")

        _monitor = d.pop("monitor", UNSET)
        monitor: ResultsMonitorRefView | Unset
        if isinstance(_monitor, Unset):
            monitor = UNSET
        else:
            monitor = ResultsMonitorRefView.from_dict(_monitor)

        _contact = d.pop("contact", UNSET)
        contact: ReportsContactRefView | Unset
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ReportsContactRefView.from_dict(_contact)

        frequency = d.pop("frequency", UNSET)

        def _parse_created(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        created = _parse_created(d.pop("created", UNSET))

        report_subscription_view = cls(
            overlimit=overlimit,
            monitor=monitor,
            contact=contact,
            frequency=frequency,
            created=created,
        )

        report_subscription_view.additional_properties = d
        return report_subscription_view

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
