from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_monitor_expand_item import GetMonitorExpandItem
from ...models.get_monitor_fields_item import GetMonitorFieldsItem
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_range import InvalidRange
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.monitor_view import MonitorView
from ...models.not_found import NotFound
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_expand import UnknownExpand
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    expand: list[GetMonitorExpandItem] | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    fields: list[GetMonitorFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_expand: list[str] | Unset = UNSET
    if not isinstance(expand, Unset):
        json_expand = []
        for expand_item_data in expand:
            expand_item: str = expand_item_data
            json_expand.append(expand_item)

    params["expand"] = json_expand

    params["from"] = from_

    params["to"] = to

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
        "url": "/monitor/{id}".format(
            id=quote(str(id), safe=""),
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
    | InvalidRange
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | MonitorView
    | NotFound
    | QuotaExceeded
    | None
):
    if response.status_code == 200:
        response_200 = MonitorView.from_dict(response.json())

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

        def _parse_response_422(data: object) -> InvalidRange | UnknownExpand | UnknownField | UnknownParameter:
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
                response_422_type_2 = InvalidRange.from_dict(data)

                return response_422_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_3 = UnknownParameter.from_dict(data)

            return response_422_type_3

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
    | InvalidRange
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | MonitorView
    | NotFound
    | QuotaExceeded
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    expand: list[GetMonitorExpandItem] | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    fields: list[GetMonitorFieldsItem] | Unset = UNSET,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidRange
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | MonitorView
    | NotFound
    | QuotaExceeded
]:
    """Retrieve one monitor, with its full configuration.

     Returns a single monitor in exactly the row shape the list endpoint uses, but with settings embedded
    by default because this is the configuration read. Reach for it when the id is already known;
    filtering the list down to one id costs the same call and returns less. It takes the same expand
    vocabulary the list does, so lastResult, spans and uptime are available here too. A monitor that
    does not exist and one that belongs to another account answer the same not-found, so an id cannot be
    probed.

    Args:
        id (UUID):
        expand (list[GetMonitorExpandItem] | Unset):
        from_ (int | Unset):
        to (int | Unset):
        fields (list[GetMonitorFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidRange | UnknownExpand | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | MonitorView | NotFound | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        id=id,
        expand=expand,
        from_=from_,
        to=to,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    expand: list[GetMonitorExpandItem] | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    fields: list[GetMonitorFieldsItem] | Unset = UNSET,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidRange
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | MonitorView
    | NotFound
    | QuotaExceeded
    | None
):
    """Retrieve one monitor, with its full configuration.

     Returns a single monitor in exactly the row shape the list endpoint uses, but with settings embedded
    by default because this is the configuration read. Reach for it when the id is already known;
    filtering the list down to one id costs the same call and returns less. It takes the same expand
    vocabulary the list does, so lastResult, spans and uptime are available here too. A monitor that
    does not exist and one that belongs to another account answer the same not-found, so an id cannot be
    probed.

    Args:
        id (UUID):
        expand (list[GetMonitorExpandItem] | Unset):
        from_ (int | Unset):
        to (int | Unset):
        fields (list[GetMonitorFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidRange | UnknownExpand | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | MonitorView | NotFound | QuotaExceeded
    """

    return sync_detailed(
        id=id,
        client=client,
        expand=expand,
        from_=from_,
        to=to,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    expand: list[GetMonitorExpandItem] | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    fields: list[GetMonitorFieldsItem] | Unset = UNSET,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidRange
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | MonitorView
    | NotFound
    | QuotaExceeded
]:
    """Retrieve one monitor, with its full configuration.

     Returns a single monitor in exactly the row shape the list endpoint uses, but with settings embedded
    by default because this is the configuration read. Reach for it when the id is already known;
    filtering the list down to one id costs the same call and returns less. It takes the same expand
    vocabulary the list does, so lastResult, spans and uptime are available here too. A monitor that
    does not exist and one that belongs to another account answer the same not-found, so an id cannot be
    probed.

    Args:
        id (UUID):
        expand (list[GetMonitorExpandItem] | Unset):
        from_ (int | Unset):
        to (int | Unset):
        fields (list[GetMonitorFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidRange | UnknownExpand | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | MonitorView | NotFound | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        id=id,
        expand=expand,
        from_=from_,
        to=to,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    expand: list[GetMonitorExpandItem] | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    fields: list[GetMonitorFieldsItem] | Unset = UNSET,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidRange
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | MonitorView
    | NotFound
    | QuotaExceeded
    | None
):
    """Retrieve one monitor, with its full configuration.

     Returns a single monitor in exactly the row shape the list endpoint uses, but with settings embedded
    by default because this is the configuration read. Reach for it when the id is already known;
    filtering the list down to one id costs the same call and returns less. It takes the same expand
    vocabulary the list does, so lastResult, spans and uptime are available here too. A monitor that
    does not exist and one that belongs to another account answer the same not-found, so an id cannot be
    probed.

    Args:
        id (UUID):
        expand (list[GetMonitorExpandItem] | Unset):
        from_ (int | Unset):
        to (int | Unset):
        fields (list[GetMonitorFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidRange | UnknownExpand | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | MonitorView | NotFound | QuotaExceeded
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            expand=expand,
            from_=from_,
            to=to,
            fields=fields,
        )
    ).parsed
