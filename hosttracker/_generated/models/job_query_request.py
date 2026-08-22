from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.job_query_request_fields_item import JobQueryRequestFieldsItem, check_job_query_request_fields_item
from ..models.job_query_request_state_item import JobQueryRequestStateItem, check_job_query_request_state_item
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobQueryRequest")


@_attrs_define
class JobQueryRequest:
    """The parameters, as one JSON object. A list-valued filter is a JSON array; everything else is a string, number or
    boolean. An omitted member and an explicit null both mean the parameter was not sent, and an empty array means it
    was sent empty - which every list filter refuses, exactly as it refuses an empty value on the query string.

    """

    kind: list[str] | Unset = UNSET
    """ Job kinds, e.g. `monitor.bulkCreate` - ANY-OF. Each token is accepted as any string and matched exactly: the
    kind set is an open registry that grows over time, and refusing an unregistered one would make this list refuse
    to show jobs whose executor has since been retired. """
    state: list[JobQueryRequestStateItem] | Unset = UNSET
    """ Which lifecycle states to include. """
    limit: int | Unset = 50
    """ Rows to return. """
    cursor: str | Unset = UNSET
    """ Opaque cursor from a previous response's `nextCursor`. Absent ⇒ first page. """
    fields: list[JobQueryRequestFieldsItem] | Unset = UNSET
    """ Which top-level members to keep on each row - `fields=id,name`. Everything else is dropped; `id` is always
    returned whether or not you name it, and the envelope (`data`, `nextCursor`, `hasMore`, `count`, `summary`) is
    never affected. A block an `expand=` adds is a member like any other, so `fields=id,monitor&expand=monitor`
    returns the id and the monitor block. An unrecognised name is refused, never dropped, and the refusal lists what
    this row publishes. `id` is accepted on every row, including the rows that publish no `id` member - there it
    simply keeps nothing, and a mask that would keep NOTHING at all (`fields=` or `fields=id` on such a row) is
    refused rather than answered with an empty object. """

    def to_dict(self) -> dict[str, Any]:
        kind: list[str] | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        state: list[str] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = []
            for state_item_data in self.state:
                state_item: str = state_item_data
                state.append(state_item)

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
        if kind is not UNSET:
            field_dict["kind"] = kind
        if state is not UNSET:
            field_dict["state"] = state
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
        kind = cast(list[str], d.pop("kind", UNSET))

        _state = d.pop("state", UNSET)
        state: list[JobQueryRequestStateItem] | Unset = UNSET
        if _state is not UNSET:
            state = []
            for state_item_data in _state:
                state_item = check_job_query_request_state_item(state_item_data)

                state.append(state_item)

        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[JobQueryRequestFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = check_job_query_request_fields_item(fields_item_data)

                fields.append(fields_item)

        job_query_request = cls(
            kind=kind,
            state=state,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )

        return job_query_request
