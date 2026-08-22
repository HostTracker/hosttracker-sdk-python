from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_bulk_validate_summary import ContactBulkValidateSummary
    from ..models.contact_validate_item_view import ContactValidateItemView


T = TypeVar("T", bound="ContactBulkValidateView")


@_attrs_define
class ContactBulkValidateView:
    valid: bool
    """ True when EVERY item is valid - the one member a caller that just wants a go/no-go reads. An item that would
    be created DISABLED is valid: the request is well formed and the write will land; the caveat is in its own
    `overlimit`. """
    summary: ContactBulkValidateSummary | Unset = UNSET
    """ The per-leg item counts of a validation run. """
    create: list[ContactValidateItemView] | Unset = UNSET
    update: list[ContactValidateItemView] | Unset = UNSET
    delete: list[ContactValidateItemView] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        valid = self.valid

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        create: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.create, Unset):
            create = []
            for create_item_data in self.create:
                create_item = create_item_data.to_dict()
                create.append(create_item)

        update: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.update, Unset):
            update = []
            for update_item_data in self.update:
                update_item = update_item_data.to_dict()
                update.append(update_item)

        delete: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.delete, Unset):
            delete = []
            for delete_item_data in self.delete:
                delete_item = delete_item_data.to_dict()
                delete.append(delete_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valid": valid,
            }
        )
        if summary is not UNSET:
            field_dict["summary"] = summary
        if create is not UNSET:
            field_dict["create"] = create
        if update is not UNSET:
            field_dict["update"] = update
        if delete is not UNSET:
            field_dict["delete"] = delete

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_bulk_validate_summary import ContactBulkValidateSummary
        from ..models.contact_validate_item_view import ContactValidateItemView

        d = dict(src_dict)
        valid = d.pop("valid")

        _summary = d.pop("summary", UNSET)
        summary: ContactBulkValidateSummary | Unset
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = ContactBulkValidateSummary.from_dict(_summary)

        _create = d.pop("create", UNSET)
        create: list[ContactValidateItemView] | Unset = UNSET
        if _create is not UNSET:
            create = []
            for create_item_data in _create:
                create_item = ContactValidateItemView.from_dict(create_item_data)

                create.append(create_item)

        _update = d.pop("update", UNSET)
        update: list[ContactValidateItemView] | Unset = UNSET
        if _update is not UNSET:
            update = []
            for update_item_data in _update:
                update_item = ContactValidateItemView.from_dict(update_item_data)

                update.append(update_item)

        _delete = d.pop("delete", UNSET)
        delete: list[ContactValidateItemView] | Unset = UNSET
        if _delete is not UNSET:
            delete = []
            for delete_item_data in _delete:
                delete_item = ContactValidateItemView.from_dict(delete_item_data)

                delete.append(delete_item)

        contact_bulk_validate_view = cls(
            valid=valid,
            summary=summary,
            create=create,
            update=update,
            delete=delete,
        )

        contact_bulk_validate_view.additional_properties = d
        return contact_bulk_validate_view

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
