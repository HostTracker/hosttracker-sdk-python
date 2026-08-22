from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.result_query_request_expand_item import (
    ResultQueryRequestExpandItem,
    check_result_query_request_expand_item,
)
from ..models.result_query_request_fields_item import (
    ResultQueryRequestFieldsItem,
    check_result_query_request_fields_item,
)
from ..models.result_query_request_sort import ResultQueryRequestSort, check_result_query_request_sort
from ..models.result_query_request_state_item import ResultQueryRequestStateItem, check_result_query_request_state_item
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResultQueryRequest")


@_attrs_define
class ResultQueryRequest:
    """The parameters, as one JSON object. A list-valued filter is a JSON array; everything else is a string, number or
    boolean. An omitted member and an explicit null both mean the parameter was not sent, and an empty array means it
    was sent empty - which every list filter refuses, exactly as it refuses an empty value on the query string.

    """

    monitor: list[str] | Unset = UNSET
    """ The monitors to read, as an id list - a NARROWING filter, ANDed with `url=` and `q=` exactly as on `GET
    /monitor`. Omitting every monitor filter reads the account's whole feed; a PRESENT-but-empty list selects
    nothing and answers an empty page. """
    url: list[str] | Unset = UNSET
    """ Narrow by the monitor's ADDRESS instead of by GUID - list-accepting (ANY-OF), matched against the monitor's
    address. Exact (case-insensitive) unless `like=true`. ANDed with the other monitor filters; owned monitors only.
    """
    like: bool | Unset = UNSET
    """ `true` switches `url=` from exact match to case-insensitive SUBSTRING match. Meaningless without `url=` -
    sent alone it is refused, never silently ignored. """
    q: str | Unset = UNSET
    """ Free-text monitor filter: case-insensitive substring over the monitor's NAME and address - the same matching
    `GET /monitor`'s own `q=` performs, and ANDed with the other monitor filters. An empty needle narrows nothing.
    """
    from_: int | Unset = UNSET
    """ Window start, Unix seconds. """
    to: int | Unset = UNSET
    """ Window end, Unix seconds. Omitted ⇒ now. """
    location: list[str] | Unset = UNSET
    """ Agent (location) ids - ANY-OF, like every other v2 list filter. """
    state: list[ResultQueryRequestStateItem] | Unset = UNSET
    """ Which lifecycle states to include. """
    sort: ResultQueryRequestSort | Unset = UNSET
    """ Which column to order by, optionally with a direction: `sort=name` or `sort=name:desc`. Without a suffix
    each column takes its natural direction - time columns newest-first, everything else A to Z. The columns a list
    offers are published as this parameter's accepted values, bare and with each suffix, and a refusal echoes that
    same full set; there is no separate `order` parameter. A cursor addresses the ordering it was minted in, column
    AND direction: replaying one under a different `sort` is refused rather than answered with rows you have already
    read. """
    expand: list[ResultQueryRequestExpandItem] | Unset = UNSET
    """ Comma-separated names of the extra blocks to embed. The only composition spelling on this surface - an
    unrecognised name is refused, never dropped, and the refusal lists what is allowed. A repeated key is accepted
    too and unions with the comma list, so expand=a,b and expand=a&expand=b ask the same thing. Sending it REPLACES
    the endpoint's defaults, so `expand=` on its own asks for the leanest row - present and empty, which is not the
    same as not sending it. Nothing relational is ever on by default: a list returns bare rows and a single read
    returns the resource's own detail. On a row that belongs to a monitor, `monitor.<value>` (settings,
    subscription, lastIncident, maintenance) embeds that block inside the row's `monitor` object and implies
    `monitor` itself. """
    limit: int | Unset = 50
    """ Rows to return. """
    cursor: str | Unset = UNSET
    """ Opaque cursor from a previous response's `nextCursor`. Absent ⇒ first page. """
    fields: list[ResultQueryRequestFieldsItem] | Unset = UNSET
    """ Which top-level members to keep on each row - `fields=id,name`. Everything else is dropped; `id` is always
    returned whether or not you name it, and the envelope (`data`, `nextCursor`, `hasMore`, `count`, `summary`) is
    never affected. A block an `expand=` adds is a member like any other, so `fields=id,monitor&expand=monitor`
    returns the id and the monitor block. An unrecognised name is refused, never dropped, and the refusal lists what
    this row publishes. `id` is accepted on every row, including the rows that publish no `id` member - there it
    simply keeps nothing, and a mask that would keep NOTHING at all (`fields=` or `fields=id` on such a row) is
    refused rather than answered with an empty object. """

    def to_dict(self) -> dict[str, Any]:
        monitor: list[str] | Unset = UNSET
        if not isinstance(self.monitor, Unset):
            monitor = self.monitor

        url: list[str] | Unset = UNSET
        if not isinstance(self.url, Unset):
            url = self.url

        like = self.like

        q = self.q

        from_ = self.from_

        to = self.to

        location: list[str] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location

        state: list[str] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = []
            for state_item_data in self.state:
                state_item: str = state_item_data
                state.append(state_item)

        sort: str | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort

        expand: list[str] | Unset = UNSET
        if not isinstance(self.expand, Unset):
            expand = []
            for expand_item_data in self.expand:
                expand_item: str = expand_item_data
                expand.append(expand_item)

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
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if url is not UNSET:
            field_dict["url"] = url
        if like is not UNSET:
            field_dict["like"] = like
        if q is not UNSET:
            field_dict["q"] = q
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if location is not UNSET:
            field_dict["location"] = location
        if state is not UNSET:
            field_dict["state"] = state
        if sort is not UNSET:
            field_dict["sort"] = sort
        if expand is not UNSET:
            field_dict["expand"] = expand
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
        monitor = cast(list[str], d.pop("monitor", UNSET))

        url = cast(list[str], d.pop("url", UNSET))

        like = d.pop("like", UNSET)

        q = d.pop("q", UNSET)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        location = cast(list[str], d.pop("location", UNSET))

        _state = d.pop("state", UNSET)
        state: list[ResultQueryRequestStateItem] | Unset = UNSET
        if _state is not UNSET:
            state = []
            for state_item_data in _state:
                state_item = check_result_query_request_state_item(state_item_data)

                state.append(state_item)

        _sort = d.pop("sort", UNSET)
        sort: ResultQueryRequestSort | Unset
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = check_result_query_request_sort(_sort)

        _expand = d.pop("expand", UNSET)
        expand: list[ResultQueryRequestExpandItem] | Unset = UNSET
        if _expand is not UNSET:
            expand = []
            for expand_item_data in _expand:
                expand_item = check_result_query_request_expand_item(expand_item_data)

                expand.append(expand_item)

        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[ResultQueryRequestFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = check_result_query_request_fields_item(fields_item_data)

                fields.append(fields_item)

        result_query_request = cls(
            monitor=monitor,
            url=url,
            like=like,
            q=q,
            from_=from_,
            to=to,
            location=location,
            state=state,
            sort=sort,
            expand=expand,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )

        return result_query_request
