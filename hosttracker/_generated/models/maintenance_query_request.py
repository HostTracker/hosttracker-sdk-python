from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.maintenance_query_request_expand_item import (
    MaintenanceQueryRequestExpandItem,
    check_maintenance_query_request_expand_item,
)
from ..models.maintenance_query_request_fields_item import (
    MaintenanceQueryRequestFieldsItem,
    check_maintenance_query_request_fields_item,
)
from ..models.maintenance_query_request_sort import MaintenanceQueryRequestSort, check_maintenance_query_request_sort
from ..models.maintenance_query_request_state_item import (
    MaintenanceQueryRequestStateItem,
    check_maintenance_query_request_state_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MaintenanceQueryRequest")


@_attrs_define
class MaintenanceQueryRequest:
    """The parameters, as one JSON object. A list-valued filter is a JSON array; everything else is a string, number or
    boolean. An omitted member and an explicit null both mean the parameter was not sent, and an empty array means it
    was sent empty - which every list filter refuses, exactly as it refuses an empty value on the query string.

    """

    from_: int | Unset = UNSET
    """ Window START lower bound, Unix seconds. """
    to: int | Unset = UNSET
    """ Window START upper bound, Unix seconds. """
    state: list[MaintenanceQueryRequestStateItem] | Unset = UNSET
    """ `scheduled` | `active` | `finished`, any combination. """
    monitor: list[str] | Unset = UNSET
    """ Only windows covering these monitors. """
    updated_since: str | Unset = UNSET
    """ Return only what changed since this point - either Unix seconds, or the `syncCursor` a previous response
    returned. This is what makes a poll loop cheap. How much it catches depends on the resource: read its own
    `updated` field's description for exactly what moves it, and on two of them it is deliberately less than the
    name suggests. On a MONITOR only creation, an up/down transition and an automatic package-limit disable move it
    - a rename, an interval or settings change, a tag edit and a manual pause do NOT. On a CONTACT it is the
    creation instant alone, so no edit of any kind moves it. Maintenance windows and webhooks are exact: every
    change stamps them. And DELETIONS are reported by none of them - a removed row simply stops appearing, which a
    page cannot distinguish from a filter that did not match it. So subscribe to that resource's `.updated` and
    `.deleted` webhook events for the changes this parameter cannot see, and reconcile against a full list from time
    to time. A value that is neither an integer nor a cursor is refused as a validation failure naming this
    parameter (`reason: wrong_type`, `expected: integer|syncCursor`); a PAGE cursor sent here is refused as an
    invalid cursor, because that is what it is. """
    sort: MaintenanceQueryRequestSort | Unset = UNSET
    """ `from` (the default) | `created`, optionally suffixed with `:asc` or `:desc` (`sort=created:asc`). Both are
    time columns, so unsuffixed means newest-first - the order this list has always shipped. There is no separate
    `order=` parameter. """
    expand: list[MaintenanceQueryRequestExpandItem] | Unset = UNSET
    """ `monitor` - the identifying projection of the window's monitor set. """
    limit: int | Unset = 50
    """ Rows to return. """
    cursor: str | Unset = UNSET
    """ Opaque cursor from a previous response's `nextCursor`. Absent ⇒ first page. """
    fields: list[MaintenanceQueryRequestFieldsItem] | Unset = UNSET
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

        state: list[str] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = []
            for state_item_data in self.state:
                state_item: str = state_item_data
                state.append(state_item)

        monitor: list[str] | Unset = UNSET
        if not isinstance(self.monitor, Unset):
            monitor = self.monitor

        updated_since = self.updated_since

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
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if state is not UNSET:
            field_dict["state"] = state
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if updated_since is not UNSET:
            field_dict["updatedSince"] = updated_since
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
        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        _state = d.pop("state", UNSET)
        state: list[MaintenanceQueryRequestStateItem] | Unset = UNSET
        if _state is not UNSET:
            state = []
            for state_item_data in _state:
                state_item = check_maintenance_query_request_state_item(state_item_data)

                state.append(state_item)

        monitor = cast(list[str], d.pop("monitor", UNSET))

        updated_since = d.pop("updatedSince", UNSET)

        _sort = d.pop("sort", UNSET)
        sort: MaintenanceQueryRequestSort | Unset
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = check_maintenance_query_request_sort(_sort)

        _expand = d.pop("expand", UNSET)
        expand: list[MaintenanceQueryRequestExpandItem] | Unset = UNSET
        if _expand is not UNSET:
            expand = []
            for expand_item_data in _expand:
                expand_item = check_maintenance_query_request_expand_item(expand_item_data)

                expand.append(expand_item)

        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[MaintenanceQueryRequestFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = check_maintenance_query_request_fields_item(fields_item_data)

                fields.append(fields_item)

        maintenance_query_request = cls(
            from_=from_,
            to=to,
            state=state,
            monitor=monitor,
            updated_since=updated_since,
            sort=sort,
            expand=expand,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )

        return maintenance_query_request
