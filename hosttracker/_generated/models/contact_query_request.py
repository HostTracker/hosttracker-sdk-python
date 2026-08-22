from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.contact_query_request_expand_item import (
    ContactQueryRequestExpandItem,
    check_contact_query_request_expand_item,
)
from ..models.contact_query_request_fields_item import (
    ContactQueryRequestFieldsItem,
    check_contact_query_request_fields_item,
)
from ..models.contact_query_request_sort import ContactQueryRequestSort, check_contact_query_request_sort
from ..models.contact_query_request_type_item import ContactQueryRequestTypeItem, check_contact_query_request_type_item
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactQueryRequest")


@_attrs_define
class ContactQueryRequest:
    """The parameters, as one JSON object. A list-valued filter is a JSON array; everything else is a string, number or
    boolean. An omitted member and an explicit null both mean the parameter was not sent, and an empty array means it
    was sent empty - which every list filter refuses, exactly as it refuses an empty value on the query string.

    """

    id: list[str] | Unset = UNSET
    """ Explicit ids. A PRESENT-but-empty value selects NOTHING; an absent parameter is no filter. """
    type_: list[ContactQueryRequestTypeItem] | Unset = UNSET
    """ One or more contact-type tokens; a row matching any of them is returned. An unknown token is refused rather
    than silently returning an empty page. `skype` is a retired channel that cannot be created - it is accepted here
    only so an account holding legacy rows can still find them. """
    confirmed: bool | Unset = UNSET
    """ Restrict to confirmed, or to unconfirmed. """
    q: str | Unset = UNSET
    """ Case-insensitive substring over name AND address. """
    updated_since: str | Unset = UNSET
    """ Return only what changed since this point - either Unix seconds, or the `syncCursor` a previous response
    returned. This is what makes a poll loop cheap. **⚠ It compares against `updated`, which is the contact's
    CREATION instant only - a configuration edit does not move it.** A rename, an
    `alertDelay`/`language`/`activePeriod` change, or `confirmed` flipping true is invisible to this filter, because
    storage records no modification time for a contact. Subscribe to the `contact.updated` webhook (and
    `contact.confirmed` for the confirmation transition) to hear about an edit this poll cannot see. """
    sort: ContactQueryRequestSort | Unset = UNSET
    """ `created` | `name` | `address`, optionally suffixed with `:asc` or `:desc` (`sort=name:desc`). Unsuffixed
    takes the column's natural direction - `created` newest-first, the two text columns A→Z. There is no separate
    `order=` parameter: sending one is `422 unknown_parameter`. """
    expand: list[ContactQueryRequestExpandItem] | Unset = UNSET
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
    fields: list[ContactQueryRequestFieldsItem] | Unset = UNSET
    """ Which top-level members to keep on each row - `fields=id,name`. Everything else is dropped; `id` is always
    returned whether or not you name it, and the envelope (`data`, `nextCursor`, `hasMore`, `count`, `summary`) is
    never affected. A block an `expand=` adds is a member like any other, so `fields=id,monitor&expand=monitor`
    returns the id and the monitor block. An unrecognised name is refused, never dropped, and the refusal lists what
    this row publishes. `id` is accepted on every row, including the rows that publish no `id` member - there it
    simply keeps nothing, and a mask that would keep NOTHING at all (`fields=` or `fields=id` on such a row) is
    refused rather than answered with an empty object. """

    def to_dict(self) -> dict[str, Any]:
        id: list[str] | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = self.id

        type_: list[str] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = []
            for type_item_data in self.type_:
                type_item: str = type_item_data
                type_.append(type_item)

        confirmed = self.confirmed

        q = self.q

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
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if confirmed is not UNSET:
            field_dict["confirmed"] = confirmed
        if q is not UNSET:
            field_dict["q"] = q
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
        id = cast(list[str], d.pop("id", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: list[ContactQueryRequestTypeItem] | Unset = UNSET
        if _type_ is not UNSET:
            type_ = []
            for type_item_data in _type_:
                type_item = check_contact_query_request_type_item(type_item_data)

                type_.append(type_item)

        confirmed = d.pop("confirmed", UNSET)

        q = d.pop("q", UNSET)

        updated_since = d.pop("updatedSince", UNSET)

        _sort = d.pop("sort", UNSET)
        sort: ContactQueryRequestSort | Unset
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = check_contact_query_request_sort(_sort)

        _expand = d.pop("expand", UNSET)
        expand: list[ContactQueryRequestExpandItem] | Unset = UNSET
        if _expand is not UNSET:
            expand = []
            for expand_item_data in _expand:
                expand_item = check_contact_query_request_expand_item(expand_item_data)

                expand.append(expand_item)

        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[ContactQueryRequestFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = check_contact_query_request_fields_item(fields_item_data)

                fields.append(fields_item)

        contact_query_request = cls(
            id=id,
            type_=type_,
            confirmed=confirmed,
            q=q,
            updated_since=updated_since,
            sort=sort,
            expand=expand,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )

        return contact_query_request
