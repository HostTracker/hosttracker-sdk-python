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
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_parameter import UnknownParameter
from ...models.validation_failed import ValidationFailed
from ...models.webhook_test_result_view import WebhookTestResultView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    delivery_id: str,
    *,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhook/{id}/delivery/{delivery_id}/redeliver".format(
            id=quote(str(id), safe=""),
            delivery_id=quote(str(delivery_id), safe=""),
        ),
    }

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
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownParameter
    | ValidationFailed
    | WebhookTestResultView
    | None
):
    if response.status_code == 200:
        response_200 = WebhookTestResultView.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = IdempotencyKeyConflict.from_dict(response.json())

        return response_409

    if response.status_code == 422:

        def _parse_response_422(data: object) -> UnknownParameter | ValidationFailed:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = ValidationFailed.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_1 = UnknownParameter.from_dict(data)

            return response_422_type_1

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
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownParameter
    | ValidationFailed
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
    delivery_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownParameter
    | ValidationFailed
    | WebhookTestResultView
]:
    """Resend a previously recorded webhook delivery.

     Resends the exact payload of a recorded delivery with a freshly signed timestamp and reports the
    outcome synchronously. Use it to recover a delivery an endpoint missed while it was down, once the
    endpoint is healthy again. The delivery identifier is reused unchanged, so a consumer that
    deduplicates on it will not process the event twice.

    Args:
        id (UUID):
        delivery_id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownParameter | ValidationFailed | WebhookTestResultView]
    """

    kwargs = _get_kwargs(
        id=id,
        delivery_id=delivery_id,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> (
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownParameter
    | ValidationFailed
    | WebhookTestResultView
    | None
):
    """Resend a previously recorded webhook delivery.

     Resends the exact payload of a recorded delivery with a freshly signed timestamp and reports the
    outcome synchronously. Use it to recover a delivery an endpoint missed while it was down, once the
    endpoint is healthy again. The delivery identifier is reused unchanged, so a consumer that
    deduplicates on it will not process the event twice.

    Args:
        id (UUID):
        delivery_id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownParameter | ValidationFailed | WebhookTestResultView
    """

    return sync_detailed(
        id=id,
        delivery_id=delivery_id,
        client=client,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownParameter
    | ValidationFailed
    | WebhookTestResultView
]:
    """Resend a previously recorded webhook delivery.

     Resends the exact payload of a recorded delivery with a freshly signed timestamp and reports the
    outcome synchronously. Use it to recover a delivery an endpoint missed while it was down, once the
    endpoint is healthy again. The delivery identifier is reused unchanged, so a consumer that
    deduplicates on it will not process the event twice.

    Args:
        id (UUID):
        delivery_id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownParameter | ValidationFailed | WebhookTestResultView]
    """

    kwargs = _get_kwargs(
        id=id,
        delivery_id=delivery_id,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    delivery_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> (
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownParameter
    | ValidationFailed
    | WebhookTestResultView
    | None
):
    """Resend a previously recorded webhook delivery.

     Resends the exact payload of a recorded delivery with a freshly signed timestamp and reports the
    outcome synchronously. Use it to recover a delivery an endpoint missed while it was down, once the
    endpoint is healthy again. The delivery identifier is reused unchanged, so a consumer that
    deduplicates on it will not process the event twice.

    Args:
        id (UUID):
        delivery_id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownParameter | ValidationFailed | WebhookTestResultView
    """

    return (
        await asyncio_detailed(
            id=id,
            delivery_id=delivery_id,
            client=client,
            idempotency_key=idempotency_key,
        )
    ).parsed
