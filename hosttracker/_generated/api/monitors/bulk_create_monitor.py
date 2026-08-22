from http import HTTPStatus
from typing import Any

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
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.monitor_bulk_create_request import MonitorBulkCreateRequest
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.too_many_items import TooManyItems
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.validation_failed import ValidationFailed
from ...types import Response


def _get_kwargs(
    *,
    body: MonitorBulkCreateRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/monitor/bulk",
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
    | InvalidToken
    | JobAcceptedView
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | None
):
    if response.status_code == 202:
        response_202 = JobAcceptedView.from_dict(response.json())

        return response_202

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

        def _parse_response_422(data: object) -> TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed:
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
                response_422_type_1 = UnknownEnumValue.from_dict(data)

                return response_422_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_2 = TooManyItems.from_dict(data)

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
    | InvalidToken
    | JobAcceptedView
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
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
    body: MonitorBulkCreateRequest,
    idempotency_key: str,
) -> Response[
    IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | JobAcceptedView
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
]:
    """Create many monitors at once as one asynchronous job.

     Submits a batch of monitor definitions as a single job and answers immediately with a job id to poll
    for per-item results. Shared defaults are declared once and overridden per item. Prefer it over a
    loop of single creates when importing a site list; per-item validation happens as the job runs, so
    the response here only confirms the batch was accepted. An Idempotency-Key is mandatory, because a
    retried batch would otherwise duplicate every item in it. How many items one batch may carry is the
    account's own monitor cap, never more than 5000; the number is published as limits.maxBulkItems on
    the account endpoint, and a batch over it is refused naming the cap that applies. The 202 carries a
    Retry-After header saying how long to wait before the first poll, sized on how much work was
    accepted.

    Args:
        idempotency_key (str):
        body (MonitorBulkCreateRequest): The member vocabulary is closed: a member not listed here
            is refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | UnsupportedMediaType]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: MonitorBulkCreateRequest,
    idempotency_key: str,
) -> (
    IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | JobAcceptedView
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | None
):
    """Create many monitors at once as one asynchronous job.

     Submits a batch of monitor definitions as a single job and answers immediately with a job id to poll
    for per-item results. Shared defaults are declared once and overridden per item. Prefer it over a
    loop of single creates when importing a site list; per-item validation happens as the job runs, so
    the response here only confirms the batch was accepted. An Idempotency-Key is mandatory, because a
    retried batch would otherwise duplicate every item in it. How many items one batch may carry is the
    account's own monitor cap, never more than 5000; the number is published as limits.maxBulkItems on
    the account endpoint, and a batch over it is refused naming the cap that applies. The 202 carries a
    Retry-After header saying how long to wait before the first poll, sized on how much work was
    accepted.

    Args:
        idempotency_key (str):
        body (MonitorBulkCreateRequest): The member vocabulary is closed: a member not listed here
            is refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | UnsupportedMediaType
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MonitorBulkCreateRequest,
    idempotency_key: str,
) -> Response[
    IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | JobAcceptedView
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
]:
    """Create many monitors at once as one asynchronous job.

     Submits a batch of monitor definitions as a single job and answers immediately with a job id to poll
    for per-item results. Shared defaults are declared once and overridden per item. Prefer it over a
    loop of single creates when importing a site list; per-item validation happens as the job runs, so
    the response here only confirms the batch was accepted. An Idempotency-Key is mandatory, because a
    retried batch would otherwise duplicate every item in it. How many items one batch may carry is the
    account's own monitor cap, never more than 5000; the number is published as limits.maxBulkItems on
    the account endpoint, and a batch over it is refused naming the cap that applies. The 202 carries a
    Retry-After header saying how long to wait before the first poll, sized on how much work was
    accepted.

    Args:
        idempotency_key (str):
        body (MonitorBulkCreateRequest): The member vocabulary is closed: a member not listed here
            is refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | UnsupportedMediaType]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MonitorBulkCreateRequest,
    idempotency_key: str,
) -> (
    IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | JobAcceptedView
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | None
):
    """Create many monitors at once as one asynchronous job.

     Submits a batch of monitor definitions as a single job and answers immediately with a job id to poll
    for per-item results. Shared defaults are declared once and overridden per item. Prefer it over a
    loop of single creates when importing a site list; per-item validation happens as the job runs, so
    the response here only confirms the batch was accepted. An Idempotency-Key is mandatory, because a
    retried batch would otherwise duplicate every item in it. How many items one batch may carry is the
    account's own monitor cap, never more than 5000; the number is published as limits.maxBulkItems on
    the account endpoint, and a batch over it is refused naming the cap that applies. The 202 carries a
    Retry-After header saying how long to wait before the first poll, sized on how much work was
    accepted.

    Args:
        idempotency_key (str):
        body (MonitorBulkCreateRequest): The member vocabulary is closed: a member not listed here
            is refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | UnsupportedMediaType
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
