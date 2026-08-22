from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.alert_by_contact_query_request_contact_type_item import (
    AlertByContactQueryRequestContactTypeItem,
    check_alert_by_contact_query_request_contact_type_item,
)
from ..models.alert_by_contact_query_request_fields_item import (
    AlertByContactQueryRequestFieldsItem,
    check_alert_by_contact_query_request_fields_item,
)
from ..models.alert_by_contact_query_request_monitor_type_item import (
    AlertByContactQueryRequestMonitorTypeItem,
    check_alert_by_contact_query_request_monitor_type_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertByContactQueryRequest")


@_attrs_define
class AlertByContactQueryRequest:
    """The parameters, as one JSON object. A list-valued filter is a JSON array; everything else is a string, number or
    boolean. An omitted member and an explicit null both mean the parameter was not sent, and an empty array means it
    was sent empty - which every list filter refuses, exactly as it refuses an empty value on the query string.

    """

    monitor_id: list[str] | Unset = UNSET
    """ See this operation's description for how this parameter narrows the result. """
    monitor_type: list[AlertByContactQueryRequestMonitorTypeItem] | Unset = UNSET
    """ See this operation's description for how this parameter narrows the result. """
    monitor_tag: list[str] | Unset = UNSET
    """ See this operation's description for how this parameter narrows the result. """
    monitor_url: list[str] | Unset = UNSET
    """ See this operation's description for how this parameter narrows the result. """
    monitor_like: bool | Unset = UNSET
    """ See this operation's description for how this parameter narrows the result. """
    monitor_q: str | Unset = UNSET
    """ See this operation's description for how this parameter narrows the result. """
    contact_id: list[str] | Unset = UNSET
    """ See this operation's description for how this parameter narrows the result. """
    contact_type: list[AlertByContactQueryRequestContactTypeItem] | Unset = UNSET
    """ See this operation's description for how this parameter narrows the result. """
    contact_confirmed: bool | Unset = UNSET
    """ See this operation's description for how this parameter narrows the result. """
    contact_q: str | Unset = UNSET
    """ See this operation's description for how this parameter narrows the result. """
    limit: int | Unset = 50
    """ Rows to return. """
    cursor: str | Unset = UNSET
    """ Opaque cursor from a previous response's `nextCursor`. Absent ⇒ first page. """
    fields: list[AlertByContactQueryRequestFieldsItem] | Unset = UNSET
    """ Which top-level members to keep on each row - `fields=id,name`. Everything else is dropped; `id` is always
    returned whether or not you name it, and the envelope (`data`, `nextCursor`, `hasMore`, `count`, `summary`) is
    never affected. A block an `expand=` adds is a member like any other, so `fields=id,monitor&expand=monitor`
    returns the id and the monitor block. An unrecognised name is refused, never dropped, and the refusal lists what
    this row publishes. `id` is accepted on every row, including the rows that publish no `id` member - there it
    simply keeps nothing, and a mask that would keep NOTHING at all (`fields=` or `fields=id` on such a row) is
    refused rather than answered with an empty object. """

    def to_dict(self) -> dict[str, Any]:
        monitor_id: list[str] | Unset = UNSET
        if not isinstance(self.monitor_id, Unset):
            monitor_id = self.monitor_id

        monitor_type: list[str] | Unset = UNSET
        if not isinstance(self.monitor_type, Unset):
            monitor_type = []
            for monitor_type_item_data in self.monitor_type:
                monitor_type_item: str = monitor_type_item_data
                monitor_type.append(monitor_type_item)

        monitor_tag: list[str] | Unset = UNSET
        if not isinstance(self.monitor_tag, Unset):
            monitor_tag = self.monitor_tag

        monitor_url: list[str] | Unset = UNSET
        if not isinstance(self.monitor_url, Unset):
            monitor_url = self.monitor_url

        monitor_like = self.monitor_like

        monitor_q = self.monitor_q

        contact_id: list[str] | Unset = UNSET
        if not isinstance(self.contact_id, Unset):
            contact_id = self.contact_id

        contact_type: list[str] | Unset = UNSET
        if not isinstance(self.contact_type, Unset):
            contact_type = []
            for contact_type_item_data in self.contact_type:
                contact_type_item: str = contact_type_item_data
                contact_type.append(contact_type_item)

        contact_confirmed = self.contact_confirmed

        contact_q = self.contact_q

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
        if monitor_id is not UNSET:
            field_dict["monitor.id"] = monitor_id
        if monitor_type is not UNSET:
            field_dict["monitor.type"] = monitor_type
        if monitor_tag is not UNSET:
            field_dict["monitor.tag"] = monitor_tag
        if monitor_url is not UNSET:
            field_dict["monitor.url"] = monitor_url
        if monitor_like is not UNSET:
            field_dict["monitor.like"] = monitor_like
        if monitor_q is not UNSET:
            field_dict["monitor.q"] = monitor_q
        if contact_id is not UNSET:
            field_dict["contact.id"] = contact_id
        if contact_type is not UNSET:
            field_dict["contact.type"] = contact_type
        if contact_confirmed is not UNSET:
            field_dict["contact.confirmed"] = contact_confirmed
        if contact_q is not UNSET:
            field_dict["contact.q"] = contact_q
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
        monitor_id = cast(list[str], d.pop("monitor.id", UNSET))

        _monitor_type = d.pop("monitor.type", UNSET)
        monitor_type: list[AlertByContactQueryRequestMonitorTypeItem] | Unset = UNSET
        if _monitor_type is not UNSET:
            monitor_type = []
            for monitor_type_item_data in _monitor_type:
                monitor_type_item = check_alert_by_contact_query_request_monitor_type_item(monitor_type_item_data)

                monitor_type.append(monitor_type_item)

        monitor_tag = cast(list[str], d.pop("monitor.tag", UNSET))

        monitor_url = cast(list[str], d.pop("monitor.url", UNSET))

        monitor_like = d.pop("monitor.like", UNSET)

        monitor_q = d.pop("monitor.q", UNSET)

        contact_id = cast(list[str], d.pop("contact.id", UNSET))

        _contact_type = d.pop("contact.type", UNSET)
        contact_type: list[AlertByContactQueryRequestContactTypeItem] | Unset = UNSET
        if _contact_type is not UNSET:
            contact_type = []
            for contact_type_item_data in _contact_type:
                contact_type_item = check_alert_by_contact_query_request_contact_type_item(contact_type_item_data)

                contact_type.append(contact_type_item)

        contact_confirmed = d.pop("contact.confirmed", UNSET)

        contact_q = d.pop("contact.q", UNSET)

        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[AlertByContactQueryRequestFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = check_alert_by_contact_query_request_fields_item(fields_item_data)

                fields.append(fields_item)

        alert_by_contact_query_request = cls(
            monitor_id=monitor_id,
            monitor_type=monitor_type,
            monitor_tag=monitor_tag,
            monitor_url=monitor_url,
            monitor_like=monitor_like,
            monitor_q=monitor_q,
            contact_id=contact_id,
            contact_type=contact_type,
            contact_confirmed=contact_confirmed,
            contact_q=contact_q,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )

        return alert_by_contact_query_request
