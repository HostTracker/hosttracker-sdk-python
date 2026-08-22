from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.agent_query_request_capability_item import (
    AgentQueryRequestCapabilityItem,
    check_agent_query_request_capability_item,
)
from ..models.agent_query_request_fields_item import AgentQueryRequestFieldsItem, check_agent_query_request_fields_item
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentQueryRequest")


@_attrs_define
class AgentQueryRequest:
    """The parameters, as one JSON object. A list-valued filter is a JSON array; everything else is a string, number or
    boolean. An omitted member and an explicit null both mean the parameter was not sent, and an empty array means it
    was sent empty - which every list filter refuses, exactly as it refuses an empty value on the query string.

    """

    country: list[str] | Unset = UNSET
    """ Datacenter country names. Repeatable and comma-separable; matched case-insensitively. """
    pool: list[str] | Unset = UNSET
    """ Pool ids - a location is kept when it belongs to any of them (parents populated). """
    capability: list[AgentQueryRequestCapabilityItem] | Unset = UNSET
    """ `icmp` | `browser` | `internal`. ANDed: a location must offer all requested capabilities. """
    limit: int | Unset = 50
    """ Rows to return. """
    cursor: str | Unset = UNSET
    """ Opaque cursor from a previous response's `nextCursor`. Absent ⇒ first page. """
    fields: list[AgentQueryRequestFieldsItem] | Unset = UNSET
    """ Which top-level members to keep on each row - `fields=id,name`. Everything else is dropped; `id` is always
    returned whether or not you name it, and the envelope (`data`, `nextCursor`, `hasMore`, `count`, `summary`) is
    never affected. A block an `expand=` adds is a member like any other, so `fields=id,monitor&expand=monitor`
    returns the id and the monitor block. An unrecognised name is refused, never dropped, and the refusal lists what
    this row publishes. `id` is accepted on every row, including the rows that publish no `id` member - there it
    simply keeps nothing, and a mask that would keep NOTHING at all (`fields=` or `fields=id` on such a row) is
    refused rather than answered with an empty object. """

    def to_dict(self) -> dict[str, Any]:
        country: list[str] | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = self.country

        pool: list[str] | Unset = UNSET
        if not isinstance(self.pool, Unset):
            pool = self.pool

        capability: list[str] | Unset = UNSET
        if not isinstance(self.capability, Unset):
            capability = []
            for capability_item_data in self.capability:
                capability_item: str = capability_item_data
                capability.append(capability_item)

        limit = self.limit

        cursor = self.cursor

        fields: list[str] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item: str = fields_item_data
                fields.append(fields_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if country is not UNSET:
            field_dict["country"] = country
        if pool is not UNSET:
            field_dict["pool"] = pool
        if capability is not UNSET:
            field_dict["capability"] = capability
        if limit is not UNSET:
            field_dict["limit"] = limit
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country = cast(list[str], d.pop("country", UNSET))

        pool = cast(list[str], d.pop("pool", UNSET))

        _capability = d.pop("capability", UNSET)
        capability: list[AgentQueryRequestCapabilityItem] | Unset = UNSET
        if _capability is not UNSET:
            capability = []
            for capability_item_data in _capability:
                capability_item = check_agent_query_request_capability_item(capability_item_data)

                capability.append(capability_item)

        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[AgentQueryRequestFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = check_agent_query_request_fields_item(fields_item_data)

                fields.append(fields_item)

        agent_query_request = cls(
            country=country,
            pool=pool,
            capability=capability,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )

        return agent_query_request
