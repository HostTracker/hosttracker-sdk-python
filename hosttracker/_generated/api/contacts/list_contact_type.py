from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_type_row_page import ContactTypeRowPage
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
        "url": "/contact/type",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContactTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter | None:
    if response.status_code == 200:
        response_200 = ContactTypeRowPage.from_dict(response.json())

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
) -> Response[ContactTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter]:
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
) -> Response[ContactTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter]:
    """List the contact types, their gateways and their capabilities.

     Returns the catalogue of contact types: which can be created directly, which need confirmation,
    which can receive scheduled reports, the gateways each offers, and the alert delays the account may
    choose from. Use it to build a contact form or to validate a type before a create - the creatable
    set is not fixed forever, so reading it beats hard-coding it.

    Two rows carry a vocabulary of their own: `webPush` publishes `webPushKey`, the application server
    key a browser needs to mint the push subscription a webPush contact is created from, and `http`
    publishes `templateParameters`, the `[[token]]` vocabulary a custom message template may use.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter]
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
) -> ContactTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter | None:
    """List the contact types, their gateways and their capabilities.

     Returns the catalogue of contact types: which can be created directly, which need confirmation,
    which can receive scheduled reports, the gateways each offers, and the alert delays the account may
    choose from. Use it to build a contact form or to validate a type before a create - the creatable
    set is not fixed forever, so reading it beats hard-coding it.

    Two rows carry a vocabulary of their own: `webPush` publishes `webPushKey`, the application server
    key a browser needs to mint the push subscription a webPush contact is created from, and `http`
    publishes `templateParameters`, the `[[token]]` vocabulary a custom message template may use.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter
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
) -> Response[ContactTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter]:
    """List the contact types, their gateways and their capabilities.

     Returns the catalogue of contact types: which can be created directly, which need confirmation,
    which can receive scheduled reports, the gateways each offers, and the alert delays the account may
    choose from. Use it to build a contact form or to validate a type before a create - the creatable
    set is not fixed forever, so reading it beats hard-coding it.

    Two rows carry a vocabulary of their own: `webPush` publishes `webPushKey`, the application server
    key a browser needs to mint the push subscription a webPush contact is created from, and `http`
    publishes `templateParameters`, the `[[token]]` vocabulary a custom message template may use.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter]
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
) -> ContactTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter | None:
    """List the contact types, their gateways and their capabilities.

     Returns the catalogue of contact types: which can be created directly, which need confirmation,
    which can receive scheduled reports, the gateways each offers, and the alert delays the account may
    choose from. Use it to build a contact form or to validate a type before a create - the creatable
    set is not fixed forever, so reading it beats hard-coding it.

    Two rows carry a vocabulary of their own: `webPush` publishes `webPushKey`, the application server
    key a browser needs to mint the push subscription a webPush contact is created from, and `http`
    publishes `templateParameters`, the `[[token]]` vocabulary a custom message template may use.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactTypeRowPage | InternalError | MethodNotAllowed | UnknownParameter
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
