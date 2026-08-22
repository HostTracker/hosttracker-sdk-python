from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.notification_query_request_expand_item import (
    NotificationQueryRequestExpandItem,
    check_notification_query_request_expand_item,
)
from ..models.notification_query_request_fields_item import (
    NotificationQueryRequestFieldsItem,
    check_notification_query_request_fields_item,
)
from ..models.notification_query_request_outcome_item import (
    NotificationQueryRequestOutcomeItem,
    check_notification_query_request_outcome_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationQueryRequest")


@_attrs_define
class NotificationQueryRequest:
    """The parameters, as one JSON object. A list-valued filter is a JSON array; everything else is a string, number or
    boolean. An omitted member and an explicit null both mean the parameter was not sent, and an empty array means it
    was sent empty - which every list filter refuses, exactly as it refuses an empty value on the query string.

    """

    from_: int | Unset = UNSET
    """ Window start, Unix seconds. """
    to: int | Unset = UNSET
    """ Window end, Unix seconds. """
    contact: list[str] | Unset = UNSET
    """ Contact ids - the one relation the log is indexed by. """
    outcome: list[NotificationQueryRequestOutcomeItem] | Unset = UNSET
    """ Delivery outcomes, as the pipeline records them. Spelled `outcome`: the result of a DELIVERY is an outcome,
    the same word webhook deliveries and tests already use. """
    expand: list[NotificationQueryRequestExpandItem] | Unset = UNSET
    """ Declaration only - the VALUE is read from the raw query (a bound string cannot tell `?expand=` from an
    absent parameter, and keeps only the first of a repeated key). """
    limit: int | Unset = 50
    """ Rows to return. """
    cursor: str | Unset = UNSET
    """ Opaque cursor from a previous response's `nextCursor`. Absent ⇒ first page. """
    fields: list[NotificationQueryRequestFieldsItem] | Unset = UNSET
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

        contact: list[str] | Unset = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact

        outcome: list[str] | Unset = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = []
            for outcome_item_data in self.outcome:
                outcome_item: str = outcome_item_data
                outcome.append(outcome_item)

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
        if contact is not UNSET:
            field_dict["contact"] = contact
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
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

        contact = cast(list[str], d.pop("contact", UNSET))

        _outcome = d.pop("outcome", UNSET)
        outcome: list[NotificationQueryRequestOutcomeItem] | Unset = UNSET
        if _outcome is not UNSET:
            outcome = []
            for outcome_item_data in _outcome:
                outcome_item = check_notification_query_request_outcome_item(outcome_item_data)

                outcome.append(outcome_item)

        _expand = d.pop("expand", UNSET)
        expand: list[NotificationQueryRequestExpandItem] | Unset = UNSET
        if _expand is not UNSET:
            expand = []
            for expand_item_data in _expand:
                expand_item = check_notification_query_request_expand_item(expand_item_data)

                expand.append(expand_item)

        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[NotificationQueryRequestFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = check_notification_query_request_fields_item(fields_item_data)

                fields.append(fields_item)

        notification_query_request = cls(
            from_=from_,
            to=to,
            contact=contact,
            outcome=outcome,
            expand=expand,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )

        return notification_query_request
