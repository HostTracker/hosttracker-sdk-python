from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.webhook_delivery_query_request_event_item import (
    WebhookDeliveryQueryRequestEventItem,
    check_webhook_delivery_query_request_event_item,
)
from ..models.webhook_delivery_query_request_fields_item import (
    WebhookDeliveryQueryRequestFieldsItem,
    check_webhook_delivery_query_request_fields_item,
)
from ..models.webhook_delivery_query_request_outcome_item import (
    WebhookDeliveryQueryRequestOutcomeItem,
    check_webhook_delivery_query_request_outcome_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookDeliveryQueryRequest")


@_attrs_define
class WebhookDeliveryQueryRequest:
    """The parameters, as one JSON object. A list-valued filter is a JSON array; everything else is a string, number or
    boolean. An omitted member and an explicit null both mean the parameter was not sent, and an empty array means it
    was sent empty - which every list filter refuses, exactly as it refuses an empty value on the query string.

    """

    from_: int | Unset = UNSET
    """ Window start, Unix seconds. """
    to: int | Unset = UNSET
    """ Window end, Unix seconds. """
    event: list[WebhookDeliveryQueryRequestEventItem] | Unset = UNSET
    """ Event tokens. """
    outcome: list[WebhookDeliveryQueryRequestOutcomeItem] | Unset = UNSET
    """ Delivery outcomes. """
    limit: int | Unset = 50
    """ Rows to return. """
    cursor: str | Unset = UNSET
    """ Opaque cursor from a previous response's `nextCursor`. Absent ⇒ first page. """
    fields: list[WebhookDeliveryQueryRequestFieldsItem] | Unset = UNSET
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

        event: list[str] | Unset = UNSET
        if not isinstance(self.event, Unset):
            event = []
            for event_item_data in self.event:
                event_item: str = event_item_data
                event.append(event_item)

        outcome: list[str] | Unset = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = []
            for outcome_item_data in self.outcome:
                outcome_item: str = outcome_item_data
                outcome.append(outcome_item)

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
        if event is not UNSET:
            field_dict["event"] = event
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
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

        _event = d.pop("event", UNSET)
        event: list[WebhookDeliveryQueryRequestEventItem] | Unset = UNSET
        if _event is not UNSET:
            event = []
            for event_item_data in _event:
                event_item = check_webhook_delivery_query_request_event_item(event_item_data)

                event.append(event_item)

        _outcome = d.pop("outcome", UNSET)
        outcome: list[WebhookDeliveryQueryRequestOutcomeItem] | Unset = UNSET
        if _outcome is not UNSET:
            outcome = []
            for outcome_item_data in _outcome:
                outcome_item = check_webhook_delivery_query_request_outcome_item(outcome_item_data)

                outcome.append(outcome_item)

        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[WebhookDeliveryQueryRequestFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = check_webhook_delivery_query_request_fields_item(fields_item_data)

                fields.append(fields_item)

        webhook_delivery_query_request = cls(
            from_=from_,
            to=to,
            event=event,
            outcome=outcome,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )

        return webhook_delivery_query_request
