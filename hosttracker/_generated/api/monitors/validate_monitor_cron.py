from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cron_preview_request import CronPreviewRequest
from ...models.cron_preview_view import CronPreviewView
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.validation_failed import ValidationFailed
from ...types import Response


def _get_kwargs(
    *,
    body: CronPreviewRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/monitor/validate-cron",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CronPreviewView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | None
):
    if response.status_code == 200:
        response_200 = CronPreviewView.from_dict(response.json())

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
    CronPreviewView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
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
    body: CronPreviewRequest,
) -> Response[
    CronPreviewView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
]:
    """Check a cron schedule before saving it, and see when it would run.

     Answers whether a monitor write would accept this cron expression for this account and, when it
    would, the next five times it fires - which is what catches an expression that parses perfectly and
    does not mean what its author intended. A schedule that would be refused is still a 200: the answer
    carries valid=false and a reason (the expression cannot be parsed, it never runs, it runs more often
    than once a minute, or the account's package does not include cron scheduling). It reads the same
    validator and the same package limits the monitor write does, so a preview and a save cannot
    disagree.

    Args:
        body (CronPreviewRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CronPreviewView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnknownParameter | ValidationFailed | UnsupportedMediaType]
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
    body: CronPreviewRequest,
) -> (
    CronPreviewView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | None
):
    """Check a cron schedule before saving it, and see when it would run.

     Answers whether a monitor write would accept this cron expression for this account and, when it
    would, the next five times it fires - which is what catches an expression that parses perfectly and
    does not mean what its author intended. A schedule that would be refused is still a 200: the answer
    carries valid=false and a reason (the expression cannot be parsed, it never runs, it runs more often
    than once a minute, or the account's package does not include cron scheduling). It reads the same
    validator and the same package limits the monitor write does, so a preview and a save cannot
    disagree.

    Args:
        body (CronPreviewRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CronPreviewView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnknownParameter | ValidationFailed | UnsupportedMediaType
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CronPreviewRequest,
) -> Response[
    CronPreviewView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
]:
    """Check a cron schedule before saving it, and see when it would run.

     Answers whether a monitor write would accept this cron expression for this account and, when it
    would, the next five times it fires - which is what catches an expression that parses perfectly and
    does not mean what its author intended. A schedule that would be refused is still a 200: the answer
    carries valid=false and a reason (the expression cannot be parsed, it never runs, it runs more often
    than once a minute, or the account's package does not include cron scheduling). It reads the same
    validator and the same package limits the monitor write does, so a preview and a save cannot
    disagree.

    Args:
        body (CronPreviewRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CronPreviewView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnknownParameter | ValidationFailed | UnsupportedMediaType]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CronPreviewRequest,
) -> (
    CronPreviewView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | None
):
    """Check a cron schedule before saving it, and see when it would run.

     Answers whether a monitor write would accept this cron expression for this account and, when it
    would, the next five times it fires - which is what catches an expression that parses perfectly and
    does not mean what its author intended. A schedule that would be refused is still a 200: the answer
    carries valid=false and a reason (the expression cannot be parsed, it never runs, it runs more often
    than once a minute, or the account's package does not include cron scheduling). It reads the same
    validator and the same package limits the monitor write does, so a preview and a save cannot
    disagree.

    Args:
        body (CronPreviewRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CronPreviewView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnknownParameter | ValidationFailed | UnsupportedMediaType
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
