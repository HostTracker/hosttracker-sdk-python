from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.contact_bulk_filter import ContactBulkFilter


T = TypeVar("T", bound="ContactBulkDeleteValidateRequest")


@_attrs_define
class ContactBulkDeleteValidateRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored."""

    filter_: ContactBulkFilter
    """ Which contacts the deletion selects. A filter that narrows by nothing is REFUSED - it would select every
    contact on the account. The member names are the plural forms; the list endpoint's query string spells the same
    narrowings in the singular. """

    def to_dict(self) -> dict[str, Any]:
        filter_ = self.filter_.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "filter": filter_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_bulk_filter import ContactBulkFilter

        d = dict(src_dict)
        filter_ = ContactBulkFilter.from_dict(d.pop("filter"))

        contact_bulk_delete_validate_request = cls(
            filter_=filter_,
        )

        return contact_bulk_delete_validate_request
