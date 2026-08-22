from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_view import AccountView
from ...models.get_account_expand_item import GetAccountExpandItem
from ...models.get_account_fields_item import GetAccountFieldsItem
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_expand import UnknownExpand
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    expand: list[GetAccountExpandItem] | Unset = UNSET,
    fields: list[GetAccountFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_expand: list[str] | Unset = UNSET
    if not isinstance(expand, Unset):
        json_expand = []
        for expand_item_data in expand:
            expand_item: str = expand_item_data
            json_expand.append(expand_item)

    params["expand"] = json_expand

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
        "url": "/account",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AccountView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | None
):
    if response.status_code == 200:
        response_200 = AccountView.from_dict(response.json())

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
    AccountView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
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
    *,
    client: AuthenticatedClient,
    expand: list[GetAccountExpandItem] | Unset = UNSET,
    fields: list[GetAccountFieldsItem] | Unset = UNSET,
) -> Response[
    AccountView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownExpand
    | UnknownField
    | UnknownParameter
]:
    """Read the account: identity, package, usage, limits and status.

     Returns the caller's account in one document - who it is, which package it holds, what it is using,
    the bounds every other endpoint enforces, and whether monitoring is currently running. Make it the
    first call an integration ever makes: the limits block is what lets a client size its later requests
    instead of discovering the bounds by being refused. Expand quota to fold the quota document in and
    save a second call.

    Args:
        expand (list[GetAccountExpandItem] | Unset):
        fields (list[GetAccountFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownExpand | UnknownField | UnknownParameter]
    """

    kwargs = _get_kwargs(
        expand=expand,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    expand: list[GetAccountExpandItem] | Unset = UNSET,
    fields: list[GetAccountFieldsItem] | Unset = UNSET,
) -> (
    AccountView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | None
):
    """Read the account: identity, package, usage, limits and status.

     Returns the caller's account in one document - who it is, which package it holds, what it is using,
    the bounds every other endpoint enforces, and whether monitoring is currently running. Make it the
    first call an integration ever makes: the limits block is what lets a client size its later requests
    instead of discovering the bounds by being refused. Expand quota to fold the quota document in and
    save a second call.

    Args:
        expand (list[GetAccountExpandItem] | Unset):
        fields (list[GetAccountFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownExpand | UnknownField | UnknownParameter
    """

    return sync_detailed(
        client=client,
        expand=expand,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    expand: list[GetAccountExpandItem] | Unset = UNSET,
    fields: list[GetAccountFieldsItem] | Unset = UNSET,
) -> Response[
    AccountView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownExpand
    | UnknownField
    | UnknownParameter
]:
    """Read the account: identity, package, usage, limits and status.

     Returns the caller's account in one document - who it is, which package it holds, what it is using,
    the bounds every other endpoint enforces, and whether monitoring is currently running. Make it the
    first call an integration ever makes: the limits block is what lets a client size its later requests
    instead of discovering the bounds by being refused. Expand quota to fold the quota document in and
    save a second call.

    Args:
        expand (list[GetAccountExpandItem] | Unset):
        fields (list[GetAccountFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownExpand | UnknownField | UnknownParameter]
    """

    kwargs = _get_kwargs(
        expand=expand,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    expand: list[GetAccountExpandItem] | Unset = UNSET,
    fields: list[GetAccountFieldsItem] | Unset = UNSET,
) -> (
    AccountView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | None
):
    """Read the account: identity, package, usage, limits and status.

     Returns the caller's account in one document - who it is, which package it holds, what it is using,
    the bounds every other endpoint enforces, and whether monitoring is currently running. Make it the
    first call an integration ever makes: the limits block is what lets a client size its later requests
    instead of discovering the bounds by being refused. Expand quota to fold the quota document in and
    save a second call.

    Args:
        expand (list[GetAccountExpandItem] | Unset):
        fields (list[GetAccountFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownExpand | UnknownField | UnknownParameter
    """

    return (
        await asyncio_detailed(
            client=client,
            expand=expand,
            fields=fields,
        )
    ).parsed
