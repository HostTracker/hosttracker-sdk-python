from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.webhook_query_request_fields_item import (
    WebhookQueryRequestFieldsItem,
    check_webhook_query_request_fields_item,
)
from ..models.webhook_query_request_sort import WebhookQueryRequestSort, check_webhook_query_request_sort
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookQueryRequest")


@_attrs_define
class WebhookQueryRequest:
    """The parameters, as one JSON object. A list-valued filter is a JSON array; everything else is a string, number or
    boolean. An omitted member and an explicit null both mean the parameter was not sent, and an empty array means it
    was sent empty - which every list filter refuses, exactly as it refuses an empty value on the query string.

    """

    sort: WebhookQueryRequestSort | Unset = UNSET
    """ `created` | `updated` | `name` | `url`, optionally suffixed `:asc`/`:desc`. """
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
    limit: int | Unset = 50
    """ Rows to return. """
    cursor: str | Unset = UNSET
    """ Opaque cursor from a previous response's `nextCursor`. Absent ⇒ first page. """
    fields: list[WebhookQueryRequestFieldsItem] | Unset = UNSET
    """ Which top-level members to keep on each row - `fields=id,name`. Everything else is dropped; `id` is always
    returned whether or not you name it, and the envelope (`data`, `nextCursor`, `hasMore`, `count`, `summary`) is
    never affected. A block an `expand=` adds is a member like any other, so `fields=id,monitor&expand=monitor`
    returns the id and the monitor block. An unrecognised name is refused, never dropped, and the refusal lists what
    this row publishes. `id` is accepted on every row, including the rows that publish no `id` member - there it
    simply keeps nothing, and a mask that would keep NOTHING at all (`fields=` or `fields=id` on such a row) is
    refused rather than answered with an empty object. """

    def to_dict(self) -> dict[str, Any]:
        sort: str | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort

        updated_since = self.updated_since

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
        if sort is not UNSET:
            field_dict["sort"] = sort
        if updated_since is not UNSET:
            field_dict["updatedSince"] = updated_since
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
        _sort = d.pop("sort", UNSET)
        sort: WebhookQueryRequestSort | Unset
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = check_webhook_query_request_sort(_sort)

        updated_since = d.pop("updatedSince", UNSET)

        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[WebhookQueryRequestFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = check_webhook_query_request_fields_item(fields_item_data)

                fields.append(fields_item)

        webhook_query_request = cls(
            sort=sort,
            updated_since=updated_since,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )

        return webhook_query_request
