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
from ...models.list_maintenance_expand_item import ListMaintenanceExpandItem
from ...models.list_maintenance_fields_item import ListMaintenanceFieldsItem
from ...models.list_maintenance_sort import ListMaintenanceSort
from ...models.list_maintenance_state_item import ListMaintenanceStateItem
from ...models.maintenance_page import MaintenancePage
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_expand import UnknownExpand
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    state: list[ListMaintenanceStateItem] | Unset = UNSET,
    monitor: list[str] | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    sort: ListMaintenanceSort | Unset = UNSET,
    expand: list[ListMaintenanceExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMaintenanceFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    json_state: list[str] | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item: str = state_item_data
            json_state.append(state_item)

    params["state"] = json_state

    json_monitor: list[str] | Unset = UNSET
    if not isinstance(monitor, Unset):
        json_monitor = monitor

    params["monitor"] = json_monitor

    params["updatedSince"] = updated_since

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
        "url": "/maintenance",
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
    | MaintenancePage
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    if response.status_code == 200:
        response_200 = MaintenancePage.from_dict(response.json())

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
    | MaintenancePage
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
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    state: list[ListMaintenanceStateItem] | Unset = UNSET,
    monitor: list[str] | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    sort: ListMaintenanceSort | Unset = UNSET,
    expand: list[ListMaintenanceExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMaintenanceFieldsItem] | Unset = UNSET,
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
    | MaintenancePage
    | MethodNotAllowed
    | QuotaExceeded
]:
    """List scheduled, active and finished maintenance windows.

     Returns a page of maintenance windows, optionally narrowed by time window, state or the monitors
    they cover. A recurring window is returned once with its recurrence rule rather than expanded into
    every future occurrence, so a year of weekly maintenance is one row. The envelope carries a sync
    cursor, so a poll loop can read only what changed. Order it with sort=from (the default, newest
    window start first) or sort=created, each with an optional :asc/:desc suffix. Every row carries its
    coverage per monitor in monitors[]; the window-level suppress is present only when every monitor it
    covers shares one suppression. Nothing is embedded by default: ask for expand=monitor for the
    monitor's identifying projection, and expand=monitor.settings / monitor.subscription /
    monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks inside it.

    Args:
        from_ (int | Unset):
        to (int | Unset):
        state (list[ListMaintenanceStateItem] | Unset):
        monitor (list[str] | Unset):
        updated_since (str | Unset):
        sort (ListMaintenanceSort | Unset):
        expand (list[ListMaintenanceExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMaintenanceFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MaintenancePage | MethodNotAllowed | QuotaExceeded]
    """

    kwargs = _get_kwargs(
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

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    state: list[ListMaintenanceStateItem] | Unset = UNSET,
    monitor: list[str] | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    sort: ListMaintenanceSort | Unset = UNSET,
    expand: list[ListMaintenanceExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMaintenanceFieldsItem] | Unset = UNSET,
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
    | MaintenancePage
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    """List scheduled, active and finished maintenance windows.

     Returns a page of maintenance windows, optionally narrowed by time window, state or the monitors
    they cover. A recurring window is returned once with its recurrence rule rather than expanded into
    every future occurrence, so a year of weekly maintenance is one row. The envelope carries a sync
    cursor, so a poll loop can read only what changed. Order it with sort=from (the default, newest
    window start first) or sort=created, each with an optional :asc/:desc suffix. Every row carries its
    coverage per monitor in monitors[]; the window-level suppress is present only when every monitor it
    covers shares one suppression. Nothing is embedded by default: ask for expand=monitor for the
    monitor's identifying projection, and expand=monitor.settings / monitor.subscription /
    monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks inside it.

    Args:
        from_ (int | Unset):
        to (int | Unset):
        state (list[ListMaintenanceStateItem] | Unset):
        monitor (list[str] | Unset):
        updated_since (str | Unset):
        sort (ListMaintenanceSort | Unset):
        expand (list[ListMaintenanceExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMaintenanceFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MaintenancePage | MethodNotAllowed | QuotaExceeded
    """

    return sync_detailed(
        client=client,
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
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    state: list[ListMaintenanceStateItem] | Unset = UNSET,
    monitor: list[str] | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    sort: ListMaintenanceSort | Unset = UNSET,
    expand: list[ListMaintenanceExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMaintenanceFieldsItem] | Unset = UNSET,
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
    | MaintenancePage
    | MethodNotAllowed
    | QuotaExceeded
]:
    """List scheduled, active and finished maintenance windows.

     Returns a page of maintenance windows, optionally narrowed by time window, state or the monitors
    they cover. A recurring window is returned once with its recurrence rule rather than expanded into
    every future occurrence, so a year of weekly maintenance is one row. The envelope carries a sync
    cursor, so a poll loop can read only what changed. Order it with sort=from (the default, newest
    window start first) or sort=created, each with an optional :asc/:desc suffix. Every row carries its
    coverage per monitor in monitors[]; the window-level suppress is present only when every monitor it
    covers shares one suppression. Nothing is embedded by default: ask for expand=monitor for the
    monitor's identifying projection, and expand=monitor.settings / monitor.subscription /
    monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks inside it.

    Args:
        from_ (int | Unset):
        to (int | Unset):
        state (list[ListMaintenanceStateItem] | Unset):
        monitor (list[str] | Unset):
        updated_since (str | Unset):
        sort (ListMaintenanceSort | Unset):
        expand (list[ListMaintenanceExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMaintenanceFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MaintenancePage | MethodNotAllowed | QuotaExceeded]
    """

    kwargs = _get_kwargs(
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

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    state: list[ListMaintenanceStateItem] | Unset = UNSET,
    monitor: list[str] | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    sort: ListMaintenanceSort | Unset = UNSET,
    expand: list[ListMaintenanceExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMaintenanceFieldsItem] | Unset = UNSET,
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
    | MaintenancePage
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    """List scheduled, active and finished maintenance windows.

     Returns a page of maintenance windows, optionally narrowed by time window, state or the monitors
    they cover. A recurring window is returned once with its recurrence rule rather than expanded into
    every future occurrence, so a year of weekly maintenance is one row. The envelope carries a sync
    cursor, so a poll loop can read only what changed. Order it with sort=from (the default, newest
    window start first) or sort=created, each with an optional :asc/:desc suffix. Every row carries its
    coverage per monitor in monitors[]; the window-level suppress is present only when every monitor it
    covers shares one suppression. Nothing is embedded by default: ask for expand=monitor for the
    monitor's identifying projection, and expand=monitor.settings / monitor.subscription /
    monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks inside it.

    Args:
        from_ (int | Unset):
        to (int | Unset):
        state (list[ListMaintenanceStateItem] | Unset):
        monitor (list[str] | Unset):
        updated_since (str | Unset):
        sort (ListMaintenanceSort | Unset):
        expand (list[ListMaintenanceExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMaintenanceFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MaintenancePage | MethodNotAllowed | QuotaExceeded
    """

    return (
        await asyncio_detailed(
            client=client,
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
    ).parsed
