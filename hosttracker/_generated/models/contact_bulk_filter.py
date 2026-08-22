from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.contact_bulk_filter_types_item import ContactBulkFilterTypesItem, check_contact_bulk_filter_types_item
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactBulkFilter")


@_attrs_define
class ContactBulkFilter:
    """Which contacts the deletion selects. A filter that narrows by nothing is REFUSED - it would select every contact on
    the account. The member names are the plural forms; the list endpoint's query string spells the same narrowings in
    the singular.

    """

    contact_ids: list[UUID] | Unset = UNSET
    """ A contact to select, named explicitly. """
    types: list[ContactBulkFilterTypesItem] | Unset = UNSET
    """ Select by contact type. """
    confirmed: bool | None | Unset = UNSET
    """ Select only confirmed, or only unconfirmed, contacts. """
    q: None | str | Unset = UNSET
    """ A case-insensitive substring match over name and address. """

    def to_dict(self) -> dict[str, Any]:
        contact_ids: list[str] | Unset = UNSET
        if not isinstance(self.contact_ids, Unset):
            contact_ids = []
            for contact_ids_item_data in self.contact_ids:
                contact_ids_item = str(contact_ids_item_data)
                contact_ids.append(contact_ids_item)

        types: list[str] | Unset = UNSET
        if not isinstance(self.types, Unset):
            types = []
            for types_item_data in self.types:
                types_item: str = types_item_data
                types.append(types_item)

        confirmed: bool | None | Unset
        if isinstance(self.confirmed, Unset):
            confirmed = UNSET
        else:
            confirmed = self.confirmed

        q: None | str | Unset
        if isinstance(self.q, Unset):
            q = UNSET
        else:
            q = self.q

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if contact_ids is not UNSET:
            field_dict["contactIds"] = contact_ids
        if types is not UNSET:
            field_dict["types"] = types
        if confirmed is not UNSET:
            field_dict["confirmed"] = confirmed
        if q is not UNSET:
            field_dict["q"] = q

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _contact_ids = d.pop("contactIds", UNSET)
        contact_ids: list[UUID] | Unset = UNSET
        if _contact_ids is not UNSET:
            contact_ids = []
            for contact_ids_item_data in _contact_ids:
                contact_ids_item = UUID(contact_ids_item_data)

                contact_ids.append(contact_ids_item)

        _types = d.pop("types", UNSET)
        types: list[ContactBulkFilterTypesItem] | Unset = UNSET
        if _types is not UNSET:
            types = []
            for types_item_data in _types:
                types_item = check_contact_bulk_filter_types_item(types_item_data)

                types.append(types_item)

        def _parse_confirmed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        confirmed = _parse_confirmed(d.pop("confirmed", UNSET))

        def _parse_q(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        q = _parse_q(d.pop("q", UNSET))

        contact_bulk_filter = cls(
            contact_ids=contact_ids,
            types=types,
            confirmed=confirmed,
            q=q,
        )

        return contact_bulk_filter
