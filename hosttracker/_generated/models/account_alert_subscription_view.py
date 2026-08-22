from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contacts_contact_ref_view import ContactsContactRefView
    from ..models.contacts_monitor_ref_view import ContactsMonitorRefView


T = TypeVar("T", bound="AccountAlertSubscriptionView")


@_attrs_define
class AccountAlertSubscriptionView:
    """One row of the ACCOUNT-WIDE alert-subscription list: both parents identified, so the whole account's alert wiring is
    auditable in one read.

    """

    created: int
    """ Unix seconds. """
    id: str | Unset = UNSET
    monitor: ContactsMonitorRefView | Unset = UNSET
    """ The minimal identifying projection of a monitor, as embedded in relation reads. """
    contact: ContactsContactRefView | Unset = UNSET
    """ The minimal identifying projection of a contact, as embedded in relation reads. """
    alert_types: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        id = self.id

        monitor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monitor, Unset):
            monitor = self.monitor.to_dict()

        contact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        alert_types: list[str] | Unset = UNSET
        if not isinstance(self.alert_types, Unset):
            alert_types = self.alert_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if contact is not UNSET:
            field_dict["contact"] = contact
        if alert_types is not UNSET:
            field_dict["alertTypes"] = alert_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contacts_contact_ref_view import ContactsContactRefView
        from ..models.contacts_monitor_ref_view import ContactsMonitorRefView

        d = dict(src_dict)
        created = d.pop("created")

        id = d.pop("id", UNSET)

        _monitor = d.pop("monitor", UNSET)
        monitor: ContactsMonitorRefView | Unset
        if isinstance(_monitor, Unset):
            monitor = UNSET
        else:
            monitor = ContactsMonitorRefView.from_dict(_monitor)

        _contact = d.pop("contact", UNSET)
        contact: ContactsContactRefView | Unset
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ContactsContactRefView.from_dict(_contact)

        alert_types = cast(list[str], d.pop("alertTypes", UNSET))

        account_alert_subscription_view = cls(
            created=created,
            id=id,
            monitor=monitor,
            contact=contact,
            alert_types=alert_types,
        )

        account_alert_subscription_view.additional_properties = d
        return account_alert_subscription_view

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
