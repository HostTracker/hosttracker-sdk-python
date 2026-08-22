from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.monitor_subscription_view_alert_type import (
    MonitorSubscriptionViewAlertType,
    check_monitor_subscription_view_alert_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_contact_ref_view import MonitorContactRefView


T = TypeVar("T", bound="MonitorSubscriptionView")


@_attrs_define
class MonitorSubscriptionView:
    """One alert subscription, carrying the minimal identifying projection of BOTH sides."""

    alert_type: MonitorSubscriptionViewAlertType | Unset = UNSET
    """ `up` | `down` | `repeatedlyDown` - the event this subscription fires on. """
    contact: MonitorContactRefView | Unset = UNSET
    """ A contact's identifying projection - `{id, type, name, address}`, never a bare id. """
    created: int | None | Unset = UNSET
    """ Unix seconds. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_type: str | Unset = UNSET
        if not isinstance(self.alert_type, Unset):
            alert_type = self.alert_type

        contact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        created: int | None | Unset
        if isinstance(self.created, Unset):
            created = UNSET
        else:
            created = self.created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_type is not UNSET:
            field_dict["alertType"] = alert_type
        if contact is not UNSET:
            field_dict["contact"] = contact
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_contact_ref_view import MonitorContactRefView

        d = dict(src_dict)
        _alert_type = d.pop("alertType", UNSET)
        alert_type: MonitorSubscriptionViewAlertType | Unset
        if isinstance(_alert_type, Unset):
            alert_type = UNSET
        else:
            alert_type = check_monitor_subscription_view_alert_type(_alert_type)

        _contact = d.pop("contact", UNSET)
        contact: MonitorContactRefView | Unset
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = MonitorContactRefView.from_dict(_contact)

        def _parse_created(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        created = _parse_created(d.pop("created", UNSET))

        monitor_subscription_view = cls(
            alert_type=alert_type,
            contact=contact,
            created=created,
        )

        monitor_subscription_view.additional_properties = d
        return monitor_subscription_view

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
