from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_confirmation_view import ContactConfirmationView


T = TypeVar("T", bound="InlineContactResultView")


@_attrs_define
class InlineContactResultView:
    id: UUID
    created: bool
    """ `false` ⇒ the item BOUND to a contact the account already held. """
    confirmed: bool
    overlimited: bool
    """ `true` when the contact this item resolved to is over the account's package allowance - **alerts to it are
    suppressed** until the package allows it again. Only a BIND can carry it: a newly created contact that trips the
    limit rolls the whole write back with `403 package_limit`. """
    ref: str | Unset = UNSET
    """ The client-supplied key from the request's `contacts[]` - the caller's join column. """
    confirmation: ContactConfirmationView | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.contact_confirmation_view import ContactConfirmationView

        id = str(self.id)

        created = self.created

        confirmed = self.confirmed

        overlimited = self.overlimited

        ref = self.ref

        confirmation: dict[str, Any] | None | Unset
        if isinstance(self.confirmation, Unset):
            confirmation = UNSET
        elif isinstance(self.confirmation, ContactConfirmationView):
            confirmation = self.confirmation.to_dict()
        else:
            confirmation = self.confirmation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
                "confirmed": confirmed,
                "overlimited": overlimited,
            }
        )
        if ref is not UNSET:
            field_dict["ref"] = ref
        if confirmation is not UNSET:
            field_dict["confirmation"] = confirmation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_confirmation_view import ContactConfirmationView

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created = d.pop("created")

        confirmed = d.pop("confirmed")

        overlimited = d.pop("overlimited")

        ref = d.pop("ref", UNSET)

        def _parse_confirmation(data: object) -> ContactConfirmationView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                confirmation_type_0 = ContactConfirmationView.from_dict(data)

                return confirmation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactConfirmationView | None | Unset, data)

        confirmation = _parse_confirmation(d.pop("confirmation", UNSET))

        inline_contact_result_view = cls(
            id=id,
            created=created,
            confirmed=confirmed,
            overlimited=overlimited,
            ref=ref,
            confirmation=confirmation,
        )

        inline_contact_result_view.additional_properties = d
        return inline_contact_result_view

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
