from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_member_page import AccountMemberPage
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_cursor import InvalidCursor
from ...models.invalid_limit import InvalidLimit
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.list_account_member_fields_item import ListAccountMemberFieldsItem
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAccountMemberFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

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
        "url": "/account/member",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AccountMemberPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    if response.status_code == 200:
        response_200 = AccountMemberPage.from_dict(response.json())

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

        def _parse_response_422(data: object) -> InvalidCursor | InvalidLimit | UnknownField | UnknownParameter:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = UnknownField.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_1 = InvalidCursor.from_dict(data)

                return response_422_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_2 = InvalidLimit.from_dict(data)

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
    AccountMemberPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownField
    | UnknownParameter
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
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAccountMemberFieldsItem] | Unset = UNSET,
) -> Response[
    AccountMemberPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
]:
    """List the contacts holding shared access to the account.

     Returns a page of the people granted shared access to the account, with the rights each holds and
    whether the invitation has been accepted. Use it to audit or display who can act on the account's
    behalf. Access grants themselves are managed elsewhere; this surface is read-only.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListAccountMemberFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountMemberPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | QuotaExceeded]
    """

    kwargs = _get_kwargs(
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
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAccountMemberFieldsItem] | Unset = UNSET,
) -> (
    AccountMemberPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    """List the contacts holding shared access to the account.

     Returns a page of the people granted shared access to the account, with the rights each holds and
    whether the invitation has been accepted. Use it to audit or display who can act on the account's
    behalf. Access grants themselves are managed elsewhere; this surface is read-only.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListAccountMemberFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountMemberPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | QuotaExceeded
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAccountMemberFieldsItem] | Unset = UNSET,
) -> Response[
    AccountMemberPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
]:
    """List the contacts holding shared access to the account.

     Returns a page of the people granted shared access to the account, with the rights each holds and
    whether the invitation has been accepted. Use it to audit or display who can act on the account's
    behalf. Access grants themselves are managed elsewhere; this surface is read-only.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListAccountMemberFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountMemberPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAccountMemberFieldsItem] | Unset = UNSET,
) -> (
    AccountMemberPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    """List the contacts holding shared access to the account.

     Returns a page of the people granted shared access to the account, with the rights each holds and
    whether the invitation has been accepted. Use it to audit or display who can act on the account's
    behalf. Access grants themselves are managed elsewhere; this surface is read-only.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListAccountMemberFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountMemberPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | QuotaExceeded
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
