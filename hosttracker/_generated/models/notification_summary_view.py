from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contacts_contact_ref_view import ContactsContactRefView


T = TypeVar("T", bound="NotificationSummaryView")


@_attrs_define
class NotificationSummaryView:
    """One row of the per-contact delivery-stats aggregate served by `GET /contact/notification/summary`: the count of
    deliveries for one (contact, outcome, UTC day) cell of the window. The v2 port of the first-party
    `/notification/stats` shape, with the outcome in the SAME published vocabulary the log's `outcome=` filter takes.

    """

    day: int
    """ The UTC day the cell counts (midnight instant, Unix seconds on the wire). Unix seconds. """
    count: int
    contact: ContactsContactRefView | Unset = UNSET
    """ The minimal identifying projection of a contact, as embedded in relation reads. """
    outcome: None | str | Unset = UNSET
    """ How the deliveries in this cell ended - the same word the log row's attempts carry. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day = self.day

        count = self.count

        contact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        outcome: None | str | Unset
        if isinstance(self.outcome, Unset):
            outcome = UNSET
        else:
            outcome = self.outcome

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day": day,
                "count": count,
            }
        )
        if contact is not UNSET:
            field_dict["contact"] = contact
        if outcome is not UNSET:
            field_dict["outcome"] = outcome

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contacts_contact_ref_view import ContactsContactRefView

        d = dict(src_dict)
        day = d.pop("day")

        count = d.pop("count")

        _contact = d.pop("contact", UNSET)
        contact: ContactsContactRefView | Unset
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ContactsContactRefView.from_dict(_contact)

        def _parse_outcome(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outcome = _parse_outcome(d.pop("outcome", UNSET))

        notification_summary_view = cls(
            day=day,
            count=count,
            contact=contact,
            outcome=outcome,
        )

        notification_summary_view.additional_properties = d
        return notification_summary_view

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
