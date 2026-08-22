from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contacts_contact_ref_view import ContactsContactRefView


T = TypeVar("T", bound="MonitorReportSubscriptionView")


@_attrs_define
class MonitorReportSubscriptionView:
    """The report subscription between a monitor and a contact, seen from the MONITOR side. A pair is a SET of frequencies;
    reports are Email-only.

    """

    created: int
    """ Unix seconds. """
    contact: ContactsContactRefView | Unset = UNSET
    """ The minimal identifying projection of a contact, as embedded in relation reads. """
    frequencies: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        contact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        frequencies: list[str] | Unset = UNSET
        if not isinstance(self.frequencies, Unset):
            frequencies = self.frequencies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
            }
        )
        if contact is not UNSET:
            field_dict["contact"] = contact
        if frequencies is not UNSET:
            field_dict["frequencies"] = frequencies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contacts_contact_ref_view import ContactsContactRefView

        d = dict(src_dict)
        created = d.pop("created")

        _contact = d.pop("contact", UNSET)
        contact: ContactsContactRefView | Unset
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ContactsContactRefView.from_dict(_contact)

        frequencies = cast(list[str], d.pop("frequencies", UNSET))

        monitor_report_subscription_view = cls(
            created=created,
            contact=contact,
            frequencies=frequencies,
        )

        monitor_report_subscription_view.additional_properties = d
        return monitor_report_subscription_view

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
