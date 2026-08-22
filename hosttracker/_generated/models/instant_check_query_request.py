from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.instant_check_query_request_fields_item import (
    InstantCheckQueryRequestFieldsItem,
    check_instant_check_query_request_fields_item,
)
from ..models.instant_check_query_request_type_item import (
    InstantCheckQueryRequestTypeItem,
    check_instant_check_query_request_type_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InstantCheckQueryRequest")


@_attrs_define
class InstantCheckQueryRequest:
    """The parameters, as one JSON object. A list-valued filter is a JSON array; everything else is a string, number or
    boolean. An omitted member and an explicit null both mean the parameter was not sent, and an empty array means it
    was sent empty - which every list filter refuses, exactly as it refuses an empty value on the query string.

    """

    from_: int | Unset = UNSET
    """ The start of the time window, in Unix seconds. """
    to: int | Unset = UNSET
    """ The end of the time window, in Unix seconds. """
    type_: list[InstantCheckQueryRequestTypeItem] | Unset = UNSET
    """ v2 type tokens. Repeatable and comma-separable. """
    limit: int | Unset = 50
    """ Rows to return. """
    cursor: str | Unset = UNSET
    """ Opaque cursor from a previous response's `nextCursor`. Absent ⇒ first page. """
    fields: list[InstantCheckQueryRequestFieldsItem] | Unset = UNSET
    """ Which top-level members to keep on each row - `fields=id,name`. Everything else is dropped; `id` is always
    returned whether or not you name it, and the envelope (`data`, `nextCursor`, `hasMore`, `count`, `summary`) is
    never affected. A block an `expand=` adds is a member like any other, so `fields=id,monitor&expand=monitor`
    returns the id and the monitor block. An unrecognised name is refused, never dropped, and the refusal lists what
    this row publishes. `id` is accepted on every row, including the rows that publish no `id` member - there it
    simply keeps nothing, and a mask that would keep NOTHING at all (`fields=` or `fields=id` on such a row) is
    refused rather than answered with an empty object. """

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        type_: list[str] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = []
            for type_item_data in self.type_:
                type_item: str = type_item_data
                type_.append(type_item)

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
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if type_ is not UNSET:
            field_dict["type"] = type_
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
        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: list[InstantCheckQueryRequestTypeItem] | Unset = UNSET
        if _type_ is not UNSET:
            type_ = []
            for type_item_data in _type_:
                type_item = check_instant_check_query_request_type_item(type_item_data)

                type_.append(type_item)

        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[InstantCheckQueryRequestFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = check_instant_check_query_request_fields_item(fields_item_data)

                fields.append(fields_item)

        instant_check_query_request = cls(
            from_=from_,
            to=to,
            type_=type_,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )

        return instant_check_query_request
