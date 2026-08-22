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
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.job_accepted_view import JobAcceptedView
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.monitor_bulk_update_request import MonitorBulkUpdateRequest
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.too_many_items import TooManyItems
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: MonitorBulkUpdateRequest | Unset = UNSET,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/monitor/bulk-update",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FilterRequired
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
        ) -> FilterRequired | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed:
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
                response_422_type_2 = FilterRequired.from_dict(data)

                return response_422_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_3 = TooManyItems.from_dict(data)

                return response_422_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_4 = UnknownParameter.from_dict(data)

            return response_422_type_4

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
    body: MonitorBulkUpdateRequest | Unset = UNSET,
    idempotency_key: str,
) -> Response[
    FilterRequired
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
    """Patch, or reset the statistics of, many monitors as one asynchronous job.

     Applies one partial patch, a statistics reset, or both to many monitors at once and answers with the
    job to poll. The target set is named either explicitly by ids or by a filter, and a filter that
    narrows by nothing is refused rather than taken to mean the whole account. Check what a filter
    selects, and that the patch parses, with bulk-update-validate first. Sending both a patch and a
    reset creates two jobs and the response names the second one as well. Tags can be edited as a DELTA
    - addTags and removeTags leave every other tag on each monitor in place, which a patch of tags (a
    replacement) cannot do across a set; the two spellings are mutually exclusive, and each item's
    receipt carries the tags it ended up with. An Idempotency-Key is mandatory: this call answers 202
    and then works asynchronously, so a retry after a timeout would otherwise start a second job over
    the same targets. The 202 carries a Retry-After header saying how long to wait before the first
    poll, sized on how much work was accepted.

    Args:
        idempotency_key (str):
        body (MonitorBulkUpdateRequest | Unset): The member vocabulary is closed: a member not
            listed here is refused rather than ignored. Every member is optional: what the body omits
            is left exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilterRequired | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
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
    body: MonitorBulkUpdateRequest | Unset = UNSET,
    idempotency_key: str,
) -> (
    FilterRequired
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
    """Patch, or reset the statistics of, many monitors as one asynchronous job.

     Applies one partial patch, a statistics reset, or both to many monitors at once and answers with the
    job to poll. The target set is named either explicitly by ids or by a filter, and a filter that
    narrows by nothing is refused rather than taken to mean the whole account. Check what a filter
    selects, and that the patch parses, with bulk-update-validate first. Sending both a patch and a
    reset creates two jobs and the response names the second one as well. Tags can be edited as a DELTA
    - addTags and removeTags leave every other tag on each monitor in place, which a patch of tags (a
    replacement) cannot do across a set; the two spellings are mutually exclusive, and each item's
    receipt carries the tags it ended up with. An Idempotency-Key is mandatory: this call answers 202
    and then works asynchronously, so a retry after a timeout would otherwise start a second job over
    the same targets. The 202 carries a Retry-After header saying how long to wait before the first
    poll, sized on how much work was accepted.

    Args:
        idempotency_key (str):
        body (MonitorBulkUpdateRequest | Unset): The member vocabulary is closed: a member not
            listed here is refused rather than ignored. Every member is optional: what the body omits
            is left exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilterRequired | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MonitorBulkUpdateRequest | Unset = UNSET,
    idempotency_key: str,
) -> Response[
    FilterRequired
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
    """Patch, or reset the statistics of, many monitors as one asynchronous job.

     Applies one partial patch, a statistics reset, or both to many monitors at once and answers with the
    job to poll. The target set is named either explicitly by ids or by a filter, and a filter that
    narrows by nothing is refused rather than taken to mean the whole account. Check what a filter
    selects, and that the patch parses, with bulk-update-validate first. Sending both a patch and a
    reset creates two jobs and the response names the second one as well. Tags can be edited as a DELTA
    - addTags and removeTags leave every other tag on each monitor in place, which a patch of tags (a
    replacement) cannot do across a set; the two spellings are mutually exclusive, and each item's
    receipt carries the tags it ended up with. An Idempotency-Key is mandatory: this call answers 202
    and then works asynchronously, so a retry after a timeout would otherwise start a second job over
    the same targets. The 202 carries a Retry-After header saying how long to wait before the first
    poll, sized on how much work was accepted.

    Args:
        idempotency_key (str):
        body (MonitorBulkUpdateRequest | Unset): The member vocabulary is closed: a member not
            listed here is refused rather than ignored. Every member is optional: what the body omits
            is left exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilterRequired | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
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
    body: MonitorBulkUpdateRequest | Unset = UNSET,
    idempotency_key: str,
) -> (
    FilterRequired
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
    """Patch, or reset the statistics of, many monitors as one asynchronous job.

     Applies one partial patch, a statistics reset, or both to many monitors at once and answers with the
    job to poll. The target set is named either explicitly by ids or by a filter, and a filter that
    narrows by nothing is refused rather than taken to mean the whole account. Check what a filter
    selects, and that the patch parses, with bulk-update-validate first. Sending both a patch and a
    reset creates two jobs and the response names the second one as well. Tags can be edited as a DELTA
    - addTags and removeTags leave every other tag on each monitor in place, which a patch of tags (a
    replacement) cannot do across a set; the two spellings are mutually exclusive, and each item's
    receipt carries the tags it ended up with. An Idempotency-Key is mandatory: this call answers 202
    and then works asynchronously, so a retry after a timeout would otherwise start a second job over
    the same targets. The 202 carries a Retry-After header saying how long to wait before the first
    poll, sized on how much work was accepted.

    Args:
        idempotency_key (str):
        body (MonitorBulkUpdateRequest | Unset): The member vocabulary is closed: a member not
            listed here is refused rather than ignored. Every member is optional: what the body omits
            is left exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilterRequired | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
