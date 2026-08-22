from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_page import IncidentPage
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_cursor import InvalidCursor
from ...models.invalid_limit import InvalidLimit
from ...models.invalid_range import InvalidRange
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.list_incident_expand_item import ListIncidentExpandItem
from ...models.list_incident_fields_item import ListIncidentFieldsItem
from ...models.list_incident_severity_item import ListIncidentSeverityItem
from ...models.list_incident_sort import ListIncidentSort
from ...models.list_incident_state_item import ListIncidentStateItem
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.quota_exceeded import QuotaExceeded
from ...models.too_many_items import TooManyItems
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_expand import UnknownExpand
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    monitor: list[str] | Unset = UNSET,
    url_query: list[str] | Unset = UNSET,
    like: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    severity: list[ListIncidentSeverityItem] | Unset = UNSET,
    state: list[ListIncidentStateItem] | Unset = UNSET,
    sort: ListIncidentSort | Unset = UNSET,
    expand: list[ListIncidentExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListIncidentFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_monitor: list[str] | Unset = UNSET
    if not isinstance(monitor, Unset):
        json_monitor = monitor

    params["monitor"] = json_monitor

    json_url_query: list[str] | Unset = UNSET
    if not isinstance(url_query, Unset):
        json_url_query = url_query

    params["url"] = json_url_query

    params["like"] = like

    params["q"] = q

    params["from"] = from_

    params["to"] = to

    json_severity: list[str] | Unset = UNSET
    if not isinstance(severity, Unset):
        json_severity = []
        for severity_item_data in severity:
            severity_item: str = severity_item_data
            json_severity.append(severity_item)

    params["severity"] = json_severity

    json_state: list[str] | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item: str = state_item_data
            json_state.append(state_item)

    params["state"] = json_state

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

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
        "url": "/monitor/incident",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    IncidentPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | TooManyItems
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    if response.status_code == 200:
        response_200 = IncidentPage.from_dict(response.json())

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
            | TooManyItems
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
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_7 = TooManyItems.from_dict(data)

                return response_422_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_8 = UnknownParameter.from_dict(data)

            return response_422_type_8

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
    IncidentPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | TooManyItems
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
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
    monitor: list[str] | Unset = UNSET,
    url_query: list[str] | Unset = UNSET,
    like: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    severity: list[ListIncidentSeverityItem] | Unset = UNSET,
    state: list[ListIncidentStateItem] | Unset = UNSET,
    sort: ListIncidentSort | Unset = UNSET,
    expand: list[ListIncidentExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListIncidentFieldsItem] | Unset = UNSET,
) -> Response[
    IncidentPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | TooManyItems
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
]:
    """List down-episodes across the account or a monitor selection.

     Returns a page of incidents - the episodes between a monitor going down and coming back - narrowed
    by monitor id (monitor=), address (url=, with like=true for substring match) or free text (q=), time
    window, severity or whether they are still open. The three monitor filters combine rather than
    adding to each other, exactly as they do on the monitor list, and with none of them this is the
    account's own incident feed over any window - an episode row exists per state change, so it stays
    small. Order it with sort=monitor to group the page by monitor (name A to Z, newest-first inside
    each) instead of the default sort=time. Each row carries its cause, duration, severity band and
    whether it fell inside a maintenance window. Use it instead of scanning raw results when the
    question is about outages rather than checks. Nothing is embedded by default: ask for expand=monitor
    for the monitor's identifying projection, and expand=monitor.settings / monitor.subscription /
    monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks inside it.
    expand=recheck adds the constellation that opened each episode: the location that detected it, the
    locations that confirmed it grouped by the error each saw, and the locations that still saw the
    target up.

    Args:
        monitor (list[str] | Unset):
        url_query (list[str] | Unset):
        like (bool | Unset):
        q (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        severity (list[ListIncidentSeverityItem] | Unset):
        state (list[ListIncidentStateItem] | Unset):
        sort (ListIncidentSort | Unset):
        expand (list[ListIncidentExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListIncidentFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | TooManyItems | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        monitor=monitor,
        url_query=url_query,
        like=like,
        q=q,
        from_=from_,
        to=to,
        severity=severity,
        state=state,
        sort=sort,
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
    monitor: list[str] | Unset = UNSET,
    url_query: list[str] | Unset = UNSET,
    like: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    severity: list[ListIncidentSeverityItem] | Unset = UNSET,
    state: list[ListIncidentStateItem] | Unset = UNSET,
    sort: ListIncidentSort | Unset = UNSET,
    expand: list[ListIncidentExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListIncidentFieldsItem] | Unset = UNSET,
) -> (
    IncidentPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | TooManyItems
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    """List down-episodes across the account or a monitor selection.

     Returns a page of incidents - the episodes between a monitor going down and coming back - narrowed
    by monitor id (monitor=), address (url=, with like=true for substring match) or free text (q=), time
    window, severity or whether they are still open. The three monitor filters combine rather than
    adding to each other, exactly as they do on the monitor list, and with none of them this is the
    account's own incident feed over any window - an episode row exists per state change, so it stays
    small. Order it with sort=monitor to group the page by monitor (name A to Z, newest-first inside
    each) instead of the default sort=time. Each row carries its cause, duration, severity band and
    whether it fell inside a maintenance window. Use it instead of scanning raw results when the
    question is about outages rather than checks. Nothing is embedded by default: ask for expand=monitor
    for the monitor's identifying projection, and expand=monitor.settings / monitor.subscription /
    monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks inside it.
    expand=recheck adds the constellation that opened each episode: the location that detected it, the
    locations that confirmed it grouped by the error each saw, and the locations that still saw the
    target up.

    Args:
        monitor (list[str] | Unset):
        url_query (list[str] | Unset):
        like (bool | Unset):
        q (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        severity (list[ListIncidentSeverityItem] | Unset):
        state (list[ListIncidentStateItem] | Unset):
        sort (ListIncidentSort | Unset):
        expand (list[ListIncidentExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListIncidentFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | TooManyItems | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | QuotaExceeded
    """

    return sync_detailed(
        client=client,
        monitor=monitor,
        url_query=url_query,
        like=like,
        q=q,
        from_=from_,
        to=to,
        severity=severity,
        state=state,
        sort=sort,
        expand=expand,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    monitor: list[str] | Unset = UNSET,
    url_query: list[str] | Unset = UNSET,
    like: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    severity: list[ListIncidentSeverityItem] | Unset = UNSET,
    state: list[ListIncidentStateItem] | Unset = UNSET,
    sort: ListIncidentSort | Unset = UNSET,
    expand: list[ListIncidentExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListIncidentFieldsItem] | Unset = UNSET,
) -> Response[
    IncidentPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | TooManyItems
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
]:
    """List down-episodes across the account or a monitor selection.

     Returns a page of incidents - the episodes between a monitor going down and coming back - narrowed
    by monitor id (monitor=), address (url=, with like=true for substring match) or free text (q=), time
    window, severity or whether they are still open. The three monitor filters combine rather than
    adding to each other, exactly as they do on the monitor list, and with none of them this is the
    account's own incident feed over any window - an episode row exists per state change, so it stays
    small. Order it with sort=monitor to group the page by monitor (name A to Z, newest-first inside
    each) instead of the default sort=time. Each row carries its cause, duration, severity band and
    whether it fell inside a maintenance window. Use it instead of scanning raw results when the
    question is about outages rather than checks. Nothing is embedded by default: ask for expand=monitor
    for the monitor's identifying projection, and expand=monitor.settings / monitor.subscription /
    monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks inside it.
    expand=recheck adds the constellation that opened each episode: the location that detected it, the
    locations that confirmed it grouped by the error each saw, and the locations that still saw the
    target up.

    Args:
        monitor (list[str] | Unset):
        url_query (list[str] | Unset):
        like (bool | Unset):
        q (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        severity (list[ListIncidentSeverityItem] | Unset):
        state (list[ListIncidentStateItem] | Unset):
        sort (ListIncidentSort | Unset):
        expand (list[ListIncidentExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListIncidentFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | TooManyItems | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        monitor=monitor,
        url_query=url_query,
        like=like,
        q=q,
        from_=from_,
        to=to,
        severity=severity,
        state=state,
        sort=sort,
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
    monitor: list[str] | Unset = UNSET,
    url_query: list[str] | Unset = UNSET,
    like: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    severity: list[ListIncidentSeverityItem] | Unset = UNSET,
    state: list[ListIncidentStateItem] | Unset = UNSET,
    sort: ListIncidentSort | Unset = UNSET,
    expand: list[ListIncidentExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListIncidentFieldsItem] | Unset = UNSET,
) -> (
    IncidentPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | TooManyItems
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    """List down-episodes across the account or a monitor selection.

     Returns a page of incidents - the episodes between a monitor going down and coming back - narrowed
    by monitor id (monitor=), address (url=, with like=true for substring match) or free text (q=), time
    window, severity or whether they are still open. The three monitor filters combine rather than
    adding to each other, exactly as they do on the monitor list, and with none of them this is the
    account's own incident feed over any window - an episode row exists per state change, so it stays
    small. Order it with sort=monitor to group the page by monitor (name A to Z, newest-first inside
    each) instead of the default sort=time. Each row carries its cause, duration, severity band and
    whether it fell inside a maintenance window. Use it instead of scanning raw results when the
    question is about outages rather than checks. Nothing is embedded by default: ask for expand=monitor
    for the monitor's identifying projection, and expand=monitor.settings / monitor.subscription /
    monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks inside it.
    expand=recheck adds the constellation that opened each episode: the location that detected it, the
    locations that confirmed it grouped by the error each saw, and the locations that still saw the
    target up.

    Args:
        monitor (list[str] | Unset):
        url_query (list[str] | Unset):
        like (bool | Unset):
        q (str | Unset):
        from_ (int | Unset):
        to (int | Unset):
        severity (list[ListIncidentSeverityItem] | Unset):
        state (list[ListIncidentStateItem] | Unset):
        sort (ListIncidentSort | Unset):
        expand (list[ListIncidentExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListIncidentFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | TooManyItems | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | QuotaExceeded
    """

    return (
        await asyncio_detailed(
            client=client,
            monitor=monitor,
            url_query=url_query,
            like=like,
            q=q,
            from_=from_,
            to=to,
            severity=severity,
            state=state,
            sort=sort,
            expand=expand,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
