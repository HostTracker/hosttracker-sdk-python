from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_cursor import InvalidCursor
from ...models.invalid_limit import InvalidLimit
from ...models.invalid_range import InvalidRange
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.list_monitor_expand_item import ListMonitorExpandItem
from ...models.list_monitor_fields_item import ListMonitorFieldsItem
from ...models.list_monitor_preset_item import ListMonitorPresetItem
from ...models.list_monitor_sort import ListMonitorSort
from ...models.list_monitor_state_item import ListMonitorStateItem
from ...models.list_monitor_type_item import ListMonitorTypeItem
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.monitor_page import MonitorPage
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_expand import UnknownExpand
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: list[str] | Unset = UNSET,
    type_: list[ListMonitorTypeItem] | Unset = UNSET,
    include_id: list[str] | Unset = UNSET,
    preset: list[ListMonitorPresetItem] | Unset = UNSET,
    open_stat: bool | Unset = UNSET,
    tag: list[str] | Unset = UNSET,
    state: list[ListMonitorStateItem] | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    url_query: list[str] | Unset = UNSET,
    like: bool | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    sort: ListMonitorSort | Unset = UNSET,
    paused_last: bool | Unset = UNSET,
    expand: list[ListMonitorExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: list[str] | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = id

    params["id"] = json_id

    json_type_: list[str] | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = []
        for type_item_data in type_:
            type_item: str = type_item_data
            json_type_.append(type_item)

    params["type"] = json_type_

    json_include_id: list[str] | Unset = UNSET
    if not isinstance(include_id, Unset):
        json_include_id = include_id

    params["includeId"] = json_include_id

    json_preset: list[str] | Unset = UNSET
    if not isinstance(preset, Unset):
        json_preset = []
        for preset_item_data in preset:
            preset_item: str = preset_item_data
            json_preset.append(preset_item)

    params["preset"] = json_preset

    params["openStat"] = open_stat

    json_tag: list[str] | Unset = UNSET
    if not isinstance(tag, Unset):
        json_tag = tag

    params["tag"] = json_tag

    json_state: list[str] | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item: str = state_item_data
            json_state.append(state_item)

    params["state"] = json_state

    params["enabled"] = enabled

    params["q"] = q

    json_url_query: list[str] | Unset = UNSET
    if not isinstance(url_query, Unset):
        json_url_query = url_query

    params["url"] = json_url_query

    params["like"] = like

    params["updatedSince"] = updated_since

    params["from"] = from_

    params["to"] = to

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["pausedLast"] = paused_last

    json_expand: list[str] | Unset = UNSET
    if not isinstance(expand, Unset):
        json_expand = []
        for expand_item_data in expand:
            expand_item: str = expand_item_data
            json_expand.append(expand_item)

    params["expand"] = json_expand

    params["limit"] = limit

    params["cursor"] = cursor

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item: str = fields_item_data
            json_fields.append(fields_item)

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/monitor",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | MonitorPage
    | QuotaExceeded
    | None
):
    if response.status_code == 200:
        response_200 = MonitorPage.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = InvalidToken.from_dict(response.json())

        return response_401

    if response.status_code == 403:

        def _parse_response_403(data: object) -> InsufficientRights | IpNotAllowed | MissingScope:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_0 = MissingScope.from_dict(data)

                return response_403_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_1 = InsufficientRights.from_dict(data)

                return response_403_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_403_type_2 = IpNotAllowed.from_dict(data)

            return response_403_type_2

        response_403 = _parse_response_403(response.json())

        return response_403

    if response.status_code == 405:
        response_405 = MethodNotAllowed.from_dict(response.json())

        return response_405

    if response.status_code == 422:

        def _parse_response_422(
            data: object,
        ) -> (
            InvalidCursor
            | InvalidLimit
            | InvalidRange
            | UnknownEnumValue
            | UnknownExpand
            | UnknownField
            | UnknownParameter
            | ValidationFailed
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = UnknownExpand.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_1 = UnknownField.from_dict(data)

                return response_422_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_2 = ValidationFailed.from_dict(data)

                return response_422_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_3 = InvalidCursor.from_dict(data)

                return response_422_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_4 = InvalidLimit.from_dict(data)

                return response_422_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_5 = InvalidRange.from_dict(data)

                return response_422_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_6 = UnknownEnumValue.from_dict(data)

                return response_422_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_7 = UnknownParameter.from_dict(data)

            return response_422_type_7

        response_422 = _parse_response_422(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = QuotaExceeded.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = InternalError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | MonitorPage
    | QuotaExceeded
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: list[str] | Unset = UNSET,
    type_: list[ListMonitorTypeItem] | Unset = UNSET,
    include_id: list[str] | Unset = UNSET,
    preset: list[ListMonitorPresetItem] | Unset = UNSET,
    open_stat: bool | Unset = UNSET,
    tag: list[str] | Unset = UNSET,
    state: list[ListMonitorStateItem] | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    url_query: list[str] | Unset = UNSET,
    like: bool | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    sort: ListMonitorSort | Unset = UNSET,
    paused_last: bool | Unset = UNSET,
    expand: list[ListMonitorExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorFieldsItem] | Unset = UNSET,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | MonitorPage
    | QuotaExceeded
]:
    """List the account's monitors, filtered, sorted and cursor-paginated.

     Returns a page of monitors in a lean projection - identity, type, url, state, tags and the share and
    logging flags - so a dashboard read costs one call. Narrow the set with id, type, tag, state,
    enabled, openStat, preset or the free-text q filter, and use expand to embed settings,
    subscriptions, the last incident, the last check result, uptime, state spans or account-wide
    aggregates in the same response. Send includeId to keep named monitors in the answer whatever the
    filters say - what a dashboard needs to keep a live selection visible while the user narrows the
    list. For an incremental poll, send updatedSince with the syncCursor the previous response returned
    instead of re-reading the whole account. Order it with
    sort=name|state|type|interval|lastChange|url|tags|created, optionally suffixed :asc or :desc
    (sort=name:desc); without a suffix each column takes its natural direction - the time columns
    lastChange and created newest-first, everything else A to Z. There is no separate order parameter.
    Add pausedLast=true to push every monitor that is not actually being checked to the end, whatever
    the sort column is. expand=summary returns the ten largest domains in topDomains; the count is
    fixed.

    Args:
        id (list[str] | Unset):
        type_ (list[ListMonitorTypeItem] | Unset):
        include_id (list[str] | Unset):
        preset (list[ListMonitorPresetItem] | Unset):
        open_stat (bool | Unset):
        tag (list[str] | Unset):
        state (list[ListMonitorStateItem] | Unset):
        enabled (bool | Unset):
        q (str | Unset):
        url_query (list[str] | Unset):
        like (bool | Unset):
        updated_since (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        sort (ListMonitorSort | Unset):
        paused_last (bool | Unset):
        expand (list[ListMonitorExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMonitorFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | MonitorPage | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        id=id,
        type_=type_,
        include_id=include_id,
        preset=preset,
        open_stat=open_stat,
        tag=tag,
        state=state,
        enabled=enabled,
        q=q,
        url_query=url_query,
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

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: list[str] | Unset = UNSET,
    type_: list[ListMonitorTypeItem] | Unset = UNSET,
    include_id: list[str] | Unset = UNSET,
    preset: list[ListMonitorPresetItem] | Unset = UNSET,
    open_stat: bool | Unset = UNSET,
    tag: list[str] | Unset = UNSET,
    state: list[ListMonitorStateItem] | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    url_query: list[str] | Unset = UNSET,
    like: bool | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    sort: ListMonitorSort | Unset = UNSET,
    paused_last: bool | Unset = UNSET,
    expand: list[ListMonitorExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorFieldsItem] | Unset = UNSET,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | MonitorPage
    | QuotaExceeded
    | None
):
    """List the account's monitors, filtered, sorted and cursor-paginated.

     Returns a page of monitors in a lean projection - identity, type, url, state, tags and the share and
    logging flags - so a dashboard read costs one call. Narrow the set with id, type, tag, state,
    enabled, openStat, preset or the free-text q filter, and use expand to embed settings,
    subscriptions, the last incident, the last check result, uptime, state spans or account-wide
    aggregates in the same response. Send includeId to keep named monitors in the answer whatever the
    filters say - what a dashboard needs to keep a live selection visible while the user narrows the
    list. For an incremental poll, send updatedSince with the syncCursor the previous response returned
    instead of re-reading the whole account. Order it with
    sort=name|state|type|interval|lastChange|url|tags|created, optionally suffixed :asc or :desc
    (sort=name:desc); without a suffix each column takes its natural direction - the time columns
    lastChange and created newest-first, everything else A to Z. There is no separate order parameter.
    Add pausedLast=true to push every monitor that is not actually being checked to the end, whatever
    the sort column is. expand=summary returns the ten largest domains in topDomains; the count is
    fixed.

    Args:
        id (list[str] | Unset):
        type_ (list[ListMonitorTypeItem] | Unset):
        include_id (list[str] | Unset):
        preset (list[ListMonitorPresetItem] | Unset):
        open_stat (bool | Unset):
        tag (list[str] | Unset):
        state (list[ListMonitorStateItem] | Unset):
        enabled (bool | Unset):
        q (str | Unset):
        url_query (list[str] | Unset):
        like (bool | Unset):
        updated_since (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        sort (ListMonitorSort | Unset):
        paused_last (bool | Unset):
        expand (list[ListMonitorExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMonitorFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | MonitorPage | QuotaExceeded
    """

    return sync_detailed(
        client=client,
        id=id,
        type_=type_,
        include_id=include_id,
        preset=preset,
        open_stat=open_stat,
        tag=tag,
        state=state,
        enabled=enabled,
        q=q,
        url_query=url_query,
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
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: list[str] | Unset = UNSET,
    type_: list[ListMonitorTypeItem] | Unset = UNSET,
    include_id: list[str] | Unset = UNSET,
    preset: list[ListMonitorPresetItem] | Unset = UNSET,
    open_stat: bool | Unset = UNSET,
    tag: list[str] | Unset = UNSET,
    state: list[ListMonitorStateItem] | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    url_query: list[str] | Unset = UNSET,
    like: bool | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    sort: ListMonitorSort | Unset = UNSET,
    paused_last: bool | Unset = UNSET,
    expand: list[ListMonitorExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorFieldsItem] | Unset = UNSET,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | MonitorPage
    | QuotaExceeded
]:
    """List the account's monitors, filtered, sorted and cursor-paginated.

     Returns a page of monitors in a lean projection - identity, type, url, state, tags and the share and
    logging flags - so a dashboard read costs one call. Narrow the set with id, type, tag, state,
    enabled, openStat, preset or the free-text q filter, and use expand to embed settings,
    subscriptions, the last incident, the last check result, uptime, state spans or account-wide
    aggregates in the same response. Send includeId to keep named monitors in the answer whatever the
    filters say - what a dashboard needs to keep a live selection visible while the user narrows the
    list. For an incremental poll, send updatedSince with the syncCursor the previous response returned
    instead of re-reading the whole account. Order it with
    sort=name|state|type|interval|lastChange|url|tags|created, optionally suffixed :asc or :desc
    (sort=name:desc); without a suffix each column takes its natural direction - the time columns
    lastChange and created newest-first, everything else A to Z. There is no separate order parameter.
    Add pausedLast=true to push every monitor that is not actually being checked to the end, whatever
    the sort column is. expand=summary returns the ten largest domains in topDomains; the count is
    fixed.

    Args:
        id (list[str] | Unset):
        type_ (list[ListMonitorTypeItem] | Unset):
        include_id (list[str] | Unset):
        preset (list[ListMonitorPresetItem] | Unset):
        open_stat (bool | Unset):
        tag (list[str] | Unset):
        state (list[ListMonitorStateItem] | Unset):
        enabled (bool | Unset):
        q (str | Unset):
        url_query (list[str] | Unset):
        like (bool | Unset):
        updated_since (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        sort (ListMonitorSort | Unset):
        paused_last (bool | Unset):
        expand (list[ListMonitorExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMonitorFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | MonitorPage | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        id=id,
        type_=type_,
        include_id=include_id,
        preset=preset,
        open_stat=open_stat,
        tag=tag,
        state=state,
        enabled=enabled,
        q=q,
        url_query=url_query,
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

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: list[str] | Unset = UNSET,
    type_: list[ListMonitorTypeItem] | Unset = UNSET,
    include_id: list[str] | Unset = UNSET,
    preset: list[ListMonitorPresetItem] | Unset = UNSET,
    open_stat: bool | Unset = UNSET,
    tag: list[str] | Unset = UNSET,
    state: list[ListMonitorStateItem] | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    url_query: list[str] | Unset = UNSET,
    like: bool | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    sort: ListMonitorSort | Unset = UNSET,
    paused_last: bool | Unset = UNSET,
    expand: list[ListMonitorExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorFieldsItem] | Unset = UNSET,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | MonitorPage
    | QuotaExceeded
    | None
):
    """List the account's monitors, filtered, sorted and cursor-paginated.

     Returns a page of monitors in a lean projection - identity, type, url, state, tags and the share and
    logging flags - so a dashboard read costs one call. Narrow the set with id, type, tag, state,
    enabled, openStat, preset or the free-text q filter, and use expand to embed settings,
    subscriptions, the last incident, the last check result, uptime, state spans or account-wide
    aggregates in the same response. Send includeId to keep named monitors in the answer whatever the
    filters say - what a dashboard needs to keep a live selection visible while the user narrows the
    list. For an incremental poll, send updatedSince with the syncCursor the previous response returned
    instead of re-reading the whole account. Order it with
    sort=name|state|type|interval|lastChange|url|tags|created, optionally suffixed :asc or :desc
    (sort=name:desc); without a suffix each column takes its natural direction - the time columns
    lastChange and created newest-first, everything else A to Z. There is no separate order parameter.
    Add pausedLast=true to push every monitor that is not actually being checked to the end, whatever
    the sort column is. expand=summary returns the ten largest domains in topDomains; the count is
    fixed.

    Args:
        id (list[str] | Unset):
        type_ (list[ListMonitorTypeItem] | Unset):
        include_id (list[str] | Unset):
        preset (list[ListMonitorPresetItem] | Unset):
        open_stat (bool | Unset):
        tag (list[str] | Unset):
        state (list[ListMonitorStateItem] | Unset):
        enabled (bool | Unset):
        q (str | Unset):
        url_query (list[str] | Unset):
        like (bool | Unset):
        updated_since (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        sort (ListMonitorSort | Unset):
        paused_last (bool | Unset):
        expand (list[ListMonitorExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMonitorFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | MonitorPage | QuotaExceeded
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            type_=type_,
            include_id=include_id,
            preset=preset,
            open_stat=open_stat,
            tag=tag,
            state=state,
            enabled=enabled,
            q=q,
            url_query=url_query,
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
    ).parsed
