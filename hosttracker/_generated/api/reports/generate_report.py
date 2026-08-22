from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.filter_required import FilterRequired
from ...models.idempotency_key_conflict import IdempotencyKeyConflict
from ...models.idempotency_key_required import IdempotencyKeyRequired
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_range import InvalidRange
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.job_accepted_view import JobAcceptedView
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.report_generate_request import ReportGenerateRequest
from ...models.too_many_items import TooManyItems
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.validation_failed import ValidationFailed
from ...types import Response


def _get_kwargs(
    *,
    body: ReportGenerateRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/monitor/report",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FilterRequired
    | InvalidRange
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | IdempotencyKeyConflict
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

        def _parse_response_422(
            data: object,
        ) -> FilterRequired | InvalidRange | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed:
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
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_3 = FilterRequired.from_dict(data)

                return response_422_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_4 = TooManyItems.from_dict(data)

                return response_422_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_5 = UnknownParameter.from_dict(data)

            return response_422_type_5

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
    FilterRequired
    | InvalidRange
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | IdempotencyKeyConflict
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
    body: ReportGenerateRequest,
    idempotency_key: str,
) -> Response[
    FilterRequired
    | InvalidRange
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | IdempotencyKeyConflict
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
    | UnsupportedMediaType
]:
    """Request a report over a set of monitors and a time range.

     Submits a rendering request and answers with a job id while the document is produced in the
    background - rendering can take a while and the service sheds load under pressure, so an inline wait
    would be the wrong contract. Poll the job, or name a webhook to be called when it finishes. The
    monitor list is explicit and required, so a report can never quietly cover the whole account. An
    Idempotency-Key is mandatory: this call answers 202 and then renders in the background, so a retry
    after a timeout would otherwise queue a second rendering of the same report. The 202 carries a
    Retry-After header saying how long to wait before the first poll, sized on how much work was
    accepted.

    Args:
        idempotency_key (str):
        body (ReportGenerateRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilterRequired | InvalidRange | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
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
    body: ReportGenerateRequest,
    idempotency_key: str,
) -> (
    FilterRequired
    | InvalidRange
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | IdempotencyKeyConflict
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
    | UnsupportedMediaType
    | None
):
    """Request a report over a set of monitors and a time range.

     Submits a rendering request and answers with a job id while the document is produced in the
    background - rendering can take a while and the service sheds load under pressure, so an inline wait
    would be the wrong contract. Poll the job, or name a webhook to be called when it finishes. The
    monitor list is explicit and required, so a report can never quietly cover the whole account. An
    Idempotency-Key is mandatory: this call answers 202 and then renders in the background, so a retry
    after a timeout would otherwise queue a second rendering of the same report. The 202 carries a
    Retry-After header saying how long to wait before the first poll, sized on how much work was
    accepted.

    Args:
        idempotency_key (str):
        body (ReportGenerateRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilterRequired | InvalidRange | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ReportGenerateRequest,
    idempotency_key: str,
) -> Response[
    FilterRequired
    | InvalidRange
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | IdempotencyKeyConflict
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
    | UnsupportedMediaType
]:
    """Request a report over a set of monitors and a time range.

     Submits a rendering request and answers with a job id while the document is produced in the
    background - rendering can take a while and the service sheds load under pressure, so an inline wait
    would be the wrong contract. Poll the job, or name a webhook to be called when it finishes. The
    monitor list is explicit and required, so a report can never quietly cover the whole account. An
    Idempotency-Key is mandatory: this call answers 202 and then renders in the background, so a retry
    after a timeout would otherwise queue a second rendering of the same report. The 202 carries a
    Retry-After header saying how long to wait before the first poll, sized on how much work was
    accepted.

    Args:
        idempotency_key (str):
        body (ReportGenerateRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilterRequired | InvalidRange | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
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
    body: ReportGenerateRequest,
    idempotency_key: str,
) -> (
    FilterRequired
    | InvalidRange
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | IdempotencyKeyConflict
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
    | UnsupportedMediaType
    | None
):
    """Request a report over a set of monitors and a time range.

     Submits a rendering request and answers with a job id while the document is produced in the
    background - rendering can take a while and the service sheds load under pressure, so an inline wait
    would be the wrong contract. Poll the job, or name a webhook to be called when it finishes. The
    monitor list is explicit and required, so a report can never quietly cover the whole account. An
    Idempotency-Key is mandatory: this call answers 202 and then renders in the background, so a retry
    after a timeout would otherwise queue a second rendering of the same report. The 202 carries a
    Retry-After header saying how long to wait before the first poll, sized on how much work was
    accepted.

    Args:
        idempotency_key (str):
        body (ReportGenerateRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilterRequired | InvalidRange | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
