from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.contact_bulk_request_on_error import ContactBulkRequestOnError, check_contact_bulk_request_on_error
from ..models.contact_bulk_request_on_overlimit import (
    ContactBulkRequestOnOverlimit,
    check_contact_bulk_request_on_overlimit,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_bulk_create_item import ContactBulkCreateItem
    from ..models.contact_bulk_update_item import ContactBulkUpdateItem
    from ..models.job_callback import JobCallback


T = TypeVar("T", bound="ContactBulkRequest")


@_attrs_define
class ContactBulkRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored. Every member is optional:
    what the body omits is left exactly as it was.

    """

    callback: JobCallback | Unset = UNSET
    """ A webhook to call when the job finishes, carrying the terminal job document and its first page of results.
    Send null for none. """
    create: list[ContactBulkCreateItem] | Unset = UNSET
    """ The contacts to create. """
    delete: list[UUID] | Unset = UNSET
    """ The contacts to remove, as bare ids - NOT objects. Deleting a contact removes its subscriptions with it; the
    receipt reports the cascade counts. """
    on_error: ContactBulkRequestOnError | Unset = UNSET
    """ Whether a failed item stops the run. "continue" (the default) attempts every item and reports each outcome
    separately; "stop" halts at the first refusal and reports every item that never ran as cancelled - which is what
    you want when the batch is one logical change. """
    on_overlimit: ContactBulkRequestOnOverlimit | Unset = UNSET
    """ What to do with an item the account's package will not fit. "fail" (the default) refuses that item and
    carries on; "disable" creates it disabled so nothing is lost; "stop" halts the run and reports the remainder as
    cancelled. Packages that bill overages as extras never refuse, so this has no effect on them. """
    update: list[ContactBulkUpdateItem] | Unset = UNSET
    """ The contacts to change. """

    def to_dict(self) -> dict[str, Any]:
        callback: dict[str, Any] | Unset = UNSET
        if not isinstance(self.callback, Unset):
            callback = self.callback.to_dict()

        create: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.create, Unset):
            create = []
            for create_item_data in self.create:
                create_item = create_item_data.to_dict()
                create.append(create_item)

        delete: list[str] | Unset = UNSET
        if not isinstance(self.delete, Unset):
            delete = []
            for delete_item_data in self.delete:
                delete_item = str(delete_item_data)
                delete.append(delete_item)

        on_error: str | Unset = UNSET
        if not isinstance(self.on_error, Unset):
            on_error = self.on_error

        on_overlimit: str | Unset = UNSET
        if not isinstance(self.on_overlimit, Unset):
            on_overlimit = self.on_overlimit

        update: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.update, Unset):
            update = []
            for update_item_data in self.update:
                update_item = update_item_data.to_dict()
                update.append(update_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if callback is not UNSET:
            field_dict["callback"] = callback
        if create is not UNSET:
            field_dict["create"] = create
        if delete is not UNSET:
            field_dict["delete"] = delete
        if on_error is not UNSET:
            field_dict["onError"] = on_error
        if on_overlimit is not UNSET:
            field_dict["onOverlimit"] = on_overlimit
        if update is not UNSET:
            field_dict["update"] = update

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_bulk_create_item import ContactBulkCreateItem
        from ..models.contact_bulk_update_item import ContactBulkUpdateItem
        from ..models.job_callback import JobCallback

        d = dict(src_dict)
        _callback = d.pop("callback", UNSET)
        callback: JobCallback | Unset
        if isinstance(_callback, Unset):
            callback = UNSET
        else:
            callback = JobCallback.from_dict(_callback)

        _create = d.pop("create", UNSET)
        create: list[ContactBulkCreateItem] | Unset = UNSET
        if _create is not UNSET:
            create = []
            for create_item_data in _create:
                create_item = ContactBulkCreateItem.from_dict(create_item_data)

                create.append(create_item)

        _delete = d.pop("delete", UNSET)
        delete: list[UUID] | Unset = UNSET
        if _delete is not UNSET:
            delete = []
            for delete_item_data in _delete:
                delete_item = UUID(delete_item_data)

                delete.append(delete_item)

        _on_error = d.pop("onError", UNSET)
        on_error: ContactBulkRequestOnError | Unset
        if isinstance(_on_error, Unset):
            on_error = UNSET
        else:
            on_error = check_contact_bulk_request_on_error(_on_error)

        _on_overlimit = d.pop("onOverlimit", UNSET)
        on_overlimit: ContactBulkRequestOnOverlimit | Unset
        if isinstance(_on_overlimit, Unset):
            on_overlimit = UNSET
        else:
            on_overlimit = check_contact_bulk_request_on_overlimit(_on_overlimit)

        _update = d.pop("update", UNSET)
        update: list[ContactBulkUpdateItem] | Unset = UNSET
        if _update is not UNSET:
            update = []
            for update_item_data in _update:
                update_item = ContactBulkUpdateItem.from_dict(update_item_data)

                update.append(update_item)

        contact_bulk_request = cls(
            callback=callback,
            create=create,
            delete=delete,
            on_error=on_error,
            on_overlimit=on_overlimit,
            update=update,
        )

        return contact_bulk_request
