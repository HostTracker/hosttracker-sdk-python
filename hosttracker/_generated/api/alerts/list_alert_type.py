from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_type_row_page import AlertTypeRowPage
from ...models.internal_error import InternalError
from ...models.method_not_allowed import MethodNotAllowed
from ...models.unknown_parameter import UnknownParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/alert/type",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter | None:
    if response.status_code == 200:
        response_200 = AlertTypeRowPage.from_dict(response.json())

        return response_200

    if response.status_code == 405:
        response_405 = MethodNotAllowed.from_dict(response.json())

        return response_405

    if response.status_code == 422:
        response_422 = UnknownParameter.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = InternalError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AlertTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter]:
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
) -> Response[AlertTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter]:
    """List the alert types and the alert delays a subscription may use.

     Returns the fixed vocabulary of alert types a subscription can name, and the alert delay values the
    account may choose from. Use it to populate a picker or to validate a value before writing a
    subscription, rather than hard-coding a vocabulary that can grow.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
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
) -> AlertTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter | None:
    """List the alert types and the alert delays a subscription may use.

     Returns the fixed vocabulary of alert types a subscription can name, and the alert delay values the
    account may choose from. Use it to populate a picker or to validate a value before writing a
    subscription, rather than hard-coding a vocabulary that can grow.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[AlertTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter]:
    """List the alert types and the alert delays a subscription may use.

     Returns the fixed vocabulary of alert types a subscription can name, and the alert delay values the
    account may choose from. Use it to populate a picker or to validate a value before writing a
    subscription, rather than hard-coding a vocabulary that can grow.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> AlertTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter | None:
    """List the alert types and the alert delays a subscription may use.

     Returns the fixed vocabulary of alert types a subscription can name, and the alert delay values the
    account may choose from. Use it to populate a picker or to validate a value before writing a
    subscription, rather than hard-coding a vocabulary that can grow.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
