from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountWriteRequestDefaultAgentPoolsType0")


@_attrs_define
class AccountWriteRequestDefaultAgentPoolsType0:
    """The monitoring locations a new monitor starts with, keyed by service type and valued with that type's pool ids,
    agent ids, or an agent id prefixed "-" to exclude it. ⚠ It REPLACES the whole map rather than merging into it, so
    send the map the account should end up with; null clears every default, and a type mapped to an empty array clears
    that one. An id no location catalogue knows is refused, never dropped.

    """

    net: list[str] | Unset = UNSET
    """ The default locations for net checks. """
    waterfall: list[str] | Unset = UNSET
    """ The default locations for waterfall checks. """
    internal: list[str] | Unset = UNSET
    """ The default locations for internal checks. """
    legacy: list[str] | Unset = UNSET
    """ The default locations for legacy checks. """
    meta: list[str] | Unset = UNSET
    """ The default locations for meta checks. """

    def to_dict(self) -> dict[str, Any]:
        net: list[str] | Unset = UNSET
        if not isinstance(self.net, Unset):
            net = self.net

        waterfall: list[str] | Unset = UNSET
        if not isinstance(self.waterfall, Unset):
            waterfall = self.waterfall

        internal: list[str] | Unset = UNSET
        if not isinstance(self.internal, Unset):
            internal = self.internal

        legacy: list[str] | Unset = UNSET
        if not isinstance(self.legacy, Unset):
            legacy = self.legacy

        meta: list[str] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if net is not UNSET:
            field_dict["net"] = net
        if waterfall is not UNSET:
            field_dict["waterfall"] = waterfall
        if internal is not UNSET:
            field_dict["internal"] = internal
        if legacy is not UNSET:
            field_dict["legacy"] = legacy
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        net = cast(list[str], d.pop("net", UNSET))

        waterfall = cast(list[str], d.pop("waterfall", UNSET))

        internal = cast(list[str], d.pop("internal", UNSET))

        legacy = cast(list[str], d.pop("legacy", UNSET))

        meta = cast(list[str], d.pop("meta", UNSET))

        account_write_request_default_agent_pools_type_0 = cls(
            net=net,
            waterfall=waterfall,
            internal=internal,
            legacy=legacy,
            meta=meta,
        )

        return account_write_request_default_agent_pools_type_0
