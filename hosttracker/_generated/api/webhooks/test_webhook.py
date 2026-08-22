from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.idempotency_key_conflict import IdempotencyKeyConflict
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_event_type import UnknownEventType
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.validation_failed import ValidationFailed
from ...models.webhook_test_request import WebhookTestRequest
from ...models.webhook_test_result_view import WebhookTestResultView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: WebhookTestRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhook/{id}/test".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnknownEventType
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | WebhookTestResultView
    | None
):
    if response.status_code == 200:
        response_200 = WebhookTestResultView.from_dict(response.json())

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

        def _parse_response_422(data: object) -> UnknownEventType | UnknownParameter | ValidationFailed:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = UnknownEventType.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_1 = ValidationFailed.from_dict(data)

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
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnknownEventType
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | WebhookTestResultView
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
    body: WebhookTestRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnknownEventType
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | WebhookTestResultView
]:
    """Send a synthetic test delivery to a webhook.

     Sends one structurally realistic event to the webhook's endpoint, signed exactly the way a real
    delivery is, and reports the outcome synchronously - including the signature header value that was
    sent, so a receiving implementation can be debugged against it. A test is never retried, so a
    failure is visible immediately instead of being queued.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (WebhookTestRequest | Unset): Which event the test delivery should carry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnknownEventType | UnknownParameter | ValidationFailed | UnsupportedMediaType | WebhookTestResultView]
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
    body: WebhookTestRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> (
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnknownEventType
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | WebhookTestResultView
    | None
):
    """Send a synthetic test delivery to a webhook.

     Sends one structurally realistic event to the webhook's endpoint, signed exactly the way a real
    delivery is, and reports the outcome synchronously - including the signature header value that was
    sent, so a receiving implementation can be debugged against it. A test is never retried, so a
    failure is visible immediately instead of being queued.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (WebhookTestRequest | Unset): Which event the test delivery should carry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnknownEventType | UnknownParameter | ValidationFailed | UnsupportedMediaType | WebhookTestResultView
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
    body: WebhookTestRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnknownEventType
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | WebhookTestResultView
]:
    """Send a synthetic test delivery to a webhook.

     Sends one structurally realistic event to the webhook's endpoint, signed exactly the way a real
    delivery is, and reports the outcome synchronously - including the signature header value that was
    sent, so a receiving implementation can be debugged against it. A test is never retried, so a
    failure is visible immediately instead of being queued.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (WebhookTestRequest | Unset): Which event the test delivery should carry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnknownEventType | UnknownParameter | ValidationFailed | UnsupportedMediaType | WebhookTestResultView]
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
    body: WebhookTestRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> (
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnknownEventType
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | WebhookTestResultView
    | None
):
    """Send a synthetic test delivery to a webhook.

     Sends one structurally realistic event to the webhook's endpoint, signed exactly the way a real
    delivery is, and reports the outcome synchronously - including the signature header value that was
    sent, so a receiving implementation can be debugged against it. A test is never retried, so a
    failure is visible immediately instead of being queued.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (WebhookTestRequest | Unset): Which event the test delivery should carry.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnknownEventType | UnknownParameter | ValidationFailed | UnsupportedMediaType | WebhookTestResultView
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
