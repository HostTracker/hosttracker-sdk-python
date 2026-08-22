from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.list_monitor_maintenance_expand_item import (
    ListMonitorMaintenanceExpandItem,
)
from ...models.list_monitor_maintenance_fields_item import (
    ListMonitorMaintenanceFieldsItem,
)
from ...models.maintenance_page import MaintenancePage
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_expand import UnknownExpand
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    monitor_id: UUID,
    *,
    expand: list[ListMonitorMaintenanceExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorMaintenanceFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

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
        "url": "/monitor/{monitor_id}/maintenance".format(
            monitor_id=quote(str(monitor_id), safe=""),
        ),
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
    | InvalidToken
    | MaintenancePage
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownExpand
    | UnknownField
    | UnknownParameter
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

    if response.status_code == 404:
        response_404 = NotFound.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = MethodNotAllowed.from_dict(response.json())

        return response_405

    if response.status_code == 422:

        def _parse_response_422(data: object) -> UnknownExpand | UnknownField | UnknownParameter:
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
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_2 = UnknownParameter.from_dict(data)

            return response_422_type_2

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
    | InvalidToken
    | MaintenancePage
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownExpand
    | UnknownField
    | UnknownParameter
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    monitor_id: UUID,
    *,
    client: AuthenticatedClient,
    expand: list[ListMonitorMaintenanceExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorMaintenanceFieldsItem] | Unset = UNSET,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MaintenancePage
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownExpand
    | UnknownField
    | UnknownParameter
]:
    """List the maintenance windows covering one monitor.

     Returns the maintenance windows that cover the monitor in the path, each as its window DEFINITION in
    exactly the shape the maintenance list returns - a recurring window appears once, never expanded
    into occurrences. The monitor-side answer to the monitor-maintenance relationship; the same rows can
    be inlined on a monitor read with expand=maintenance, and the window-side direction is the
    maintenance list's expand=monitor. Nothing is embedded by default: ask for expand=monitor for the
    monitor's identifying projection, and expand=monitor.settings / monitor.subscription /
    monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks inside it.

    Args:
        monitor_id (UUID):
        expand (list[ListMonitorMaintenanceExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMonitorMaintenanceFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MaintenancePage | MethodNotAllowed | NotFound | QuotaExceeded | UnknownExpand | UnknownField | UnknownParameter]
    """

    kwargs = _get_kwargs(
        monitor_id=monitor_id,
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
    monitor_id: UUID,
    *,
    client: AuthenticatedClient,
    expand: list[ListMonitorMaintenanceExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorMaintenanceFieldsItem] | Unset = UNSET,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MaintenancePage
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | None
):
    """List the maintenance windows covering one monitor.

     Returns the maintenance windows that cover the monitor in the path, each as its window DEFINITION in
    exactly the shape the maintenance list returns - a recurring window appears once, never expanded
    into occurrences. The monitor-side answer to the monitor-maintenance relationship; the same rows can
    be inlined on a monitor read with expand=maintenance, and the window-side direction is the
    maintenance list's expand=monitor. Nothing is embedded by default: ask for expand=monitor for the
    monitor's identifying projection, and expand=monitor.settings / monitor.subscription /
    monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks inside it.

    Args:
        monitor_id (UUID):
        expand (list[ListMonitorMaintenanceExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMonitorMaintenanceFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MaintenancePage | MethodNotAllowed | NotFound | QuotaExceeded | UnknownExpand | UnknownField | UnknownParameter
    """

    return sync_detailed(
        monitor_id=monitor_id,
        client=client,
        expand=expand,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    monitor_id: UUID,
    *,
    client: AuthenticatedClient,
    expand: list[ListMonitorMaintenanceExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorMaintenanceFieldsItem] | Unset = UNSET,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MaintenancePage
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownExpand
    | UnknownField
    | UnknownParameter
]:
    """List the maintenance windows covering one monitor.

     Returns the maintenance windows that cover the monitor in the path, each as its window DEFINITION in
    exactly the shape the maintenance list returns - a recurring window appears once, never expanded
    into occurrences. The monitor-side answer to the monitor-maintenance relationship; the same rows can
    be inlined on a monitor read with expand=maintenance, and the window-side direction is the
    maintenance list's expand=monitor. Nothing is embedded by default: ask for expand=monitor for the
    monitor's identifying projection, and expand=monitor.settings / monitor.subscription /
    monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks inside it.

    Args:
        monitor_id (UUID):
        expand (list[ListMonitorMaintenanceExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMonitorMaintenanceFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MaintenancePage | MethodNotAllowed | NotFound | QuotaExceeded | UnknownExpand | UnknownField | UnknownParameter]
    """

    kwargs = _get_kwargs(
        monitor_id=monitor_id,
        expand=expand,
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    monitor_id: UUID,
    *,
    client: AuthenticatedClient,
    expand: list[ListMonitorMaintenanceExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorMaintenanceFieldsItem] | Unset = UNSET,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MaintenancePage
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | None
):
    """List the maintenance windows covering one monitor.

     Returns the maintenance windows that cover the monitor in the path, each as its window DEFINITION in
    exactly the shape the maintenance list returns - a recurring window appears once, never expanded
    into occurrences. The monitor-side answer to the monitor-maintenance relationship; the same rows can
    be inlined on a monitor read with expand=maintenance, and the window-side direction is the
    maintenance list's expand=monitor. Nothing is embedded by default: ask for expand=monitor for the
    monitor's identifying projection, and expand=monitor.settings / monitor.subscription /
    monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks inside it.

    Args:
        monitor_id (UUID):
        expand (list[ListMonitorMaintenanceExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMonitorMaintenanceFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MaintenancePage | MethodNotAllowed | NotFound | QuotaExceeded | UnknownExpand | UnknownField | UnknownParameter
    """

    return (
        await asyncio_detailed(
            monitor_id=monitor_id,
            client=client,
            expand=expand,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
