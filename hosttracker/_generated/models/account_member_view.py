from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_member_view_state import AccountMemberViewState, check_account_member_view_state
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contacts_contact_ref_view import ContactsContactRefView


T = TypeVar("T", bound="AccountMemberView")


@_attrs_define
class AccountMemberView:
    id: UUID
    """ The membership row's id - the **contact** the access was granted to, which is the key the whole subaccount
    graph is stored under. """
    user_id: None | Unset | UUID = UNSET
    """ The delegate's own account id, once the invitation has been accepted. """
    contact: ContactsContactRefView | None | Unset = UNSET
    """ The minimal identifying projection of a contact, as embedded in relation reads. """
    rights: list[str] | Unset = UNSET
    """ The granted rights, as `<area>:<read|write>` tokens - `monitor:write`, `contact:read`, `billing:read`,
    `profile:write`, `api:access`, `member:write`, `statusPage:read`. Sorted, so two reads of the same grant are
    byte-equal. """
    state: AccountMemberViewState | Unset = UNSET
    """ `active` | `pending` (invited, not yet confirmed) | `disabled`. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.contacts_contact_ref_view import ContactsContactRefView

        id = str(self.id)

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        contact: dict[str, Any] | None | Unset
        if isinstance(self.contact, Unset):
            contact = UNSET
        elif isinstance(self.contact, ContactsContactRefView):
            contact = self.contact.to_dict()
        else:
            contact = self.contact

        rights: list[str] | Unset = UNSET
        if not isinstance(self.rights, Unset):
            rights = self.rights

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if contact is not UNSET:
            field_dict["contact"] = contact
        if rights is not UNSET:
            field_dict["rights"] = rights
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contacts_contact_ref_view import ContactsContactRefView

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("userId", UNSET))

        def _parse_contact(data: object) -> ContactsContactRefView | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                contact_type_0 = ContactsContactRefView.from_dict(data)

                return contact_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactsContactRefView | None | Unset, data)

        contact = _parse_contact(d.pop("contact", UNSET))

        rights = cast(list[str], d.pop("rights", UNSET))

        _state = d.pop("state", UNSET)
        state: AccountMemberViewState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = check_account_member_view_state(_state)

        account_member_view = cls(
            id=id,
            user_id=user_id,
            contact=contact,
            rights=rights,
            state=state,
        )

        account_member_view.additional_properties = d
        return account_member_view

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
