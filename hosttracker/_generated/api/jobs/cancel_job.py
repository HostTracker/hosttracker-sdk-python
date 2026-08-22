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
from ...models.invalid_cursor import InvalidCursor
from ...models.invalid_limit import InvalidLimit
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.job_not_cancellable import JobNotCancellable
from ...models.job_view import JobView
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_parameter import UnknownParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/job/{id}/cancel".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    IdempotencyKeyConflict
    | JobNotCancellable
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownParameter
    | InvalidToken
    | JobView
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | None
):
    if response.status_code == 202:
        response_202 = JobView.from_dict(response.json())

        return response_202

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

        def _parse_response_409(data: object) -> IdempotencyKeyConflict | JobNotCancellable:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_409_type_0 = IdempotencyKeyConflict.from_dict(data)

                return response_409_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_409_type_1 = JobNotCancellable.from_dict(data)

            return response_409_type_1

        response_409 = _parse_response_409(response.json())

        return response_409

    if response.status_code == 422:

        def _parse_response_422(data: object) -> InvalidCursor | InvalidLimit | UnknownParameter:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = InvalidCursor.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_1 = InvalidLimit.from_dict(data)

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
    | JobNotCancellable
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownParameter
    | InvalidToken
    | JobView
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
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
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    IdempotencyKeyConflict
    | JobNotCancellable
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownParameter
    | InvalidToken
    | JobView
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
]:
    """Cancel a queued or running asynchronous operation.

     Asks a job that has not finished to stop, and answers with its state and the results it produced
    before stopping. Work already completed is not undone, and the job itself is not removed - it stays
    readable for the rest of its retention window. Cancelling a job that is already cancelling is safe
    and changes nothing; a job that has already reached a final state cannot be cancelled and says so.

    Args:
        id (UUID):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdempotencyKeyConflict | JobNotCancellable | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownParameter | InvalidToken | JobView | MethodNotAllowed | NotFound | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        cursor=cursor,
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
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> (
    IdempotencyKeyConflict
    | JobNotCancellable
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownParameter
    | InvalidToken
    | JobView
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | None
):
    """Cancel a queued or running asynchronous operation.

     Asks a job that has not finished to stop, and answers with its state and the results it produced
    before stopping. Work already completed is not undone, and the job itself is not removed - it stays
    readable for the rest of its retention window. Cancelling a job that is already cancelling is safe
    and changes nothing; a job that has already reached a final state cannot be cancelled and says so.

    Args:
        id (UUID):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdempotencyKeyConflict | JobNotCancellable | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownParameter | InvalidToken | JobView | MethodNotAllowed | NotFound | QuotaExceeded
    """

    return sync_detailed(
        id=id,
        client=client,
        limit=limit,
        cursor=cursor,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    IdempotencyKeyConflict
    | JobNotCancellable
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownParameter
    | InvalidToken
    | JobView
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
]:
    """Cancel a queued or running asynchronous operation.

     Asks a job that has not finished to stop, and answers with its state and the results it produced
    before stopping. Work already completed is not undone, and the job itself is not removed - it stays
    readable for the rest of its retention window. Cancelling a job that is already cancelling is safe
    and changes nothing; a job that has already reached a final state cannot be cancelled and says so.

    Args:
        id (UUID):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdempotencyKeyConflict | JobNotCancellable | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownParameter | InvalidToken | JobView | MethodNotAllowed | NotFound | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        cursor=cursor,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> (
    IdempotencyKeyConflict
    | JobNotCancellable
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownParameter
    | InvalidToken
    | JobView
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | None
):
    """Cancel a queued or running asynchronous operation.

     Asks a job that has not finished to stop, and answers with its state and the results it produced
    before stopping. Work already completed is not undone, and the job itself is not removed - it stays
    readable for the rest of its retention window. Cancelling a job that is already cancelling is safe
    and changes nothing; a job that has already reached a final state cannot be cancelled and says so.

    Args:
        id (UUID):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdempotencyKeyConflict | JobNotCancellable | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownParameter | InvalidToken | JobView | MethodNotAllowed | NotFound | QuotaExceeded
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            limit=limit,
            cursor=cursor,
            idempotency_key=idempotency_key,
        )
    ).parsed
