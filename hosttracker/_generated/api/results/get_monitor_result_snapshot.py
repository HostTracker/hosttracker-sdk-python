from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_parameter import UnknownParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    monitor_id: UUID,
    id: str,
    *,
    as_: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_none_match, Unset):
        headers["If-None-Match"] = if_none_match

    params: dict[str, Any] = {}

    params["as"] = as_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/monitor/{monitor_id}/result/{id}/snapshot".format(
            monitor_id=quote(str(monitor_id), safe=""),
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownParameter
    | None
):
    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

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
        response_422 = UnknownParameter.from_dict(response.json())

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
    Any
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
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
    id: str,
    *,
    client: AuthenticatedClient,
    as_: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
) -> Response[
    Any
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownParameter
]:
    """Download the page snapshot captured for a check result.

     Returns the stored page snapshot for one check as binary image data rather than base64 inside a JSON
    body, with validators and cache headers so it can be served from a cache or a content network. A
    snapshot never changes once captured, so a client may cache it indefinitely - send the ETag back as
    If-None-Match and an unchanged snapshot answers 304 with no body. HEAD is accepted on the same
    address for a metadata-only probe.

    Args:
        monitor_id (UUID):
        id (str):
        as_ (str | Unset):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownParameter]
    """

    kwargs = _get_kwargs(
        monitor_id=monitor_id,
        id=id,
        as_=as_,
        if_none_match=if_none_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    monitor_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
    as_: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
) -> (
    Any
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownParameter
    | None
):
    """Download the page snapshot captured for a check result.

     Returns the stored page snapshot for one check as binary image data rather than base64 inside a JSON
    body, with validators and cache headers so it can be served from a cache or a content network. A
    snapshot never changes once captured, so a client may cache it indefinitely - send the ETag back as
    If-None-Match and an unchanged snapshot answers 304 with no body. HEAD is accepted on the same
    address for a metadata-only probe.

    Args:
        monitor_id (UUID):
        id (str):
        as_ (str | Unset):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownParameter
    """

    return sync_detailed(
        monitor_id=monitor_id,
        id=id,
        client=client,
        as_=as_,
        if_none_match=if_none_match,
    ).parsed


async def asyncio_detailed(
    monitor_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
    as_: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
) -> Response[
    Any
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownParameter
]:
    """Download the page snapshot captured for a check result.

     Returns the stored page snapshot for one check as binary image data rather than base64 inside a JSON
    body, with validators and cache headers so it can be served from a cache or a content network. A
    snapshot never changes once captured, so a client may cache it indefinitely - send the ETag back as
    If-None-Match and an unchanged snapshot answers 304 with no body. HEAD is accepted on the same
    address for a metadata-only probe.

    Args:
        monitor_id (UUID):
        id (str):
        as_ (str | Unset):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownParameter]
    """

    kwargs = _get_kwargs(
        monitor_id=monitor_id,
        id=id,
        as_=as_,
        if_none_match=if_none_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    monitor_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
    as_: str | Unset = UNSET,
    if_none_match: str | Unset = UNSET,
) -> (
    Any
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownParameter
    | None
):
    """Download the page snapshot captured for a check result.

     Returns the stored page snapshot for one check as binary image data rather than base64 inside a JSON
    body, with validators and cache headers so it can be served from a cache or a content network. A
    snapshot never changes once captured, so a client may cache it indefinitely - send the ETag back as
    If-None-Match and an unchanged snapshot answers 304 with no body. HEAD is accepted on the same
    address for a metadata-only probe.

    Args:
        monitor_id (UUID):
        id (str):
        as_ (str | Unset):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownParameter
    """

    return (
        await asyncio_detailed(
            monitor_id=monitor_id,
            id=id,
            client=client,
            as_=as_,
            if_none_match=if_none_match,
        )
    ).parsed
