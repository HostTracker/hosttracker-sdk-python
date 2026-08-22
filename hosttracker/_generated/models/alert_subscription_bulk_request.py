from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_subscription_bulk_item import AlertSubscriptionBulkItem


T = TypeVar("T", bound="AlertSubscriptionBulkRequest")


@_attrs_define
class AlertSubscriptionBulkRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored. Every member is optional:
    what the body omits is left exactly as it was.

    """

    all_contacts: bool | Unset = UNSET
    """ Read every entry that omits `contactIds` as every contact on the account. An entry may not carry
    `contactIds` as well, and only one of the two wildcards may be set. """
    all_monitors: bool | Unset = UNSET
    """ Read every entry that omits `monitorIds` as every monitor on the account. An entry may not carry
    `monitorIds` as well, and only one of the two wildcards may be set. """
    create: list[AlertSubscriptionBulkItem] | Unset = UNSET
    """ The wirings to add. """
    delete: list[AlertSubscriptionBulkItem] | Unset = UNSET
    """ The wirings to remove. """

    def to_dict(self) -> dict[str, Any]:
        all_contacts = self.all_contacts

        all_monitors = self.all_monitors

        create: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.create, Unset):
            create = []
            for create_item_data in self.create:
                create_item = create_item_data.to_dict()
                create.append(create_item)

        delete: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.delete, Unset):
            delete = []
            for delete_item_data in self.delete:
                delete_item = delete_item_data.to_dict()
                delete.append(delete_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if all_contacts is not UNSET:
            field_dict["allContacts"] = all_contacts
        if all_monitors is not UNSET:
            field_dict["allMonitors"] = all_monitors
        if create is not UNSET:
            field_dict["create"] = create
        if delete is not UNSET:
            field_dict["delete"] = delete

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_subscription_bulk_item import AlertSubscriptionBulkItem

        d = dict(src_dict)
        all_contacts = d.pop("allContacts", UNSET)

        all_monitors = d.pop("allMonitors", UNSET)

        _create = d.pop("create", UNSET)
        create: list[AlertSubscriptionBulkItem] | Unset = UNSET
        if _create is not UNSET:
            create = []
            for create_item_data in _create:
                create_item = AlertSubscriptionBulkItem.from_dict(create_item_data)

                create.append(create_item)

        _delete = d.pop("delete", UNSET)
        delete: list[AlertSubscriptionBulkItem] | Unset = UNSET
        if _delete is not UNSET:
            delete = []
            for delete_item_data in _delete:
                delete_item = AlertSubscriptionBulkItem.from_dict(delete_item_data)

                delete.append(delete_item)

        alert_subscription_bulk_request = cls(
            all_contacts=all_contacts,
            all_monitors=all_monitors,
            create=create,
            delete=delete,
        )

        return alert_subscription_bulk_request
