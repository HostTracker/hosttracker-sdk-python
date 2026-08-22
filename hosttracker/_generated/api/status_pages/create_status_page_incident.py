from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.idempotency_key_conflict import IdempotencyKeyConflict
from ...models.idempotency_key_required import IdempotencyKeyRequired
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_range import InvalidRange
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.status_page_incident_view import StatusPageIncidentView
from ...models.status_page_incident_write_request import StatusPageIncidentWriteRequest
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.validation_failed import ValidationFailed
from ...types import Response


def _get_kwargs(
    id: UUID,
    *,
    body: StatusPageIncidentWriteRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/statuspage/{id}/incident".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidRange
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | StatusPageIncidentView
    | UnsupportedMediaType
    | None
):
    if response.status_code == 201:
        response_201 = StatusPageIncidentView.from_dict(response.json())

        return response_201

    if response.status_code == 400:

        def _parse_response_400(data: object) -> IdempotencyKeyRequired | MalformedRequest:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_0 = MalformedRequest.from_dict(data)

                return response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_400_type_1 = IdempotencyKeyRequired.from_dict(data)

            return response_400_type_1

        response_400 = _parse_response_400(response.json())

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

    if response.status_code == 404:
        response_404 = NotFound.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = MethodNotAllowed.from_dict(response.json())

        return response_405

    if response.status_code == 409:
        response_409 = IdempotencyKeyConflict.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = PayloadTooLarge.from_dict(response.json())

        return response_413

    if response.status_code == 415:
        response_415 = UnsupportedMediaType.from_dict(response.json())

        return response_415

    if response.status_code == 422:

        def _parse_response_422(data: object) -> InvalidRange | UnknownEnumValue | UnknownParameter | ValidationFailed:
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
                response_422_type_1 = InvalidRange.from_dict(data)

                return response_422_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_2 = UnknownEnumValue.from_dict(data)

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
    IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidRange
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | StatusPageIncidentView
    | UnsupportedMediaType
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
    body: StatusPageIncidentWriteRequest,
    idempotency_key: str,
) -> Response[
    IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidRange
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | StatusPageIncidentView
    | UnsupportedMediaType
]:
    """Declare an incident or a scheduled maintenance on a status page.

     Declares what is happening: a title, the initial state (which seeds the timeline with the message),
    the affected components (this page's own), and for kind=maintenance the scheduled window in Unix
    seconds. This is the CI/automation door for incident communication. Declaring notifies the page's
    confirmed subscribers (email + webhook/Slack/Teams channels, component-scoped) exactly as a
    dashboard declare does - best-effort, a delivery failure never fails the write. An Idempotency-Key
    is REQUIRED here: this call notifies the page's subscribers, so a retry without one announces the
    same thing twice.

    Args:
        id (UUID):
        idempotency_key (str):
        body (StatusPageIncidentWriteRequest): The member vocabulary is closed: a member not
            listed here is refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidRange | UnknownEnumValue | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | StatusPageIncidentView | UnsupportedMediaType]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: StatusPageIncidentWriteRequest,
    idempotency_key: str,
) -> (
    IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidRange
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | StatusPageIncidentView
    | UnsupportedMediaType
    | None
):
    """Declare an incident or a scheduled maintenance on a status page.

     Declares what is happening: a title, the initial state (which seeds the timeline with the message),
    the affected components (this page's own), and for kind=maintenance the scheduled window in Unix
    seconds. This is the CI/automation door for incident communication. Declaring notifies the page's
    confirmed subscribers (email + webhook/Slack/Teams channels, component-scoped) exactly as a
    dashboard declare does - best-effort, a delivery failure never fails the write. An Idempotency-Key
    is REQUIRED here: this call notifies the page's subscribers, so a retry without one announces the
    same thing twice.

    Args:
        id (UUID):
        idempotency_key (str):
        body (StatusPageIncidentWriteRequest): The member vocabulary is closed: a member not
            listed here is refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidRange | UnknownEnumValue | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | StatusPageIncidentView | UnsupportedMediaType
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: StatusPageIncidentWriteRequest,
    idempotency_key: str,
) -> Response[
    IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidRange
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | StatusPageIncidentView
    | UnsupportedMediaType
]:
    """Declare an incident or a scheduled maintenance on a status page.

     Declares what is happening: a title, the initial state (which seeds the timeline with the message),
    the affected components (this page's own), and for kind=maintenance the scheduled window in Unix
    seconds. This is the CI/automation door for incident communication. Declaring notifies the page's
    confirmed subscribers (email + webhook/Slack/Teams channels, component-scoped) exactly as a
    dashboard declare does - best-effort, a delivery failure never fails the write. An Idempotency-Key
    is REQUIRED here: this call notifies the page's subscribers, so a retry without one announces the
    same thing twice.

    Args:
        id (UUID):
        idempotency_key (str):
        body (StatusPageIncidentWriteRequest): The member vocabulary is closed: a member not
            listed here is refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidRange | UnknownEnumValue | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | StatusPageIncidentView | UnsupportedMediaType]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: StatusPageIncidentWriteRequest,
    idempotency_key: str,
) -> (
    IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidRange
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | StatusPageIncidentView
    | UnsupportedMediaType
    | None
):
    """Declare an incident or a scheduled maintenance on a status page.

     Declares what is happening: a title, the initial state (which seeds the timeline with the message),
    the affected components (this page's own), and for kind=maintenance the scheduled window in Unix
    seconds. This is the CI/automation door for incident communication. Declaring notifies the page's
    confirmed subscribers (email + webhook/Slack/Teams channels, component-scoped) exactly as a
    dashboard declare does - best-effort, a delivery failure never fails the write. An Idempotency-Key
    is REQUIRED here: this call notifies the page's subscribers, so a retry without one announces the
    same thing twice.

    Args:
        id (UUID):
        idempotency_key (str):
        body (StatusPageIncidentWriteRequest): The member vocabulary is closed: a member not
            listed here is refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidRange | UnknownEnumValue | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | StatusPageIncidentView | UnsupportedMediaType
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
