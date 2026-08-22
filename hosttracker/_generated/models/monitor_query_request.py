from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.monitor_query_request_expand_item import (
    MonitorQueryRequestExpandItem,
    check_monitor_query_request_expand_item,
)
from ..models.monitor_query_request_fields_item import (
    MonitorQueryRequestFieldsItem,
    check_monitor_query_request_fields_item,
)
from ..models.monitor_query_request_preset_item import (
    MonitorQueryRequestPresetItem,
    check_monitor_query_request_preset_item,
)
from ..models.monitor_query_request_sort import MonitorQueryRequestSort, check_monitor_query_request_sort
from ..models.monitor_query_request_state_item import (
    MonitorQueryRequestStateItem,
    check_monitor_query_request_state_item,
)
from ..models.monitor_query_request_type_item import MonitorQueryRequestTypeItem, check_monitor_query_request_type_item
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitorQueryRequest")


@_attrs_define
class MonitorQueryRequest:
    """The parameters, as one JSON object. A list-valued filter is a JSON array; everything else is a string, number or
    boolean. An omitted member and an explicit null both mean the parameter was not sent, and an empty array means it
    was sent empty - which every list filter refuses, exactly as it refuses an empty value on the query string.

    """

    id: list[str] | Unset = UNSET
    """ Explicit ids. An OMITTED list means NONE - never "all"; an omitted PARAMETER is no filter. """
    type_: list[MonitorQueryRequestTypeItem] | Unset = UNSET
    """ One or more of the 14 v2 type tokens. An unknown token is 422, never a silently empty page. """
    include_id: list[str] | Unset = UNSET
    """ Ids to include in the answer WHATEVER the other filters say - the "keep the rows I have selected visible"
    knob a dashboard needs when the user narrows the list under a live selection. It is a UNION on top of the
    filtered set, not a filter: `state=down&includeId=X` answers every down monitor PLUS X, even when X is up. `id=`
    beside it still narrows, so `id=A,B&includeId=C` answers A, B and C. ⚠ It participates in the ORDER, so the page
    it lands on is wherever the sort puts it - it is not pinned to the top. And it is bounded by `limit` like every
    other row. """
    preset: list[MonitorQueryRequestPresetItem] | Unset = UNSET
    """ Monitors built from a server-side settings PRESET - today the single value `bl:ru`, the Russian blacklist
    check. **Why it is not a type filter.** A Russian-blacklist monitor is stored as `type: "http"` carrying
    `settings.preset: "bl:ru"` - so `type=` cannot select it and, before this filter, nothing could: the rows were
    visible only by reading every http monitor's settings. """
    open_stat: bool | Unset = UNSET
    """ Whether the monitor's statistics are publicly shared - the row's own `openStat` member. """
    tag: list[str] | Unset = UNSET
    """ Tags, matched exactly (storage keeps them as one comma-separated column). """
    state: list[MonitorQueryRequestStateItem] | Unset = UNSET
    """ `up` | `down` | `paused` | `maintenance`, any combination. """
    enabled: bool | Unset = UNSET
    """ The CONFIGURED flag, matching the resource's own `enabled` member. For "not actually being monitored" -
    which includes an over-limit monitor whose `enabled` is still true - use `state=paused`. One concept per name.
    """
    q: str | Unset = UNSET
    """ Case-insensitive substring over name AND url - the single replacement for the search-like pair. """
    url: list[str] | Unset = UNSET
    """ Address filter - the same spelling the result and incident reads take: list-accepting, matched against the
    monitor's address, exact (case-insensitive) unless `like=true`. ANY-OF, ANDed with the other filters like every
    filter on this list. """
    like: bool | Unset = UNSET
    """ `true` switches `url=` from exact match to case-insensitive SUBSTRING match. Refused without `url=`, never
    silently ignored. """
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
    from_: int | Unset = UNSET
    """ Window start, Unix seconds - read by the INTERVAL-scoped expands. """
    to: int | Unset = UNSET
    """ Window end, Unix seconds. """
    sort: MonitorQueryRequestSort | Unset = UNSET
    """ `name` | `state` | `type` | `interval` | `lastChange` | `url` | `tags` | `created`, optionally suffixed with
    `:asc` or `:desc` (`sort=name:desc`). Unsuffixed takes the column's natural direction - the two time columns
    (`lastChange`, `created`) newest-first, everything else A→Z. There is no separate `order=` parameter: sending
    one is `422 unknown_parameter`. `tags` orders by the monitor's tag list compared as text - in practice its FIRST
    tag alphabetically, with the next tag breaking a tie between two monitors that share the first, and the monitor
    id breaking the rest. A monitor with no tags sorts first ascending. """
    paused_last: bool | Unset = UNSET
    """ Order every monitor that is NOT being checked (`state: "paused"` - switched off, or suspended by a package
    limit) AFTER every monitor that is, whatever `sort=` says. **A separate knob rather than a change to each
    column's natural order**, deliberately: `sort=name` means A→Z, and quietly answering two alphabetical blocks
    instead would make a documented order wrong for every caller who never asked for the grouping. Default off, so
    no shipped ordering moves. The grouping is ABSOLUTE - `:desc` reverses the column, never the grouping - and it
    is part of the ordering a cursor addresses: replaying a cursor minted with it under a request without it (or the
    reverse) is `422 invalid_cursor`, like any other change of order mid-walk. """
    expand: list[MonitorQueryRequestExpandItem] | Unset = UNSET
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
    fields: list[MonitorQueryRequestFieldsItem] | Unset = UNSET
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

        include_id: list[str] | Unset = UNSET
        if not isinstance(self.include_id, Unset):
            include_id = self.include_id

        preset: list[str] | Unset = UNSET
        if not isinstance(self.preset, Unset):
            preset = []
            for preset_item_data in self.preset:
                preset_item: str = preset_item_data
                preset.append(preset_item)

        open_stat = self.open_stat

        tag: list[str] | Unset = UNSET
        if not isinstance(self.tag, Unset):
            tag = self.tag

        state: list[str] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = []
            for state_item_data in self.state:
                state_item: str = state_item_data
                state.append(state_item)

        enabled = self.enabled

        q = self.q

        url: list[str] | Unset = UNSET
        if not isinstance(self.url, Unset):
            url = self.url

        like = self.like

        updated_since = self.updated_since

        from_ = self.from_

        to = self.to

        sort: str | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort

        paused_last = self.paused_last

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
        if include_id is not UNSET:
            field_dict["includeId"] = include_id
        if preset is not UNSET:
            field_dict["preset"] = preset
        if open_stat is not UNSET:
            field_dict["openStat"] = open_stat
        if tag is not UNSET:
            field_dict["tag"] = tag
        if state is not UNSET:
            field_dict["state"] = state
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if q is not UNSET:
            field_dict["q"] = q
        if url is not UNSET:
            field_dict["url"] = url
        if like is not UNSET:
            field_dict["like"] = like
        if updated_since is not UNSET:
            field_dict["updatedSince"] = updated_since
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if sort is not UNSET:
            field_dict["sort"] = sort
        if paused_last is not UNSET:
            field_dict["pausedLast"] = paused_last
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
        type_: list[MonitorQueryRequestTypeItem] | Unset = UNSET
        if _type_ is not UNSET:
            type_ = []
            for type_item_data in _type_:
                type_item = check_monitor_query_request_type_item(type_item_data)

                type_.append(type_item)

        include_id = cast(list[str], d.pop("includeId", UNSET))

        _preset = d.pop("preset", UNSET)
        preset: list[MonitorQueryRequestPresetItem] | Unset = UNSET
        if _preset is not UNSET:
            preset = []
            for preset_item_data in _preset:
                preset_item = check_monitor_query_request_preset_item(preset_item_data)

                preset.append(preset_item)

        open_stat = d.pop("openStat", UNSET)

        tag = cast(list[str], d.pop("tag", UNSET))

        _state = d.pop("state", UNSET)
        state: list[MonitorQueryRequestStateItem] | Unset = UNSET
        if _state is not UNSET:
            state = []
            for state_item_data in _state:
                state_item = check_monitor_query_request_state_item(state_item_data)

                state.append(state_item)

        enabled = d.pop("enabled", UNSET)

        q = d.pop("q", UNSET)

        url = cast(list[str], d.pop("url", UNSET))

        like = d.pop("like", UNSET)

        updated_since = d.pop("updatedSince", UNSET)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        _sort = d.pop("sort", UNSET)
        sort: MonitorQueryRequestSort | Unset
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = check_monitor_query_request_sort(_sort)

        paused_last = d.pop("pausedLast", UNSET)

        _expand = d.pop("expand", UNSET)
        expand: list[MonitorQueryRequestExpandItem] | Unset = UNSET
        if _expand is not UNSET:
            expand = []
            for expand_item_data in _expand:
                expand_item = check_monitor_query_request_expand_item(expand_item_data)

                expand.append(expand_item)

        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[MonitorQueryRequestFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = check_monitor_query_request_fields_item(fields_item_data)

                fields.append(fields_item)

        monitor_query_request = cls(
            id=id,
            type_=type_,
            include_id=include_id,
            preset=preset,
            open_stat=open_stat,
            tag=tag,
            state=state,
            enabled=enabled,
            q=q,
            url=url,
            like=like,
            updated_since=updated_since,
            from_=from_,
            to=to,
            sort=sort,
            paused_last=paused_last,
            expand=expand,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )

        return monitor_query_request
