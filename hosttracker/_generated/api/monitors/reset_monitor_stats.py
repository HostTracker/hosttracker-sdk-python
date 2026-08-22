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
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.job_accepted_view import JobAcceptedView
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_parameter import UnknownParameter
from ...models.validation_failed import ValidationFailed
from ...types import Response


def _get_kwargs(
    monitor_id: UUID,
    *,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/monitor/{monitor_id}/reset-stats".format(
            monitor_id=quote(str(monitor_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | JobAcceptedView
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownParameter
    | ValidationFailed
    | None
):
    if response.status_code == 202:
        response_202 = JobAcceptedView.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = IdempotencyKeyRequired.from_dict(response.json())

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
    | IdempotencyKeyRequired
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | JobAcceptedView
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownParameter
    | ValidationFailed
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    monitor_id: UUID,
    *,
    client: AuthenticatedClient,
    idempotency_key: str,
) -> Response[
    IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | JobAcceptedView
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownParameter
    | ValidationFailed
]:
    """Reset one monitor's accumulated uptime statistics.

     Queues a job that clears the monitor's historical statistics and answers with the job to poll; the
    job's single result is the monitor as it stands afterwards. Use it for one monitor - the bulk update
    endpoint carries the same operation for many. The optional body may name a webhook to call on
    completion and nothing else. An Idempotency-Key is mandatory: this call answers 202 and then works
    asynchronously, so a retry after a timeout would otherwise start a second reset job. The 202 carries
    a Retry-After header saying how long to wait before the first poll, sized on how much work was
    accepted.

    Args:
        monitor_id (UUID):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdempotencyKeyConflict | IdempotencyKeyRequired | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | NotFound | QuotaExceeded | UnknownParameter | ValidationFailed]
    """

    kwargs = _get_kwargs(
        monitor_id=monitor_id,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    monitor_id: UUID,
    *,
    client: AuthenticatedClient,
    idempotency_key: str,
) -> (
    IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | JobAcceptedView
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownParameter
    | ValidationFailed
    | None
):
    """Reset one monitor's accumulated uptime statistics.

     Queues a job that clears the monitor's historical statistics and answers with the job to poll; the
    job's single result is the monitor as it stands afterwards. Use it for one monitor - the bulk update
    endpoint carries the same operation for many. The optional body may name a webhook to call on
    completion and nothing else. An Idempotency-Key is mandatory: this call answers 202 and then works
    asynchronously, so a retry after a timeout would otherwise start a second reset job. The 202 carries
    a Retry-After header saying how long to wait before the first poll, sized on how much work was
    accepted.

    Args:
        monitor_id (UUID):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdempotencyKeyConflict | IdempotencyKeyRequired | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | NotFound | QuotaExceeded | UnknownParameter | ValidationFailed
    """

    return sync_detailed(
        monitor_id=monitor_id,
        client=client,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    monitor_id: UUID,
    *,
    client: AuthenticatedClient,
    idempotency_key: str,
) -> Response[
    IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | JobAcceptedView
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownParameter
    | ValidationFailed
]:
    """Reset one monitor's accumulated uptime statistics.

     Queues a job that clears the monitor's historical statistics and answers with the job to poll; the
    job's single result is the monitor as it stands afterwards. Use it for one monitor - the bulk update
    endpoint carries the same operation for many. The optional body may name a webhook to call on
    completion and nothing else. An Idempotency-Key is mandatory: this call answers 202 and then works
    asynchronously, so a retry after a timeout would otherwise start a second reset job. The 202 carries
    a Retry-After header saying how long to wait before the first poll, sized on how much work was
    accepted.

    Args:
        monitor_id (UUID):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdempotencyKeyConflict | IdempotencyKeyRequired | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | NotFound | QuotaExceeded | UnknownParameter | ValidationFailed]
    """

    kwargs = _get_kwargs(
        monitor_id=monitor_id,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    monitor_id: UUID,
    *,
    client: AuthenticatedClient,
    idempotency_key: str,
) -> (
    IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | JobAcceptedView
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownParameter
    | ValidationFailed
    | None
):
    """Reset one monitor's accumulated uptime statistics.

     Queues a job that clears the monitor's historical statistics and answers with the job to poll; the
    job's single result is the monitor as it stands afterwards. Use it for one monitor - the bulk update
    endpoint carries the same operation for many. The optional body may name a webhook to call on
    completion and nothing else. An Idempotency-Key is mandatory: this call answers 202 and then works
    asynchronously, so a retry after a timeout would otherwise start a second reset job. The 202 carries
    a Retry-After header saying how long to wait before the first poll, sized on how much work was
    accepted.

    Args:
        monitor_id (UUID):
        idempotency_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdempotencyKeyConflict | IdempotencyKeyRequired | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | NotFound | QuotaExceeded | UnknownParameter | ValidationFailed
    """

    return (
        await asyncio_detailed(
            monitor_id=monitor_id,
            client=client,
            idempotency_key=idempotency_key,
        )
    ).parsed
