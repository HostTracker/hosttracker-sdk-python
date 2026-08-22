from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AccountViewDefaultAgentPools")


@_attrs_define
class AccountViewDefaultAgentPools:
    """**The monitoring locations a new monitor of each service type starts with**, keyed by the service type's wire token
    (`net`, `waterfall`, `internal`) and valued with that type's default pool ids - a pool id, an agent id, or an agent
    id prefixed `-` to exclude it from an otherwise selected pool. Empty when the account has never chosen one, in which
    case a create falls back to the platform default. It is the same map `GET /agent/pool` publishes on its envelope as
    `defaults`, in the same spelling - one fact, one vocabulary - and it is here because it is WRITABLE through `PATCH
    /account` and a client should be able to read what it is about to change from the resource that owns it. ⚠ **The
    keys are the lowerCamel service-type tokens this surface publishes everywhere else** (`net`), not the storage enum
    names the first-party `GET /user` returns (`Net`). Two spellings of one vocabulary is the defect this surface is
    built to avoid, and the v2 half of it was already spelled this way.

    """

    additional_properties: dict[str, list[str]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_view_default_agent_pools = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = cast(list[str], prop_dict)

            additional_properties[prop_name] = additional_property

        account_view_default_agent_pools.additional_properties = additional_properties
        return account_view_default_agent_pools

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[str]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[str]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
