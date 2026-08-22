from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.monitor_incident_query_request_expand_item import (
    MonitorIncidentQueryRequestExpandItem,
    check_monitor_incident_query_request_expand_item,
)
from ..models.monitor_incident_query_request_fields_item import (
    MonitorIncidentQueryRequestFieldsItem,
    check_monitor_incident_query_request_fields_item,
)
from ..models.monitor_incident_query_request_severity_item import (
    MonitorIncidentQueryRequestSeverityItem,
    check_monitor_incident_query_request_severity_item,
)
from ..models.monitor_incident_query_request_state_item import (
    MonitorIncidentQueryRequestStateItem,
    check_monitor_incident_query_request_state_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorIncidentQueryRequest")


@_attrs_define
class MonitorIncidentQueryRequest:
    """The parameters, as one JSON object. A list-valued filter is a JSON array; everything else is a string, number or
    boolean. An omitted member and an explicit null both mean the parameter was not sent, and an empty array means it
    was sent empty - which every list filter refuses, exactly as it refuses an empty value on the query string.

    """

    from_: int | Unset = UNSET
    """ The start of the time window, in Unix seconds. """
    to: int | Unset = UNSET
    """ The end of the time window, in Unix seconds. """
    severity: list[MonitorIncidentQueryRequestSeverityItem] | Unset = UNSET
    """ `minor` | `major` | `critical`, ANY-OF. """
    state: list[MonitorIncidentQueryRequestStateItem] | Unset = UNSET
    """ `open` | `resolved` - ANY-OF. """
    expand: list[MonitorIncidentQueryRequestExpandItem] | Unset = UNSET
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
    fields: list[MonitorIncidentQueryRequestFieldsItem] | Unset = UNSET
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

        severity: list[str] | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = []
            for severity_item_data in self.severity:
                severity_item: str = severity_item_data
                severity.append(severity_item)

        state: list[str] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = []
            for state_item_data in self.state:
                state_item: str = state_item_data
                state.append(state_item)

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
        if severity is not UNSET:
            field_dict["severity"] = severity
        if state is not UNSET:
            field_dict["state"] = state
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

        _severity = d.pop("severity", UNSET)
        severity: list[MonitorIncidentQueryRequestSeverityItem] | Unset = UNSET
        if _severity is not UNSET:
            severity = []
            for severity_item_data in _severity:
                severity_item = check_monitor_incident_query_request_severity_item(severity_item_data)

                severity.append(severity_item)

        _state = d.pop("state", UNSET)
        state: list[MonitorIncidentQueryRequestStateItem] | Unset = UNSET
        if _state is not UNSET:
            state = []
            for state_item_data in _state:
                state_item = check_monitor_incident_query_request_state_item(state_item_data)

                state.append(state_item)

        _expand = d.pop("expand", UNSET)
        expand: list[MonitorIncidentQueryRequestExpandItem] | Unset = UNSET
        if _expand is not UNSET:
            expand = []
            for expand_item_data in _expand:
                expand_item = check_monitor_incident_query_request_expand_item(expand_item_data)

                expand.append(expand_item)

        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[MonitorIncidentQueryRequestFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = check_monitor_incident_query_request_fields_item(fields_item_data)

                fields.append(fields_item)

        monitor_incident_query_request = cls(
            from_=from_,
            to=to,
            severity=severity,
            state=state,
            expand=expand,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )

        return monitor_incident_query_request
