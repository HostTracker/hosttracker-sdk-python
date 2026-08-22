from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.invalid_url import InvalidUrl
from ...models.ip_not_allowed import IpNotAllowed
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.monitor_resolve_request import MonitorResolveRequest
from ...models.monitor_resolve_view import MonitorResolveView
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.service_unavailable import ServiceUnavailable
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.validation_failed import ValidationFailed
from ...types import Response


def _get_kwargs(
    *,
    body: MonitorResolveRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/monitor/resolve",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | InvalidUrl
    | UnknownParameter
    | ValidationFailed
    | MalformedRequest
    | MethodNotAllowed
    | MonitorResolveView
    | PayloadTooLarge
    | QuotaExceeded
    | ServiceUnavailable
    | UnsupportedMediaType
    | None
):
    if response.status_code == 200:
        response_200 = MonitorResolveView.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = MalformedRequest.from_dict(response.json())

        return response_400

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

    if response.status_code == 413:
        response_413 = PayloadTooLarge.from_dict(response.json())

        return response_413

    if response.status_code == 415:
        response_415 = UnsupportedMediaType.from_dict(response.json())

        return response_415

    if response.status_code == 422:

        def _parse_response_422(data: object) -> InvalidUrl | UnknownParameter | ValidationFailed:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = ValidationFailed.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_1 = InvalidUrl.from_dict(data)

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

    if response.status_code == 503:
        response_503 = ServiceUnavailable.from_dict(response.json())

        return response_503

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
    | InvalidUrl
    | UnknownParameter
    | ValidationFailed
    | MalformedRequest
    | MethodNotAllowed
    | MonitorResolveView
    | PayloadTooLarge
    | QuotaExceeded
    | ServiceUnavailable
    | UnsupportedMediaType
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
    body: MonitorResolveRequest,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | InvalidUrl
    | UnknownParameter
    | ValidationFailed
    | MalformedRequest
    | MethodNotAllowed
    | MonitorResolveView
    | PayloadTooLarge
    | QuotaExceeded
    | ServiceUnavailable
    | UnsupportedMediaType
]:
    """Resolve a target address to the IPs it currently answers with.

     Looks up the addresses the url's host resolves to right now, which is what a DNS or TLS monitor's
    expected-address list is filled from. It resolves names only: nothing is connected to, no redirect
    is followed and no monitor type is guessed. A host with no address records answers an empty list,
    because that is the answer; a lookup that could not be completed answers 503 with Retry-After
    instead, so an empty list is never a lookup failure in disguise.

    Args:
        body (MonitorResolveRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | InvalidUrl | UnknownParameter | ValidationFailed | MalformedRequest | MethodNotAllowed | MonitorResolveView | PayloadTooLarge | QuotaExceeded | ServiceUnavailable | UnsupportedMediaType]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: MonitorResolveRequest,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | InvalidUrl
    | UnknownParameter
    | ValidationFailed
    | MalformedRequest
    | MethodNotAllowed
    | MonitorResolveView
    | PayloadTooLarge
    | QuotaExceeded
    | ServiceUnavailable
    | UnsupportedMediaType
    | None
):
    """Resolve a target address to the IPs it currently answers with.

     Looks up the addresses the url's host resolves to right now, which is what a DNS or TLS monitor's
    expected-address list is filled from. It resolves names only: nothing is connected to, no redirect
    is followed and no monitor type is guessed. A host with no address records answers an empty list,
    because that is the answer; a lookup that could not be completed answers 503 with Retry-After
    instead, so an empty list is never a lookup failure in disguise.

    Args:
        body (MonitorResolveRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | InvalidUrl | UnknownParameter | ValidationFailed | MalformedRequest | MethodNotAllowed | MonitorResolveView | PayloadTooLarge | QuotaExceeded | ServiceUnavailable | UnsupportedMediaType
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MonitorResolveRequest,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | InvalidUrl
    | UnknownParameter
    | ValidationFailed
    | MalformedRequest
    | MethodNotAllowed
    | MonitorResolveView
    | PayloadTooLarge
    | QuotaExceeded
    | ServiceUnavailable
    | UnsupportedMediaType
]:
    """Resolve a target address to the IPs it currently answers with.

     Looks up the addresses the url's host resolves to right now, which is what a DNS or TLS monitor's
    expected-address list is filled from. It resolves names only: nothing is connected to, no redirect
    is followed and no monitor type is guessed. A host with no address records answers an empty list,
    because that is the answer; a lookup that could not be completed answers 503 with Retry-After
    instead, so an empty list is never a lookup failure in disguise.

    Args:
        body (MonitorResolveRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | InvalidUrl | UnknownParameter | ValidationFailed | MalformedRequest | MethodNotAllowed | MonitorResolveView | PayloadTooLarge | QuotaExceeded | ServiceUnavailable | UnsupportedMediaType]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MonitorResolveRequest,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | InvalidUrl
    | UnknownParameter
    | ValidationFailed
    | MalformedRequest
    | MethodNotAllowed
    | MonitorResolveView
    | PayloadTooLarge
    | QuotaExceeded
    | ServiceUnavailable
    | UnsupportedMediaType
    | None
):
    """Resolve a target address to the IPs it currently answers with.

     Looks up the addresses the url's host resolves to right now, which is what a DNS or TLS monitor's
    expected-address list is filled from. It resolves names only: nothing is connected to, no redirect
    is followed and no monitor type is guessed. A host with no address records answers an empty list,
    because that is the answer; a lookup that could not be completed answers 503 with Retry-After
    instead, so an empty list is never a lookup failure in disguise.

    Args:
        body (MonitorResolveRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | InvalidUrl | UnknownParameter | ValidationFailed | MalformedRequest | MethodNotAllowed | MonitorResolveView | PayloadTooLarge | QuotaExceeded | ServiceUnavailable | UnsupportedMediaType
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
