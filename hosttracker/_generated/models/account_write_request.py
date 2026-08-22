from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_write_request_default_agent_pools_type_0 import AccountWriteRequestDefaultAgentPoolsType0


T = TypeVar("T", bound="AccountWriteRequest")


@_attrs_define
class AccountWriteRequest:
    """The member vocabulary is closed: a member not listed here is refused rather than ignored. Every member is optional:
    what the body omits is left exactly as it was.

    """

    company: str | Unset = UNSET
    """ The organisation the account belongs to. Send an empty string to clear it. """
    country: str | Unset = UNSET
    """ The account's country as an ISO 3166-1 alpha-2 code ("DE", "US"), matched against the platform's own country
    list. Send an empty string to clear it; a code the list does not carry is refused rather than stored. """
    default_agent_pools: AccountWriteRequestDefaultAgentPoolsType0 | None | Unset = UNSET
    """ The monitoring locations a new monitor starts with, keyed by service type and valued with that type's pool
    ids, agent ids, or an agent id prefixed "-" to exclude it. ⚠ It REPLACES the whole map rather than merging into
    it, so send the map the account should end up with; null clears every default, and a type mapped to an empty
    array clears that one. An id no location catalogue knows is refused, never dropped. """
    first_name: str | Unset = UNSET
    """ The account holder's given name. Send an empty string to clear it. """
    language: str | Unset = UNSET
    """ The language this account's notifications and UI are written in, as the platform's language code. Only
    languages the platform actively translates are accepted; a contact may still override it with its own. """
    last_name: str | Unset = UNSET
    """ The account holder's family name. Send an empty string to clear it. """
    phone: str | Unset = UNSET
    """ A contact telephone number, stored as typed and never parsed as a number. Send an empty string to clear it.
    """
    timezone: str | Unset = UNSET
    """ The account's own time zone, as an IANA zone id - "Europe/Berlin". It is what every schedule, report window
    and rendered timestamp on the account is anchored to when nothing nearer names one. There is no "no zone" state:
    send "UTC" rather than an empty value. ⚠ Storage keeps the Windows equivalent and that map is one-to-many, so a
    value can read back as its group's representative id ("Europe/Rome" reads back as "Europe/Berlin") - same clock,
    same daylight-saving rules, a re-spelled label. """

    def to_dict(self) -> dict[str, Any]:
        from ..models.account_write_request_default_agent_pools_type_0 import AccountWriteRequestDefaultAgentPoolsType0

        company = self.company

        country = self.country

        default_agent_pools: dict[str, Any] | None | Unset
        if isinstance(self.default_agent_pools, Unset):
            default_agent_pools = UNSET
        elif isinstance(self.default_agent_pools, AccountWriteRequestDefaultAgentPoolsType0):
            default_agent_pools = self.default_agent_pools.to_dict()
        else:
            default_agent_pools = self.default_agent_pools

        first_name = self.first_name

        language = self.language

        last_name = self.last_name

        phone = self.phone

        timezone = self.timezone

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if company is not UNSET:
            field_dict["company"] = company
        if country is not UNSET:
            field_dict["country"] = country
        if default_agent_pools is not UNSET:
            field_dict["defaultAgentPools"] = default_agent_pools
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if language is not UNSET:
            field_dict["language"] = language
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_write_request_default_agent_pools_type_0 import AccountWriteRequestDefaultAgentPoolsType0

        d = dict(src_dict)
        company = d.pop("company", UNSET)

        country = d.pop("country", UNSET)

        def _parse_default_agent_pools(data: object) -> AccountWriteRequestDefaultAgentPoolsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_agent_pools_type_0 = AccountWriteRequestDefaultAgentPoolsType0.from_dict(data)

                return default_agent_pools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccountWriteRequestDefaultAgentPoolsType0 | None | Unset, data)

        default_agent_pools = _parse_default_agent_pools(d.pop("defaultAgentPools", UNSET))

        first_name = d.pop("firstName", UNSET)

        language = d.pop("language", UNSET)

        last_name = d.pop("lastName", UNSET)

        phone = d.pop("phone", UNSET)

        timezone = d.pop("timezone", UNSET)

        account_write_request = cls(
            company=company,
            country=country,
            default_agent_pools=default_agent_pools,
            first_name=first_name,
            language=language,
            last_name=last_name,
            phone=phone,
            timezone=timezone,
        )

        return account_write_request
