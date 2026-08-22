from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_report_subscription_view import ContactReportSubscriptionView
    from ..models.contacts_contact_ref_view import ContactsContactRefView


T = TypeVar("T", bound="ContactGroupedReportSubscriptionView")


@_attrs_define
class ContactGroupedReportSubscriptionView:
    """One element of the BY-CONTACT grouping (`GET /report/by-contact`): one contact and every monitor whose reports it
    receives.

    """

    contact: ContactsContactRefView | Unset = UNSET
    """ The minimal identifying projection of a contact, as embedded in relation reads. """
    subscriptions: list[ContactReportSubscriptionView] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        subscriptions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = []
            for subscriptions_item_data in self.subscriptions:
                subscriptions_item = subscriptions_item_data.to_dict()
                subscriptions.append(subscriptions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact is not UNSET:
            field_dict["contact"] = contact
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_report_subscription_view import ContactReportSubscriptionView
        from ..models.contacts_contact_ref_view import ContactsContactRefView

        d = dict(src_dict)
        _contact = d.pop("contact", UNSET)
        contact: ContactsContactRefView | Unset
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ContactsContactRefView.from_dict(_contact)

        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: list[ContactReportSubscriptionView] | Unset = UNSET
        if _subscriptions is not UNSET:
            subscriptions = []
            for subscriptions_item_data in _subscriptions:
                subscriptions_item = ContactReportSubscriptionView.from_dict(subscriptions_item_data)

                subscriptions.append(subscriptions_item)

        contact_grouped_report_subscription_view = cls(
            contact=contact,
            subscriptions=subscriptions,
        )

        contact_grouped_report_subscription_view.additional_properties = d
        return contact_grouped_report_subscription_view

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
