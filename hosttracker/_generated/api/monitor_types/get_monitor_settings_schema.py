from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_error import InternalError
from ...models.json_schema_document import JsonSchemaDocument
from ...models.method_not_allowed import MethodNotAllowed
from ...models.unknown_parameter import UnknownParameter
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/monitor/type/schema",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InternalError | JsonSchemaDocument | MethodNotAllowed | UnknownParameter | None:
    if response.status_code == 200:
        response_200 = JsonSchemaDocument.from_dict(response.json())

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
) -> Response[InternalError | JsonSchemaDocument | MethodNotAllowed | UnknownParameter]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[InternalError | JsonSchemaDocument | MethodNotAllowed | UnknownParameter]:
    """Get one combined schema covering every monitor type's settings.

     Returns a single JSON Schema document whose branches are every type's settings shape, selected by
    the monitor's type property, with each referenced shape defined once in a shared namespace. Use it
    when generating client types or a single schema artefact; fetch one type's schema instead when a
    form only ever edits one kind of monitor.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalError | JsonSchemaDocument | MethodNotAllowed | UnknownParameter]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> InternalError | JsonSchemaDocument | MethodNotAllowed | UnknownParameter | None:
    """Get one combined schema covering every monitor type's settings.

     Returns a single JSON Schema document whose branches are every type's settings shape, selected by
    the monitor's type property, with each referenced shape defined once in a shared namespace. Use it
    when generating client types or a single schema artefact; fetch one type's schema instead when a
    form only ever edits one kind of monitor.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalError | JsonSchemaDocument | MethodNotAllowed | UnknownParameter
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[InternalError | JsonSchemaDocument | MethodNotAllowed | UnknownParameter]:
    """Get one combined schema covering every monitor type's settings.

     Returns a single JSON Schema document whose branches are every type's settings shape, selected by
    the monitor's type property, with each referenced shape defined once in a shared namespace. Use it
    when generating client types or a single schema artefact; fetch one type's schema instead when a
    form only ever edits one kind of monitor.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalError | JsonSchemaDocument | MethodNotAllowed | UnknownParameter]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> InternalError | JsonSchemaDocument | MethodNotAllowed | UnknownParameter | None:
    """Get one combined schema covering every monitor type's settings.

     Returns a single JSON Schema document whose branches are every type's settings shape, selected by
    the monitor's type property, with each referenced shape defined once in a shared namespace. Use it
    when generating client types or a single schema artefact; fetch one type's schema instead when a
    form only ever edits one kind of monitor.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalError | JsonSchemaDocument | MethodNotAllowed | UnknownParameter
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
