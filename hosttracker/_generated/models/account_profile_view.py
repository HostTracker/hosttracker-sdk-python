from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountProfileView")


@_attrs_define
class AccountProfileView:
    first_name: str | Unset = UNSET
    """ Given name. At most 50 characters. """
    last_name: str | Unset = UNSET
    """ Family name. At most 50 characters. """
    company: str | Unset = UNSET
    """ The organisation the account belongs to. At most 100 characters. """
    phone: str | Unset = UNSET
    """ A contact telephone number, as typed. At most 20 characters; never validated as a number, because this one
    is for a human to read and not for the platform to dial. """
    country: str | Unset = UNSET
    """ The account's country as an ISO 3166-1 **alpha-2** code (`DE`, `US`), or the empty string when none is set.
    The accepted codes are the platform's own country table; a code it does not carry is refused by `PATCH /account`
    rather than stored. """
    email: None | str | Unset = UNSET
    """ **The login email** - the address the account signs in with and the one every account-level mail is sent to,
    read from the membership store rather than from the profile row. ⚠ **Read-only here.**`PATCH /account` does not
    take it: changing the login address is a confirmation-code flow (a code is mailed to the NEW address and
    submitted back), which is an authentication concern and stays on the first-party session doors. Null when the
    account carries no membership record. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        company = self.company

        phone = self.phone

        country = self.country

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if company is not UNSET:
            field_dict["company"] = company
        if phone is not UNSET:
            field_dict["phone"] = phone
        if country is not UNSET:
            field_dict["country"] = country
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        company = d.pop("company", UNSET)

        phone = d.pop("phone", UNSET)

        country = d.pop("country", UNSET)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        account_profile_view = cls(
            first_name=first_name,
            last_name=last_name,
            company=company,
            phone=phone,
            country=country,
            email=email,
        )

        account_profile_view.additional_properties = d
        return account_profile_view

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
