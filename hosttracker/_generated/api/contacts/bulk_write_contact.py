from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_bulk_request import ContactBulkRequest
from ...models.contact_type_not_creatable import ContactTypeNotCreatable
from ...models.duplicate_contact import DuplicateContact
from ...models.idempotency_key_conflict import IdempotencyKeyConflict
from ...models.idempotency_key_required import IdempotencyKeyRequired
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_alert_delay import InvalidAlertDelay
from ...models.invalid_token import InvalidToken
from ...models.invalid_url import InvalidUrl
from ...models.ip_not_allowed import IpNotAllowed
from ...models.job_accepted_view import JobAcceptedView
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.package_limit import PackageLimit
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.too_many_items import TooManyItems
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.unsupported_report_channel import UnsupportedReportChannel
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ContactBulkRequest | Unset = UNSET,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/contact/bulk",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ContactTypeNotCreatable
    | InvalidAlertDelay
    | InvalidUrl
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | UnsupportedReportChannel
    | ValidationFailed
    | DuplicateContact
    | IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | JobAcceptedView
    | MethodNotAllowed
    | NotFound
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

        def _parse_response_403(data: object) -> InsufficientRights | IpNotAllowed | MissingScope | PackageLimit:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_0 = PackageLimit.from_dict(data)

                return response_403_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_1 = MissingScope.from_dict(data)

                return response_403_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_2 = InsufficientRights.from_dict(data)

                return response_403_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_403_type_3 = IpNotAllowed.from_dict(data)

            return response_403_type_3

        response_403 = _parse_response_403(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = NotFound.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = MethodNotAllowed.from_dict(response.json())

        return response_405

    if response.status_code == 409:

        def _parse_response_409(data: object) -> DuplicateContact | IdempotencyKeyConflict:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_409_type_0 = DuplicateContact.from_dict(data)

                return response_409_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_409_type_1 = IdempotencyKeyConflict.from_dict(data)

            return response_409_type_1

        response_409 = _parse_response_409(response.json())

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
        ) -> (
            ContactTypeNotCreatable
            | InvalidAlertDelay
            | InvalidUrl
            | TooManyItems
            | UnknownEnumValue
            | UnknownParameter
            | UnsupportedReportChannel
            | ValidationFailed
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = InvalidAlertDelay.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_1 = UnsupportedReportChannel.from_dict(data)

                return response_422_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_2 = ContactTypeNotCreatable.from_dict(data)

                return response_422_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_3 = ValidationFailed.from_dict(data)

                return response_422_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_4 = InvalidUrl.from_dict(data)

                return response_422_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_5 = UnknownEnumValue.from_dict(data)

                return response_422_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_6 = TooManyItems.from_dict(data)

                return response_422_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_7 = UnknownParameter.from_dict(data)

            return response_422_type_7

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
    ContactTypeNotCreatable
    | InvalidAlertDelay
    | InvalidUrl
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | UnsupportedReportChannel
    | ValidationFailed
    | DuplicateContact
    | IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | JobAcceptedView
    | MethodNotAllowed
    | NotFound
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
    body: ContactBulkRequest | Unset = UNSET,
    idempotency_key: str,
) -> Response[
    ContactTypeNotCreatable
    | InvalidAlertDelay
    | InvalidUrl
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | UnsupportedReportChannel
    | ValidationFailed
    | DuplicateContact
    | IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | JobAcceptedView
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
]:
    """Create, update and delete many contacts as one asynchronous job.

     Submits a batch of contact creations, updates and deletions as a single job and answers immediately
    with a job id to poll for per-item results. Items are applied one at a time, each in its own
    transaction, so a batch can partially succeed and the job reports exactly which items landed. Check
    a batch in advance with bulk-validate. A create the account's package has no room for is created
    paused rather than refused, unless onOverlimit says otherwise. An Idempotency-Key is mandatory,
    because a retry would duplicate rows and re-send paid confirmation messages. The 202 carries a
    Retry-After header saying how long to wait before the first poll, sized on how much work was
    accepted.

    Args:
        idempotency_key (str):
        body (ContactBulkRequest | Unset): The member vocabulary is closed: a member not listed
            here is refused rather than ignored. Every member is optional: what the body omits is left
            exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactTypeNotCreatable | InvalidAlertDelay | InvalidUrl | TooManyItems | UnknownEnumValue | UnknownParameter | UnsupportedReportChannel | ValidationFailed | DuplicateContact | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
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
    body: ContactBulkRequest | Unset = UNSET,
    idempotency_key: str,
) -> (
    ContactTypeNotCreatable
    | InvalidAlertDelay
    | InvalidUrl
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | UnsupportedReportChannel
    | ValidationFailed
    | DuplicateContact
    | IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | JobAcceptedView
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    """Create, update and delete many contacts as one asynchronous job.

     Submits a batch of contact creations, updates and deletions as a single job and answers immediately
    with a job id to poll for per-item results. Items are applied one at a time, each in its own
    transaction, so a batch can partially succeed and the job reports exactly which items landed. Check
    a batch in advance with bulk-validate. A create the account's package has no room for is created
    paused rather than refused, unless onOverlimit says otherwise. An Idempotency-Key is mandatory,
    because a retry would duplicate rows and re-send paid confirmation messages. The 202 carries a
    Retry-After header saying how long to wait before the first poll, sized on how much work was
    accepted.

    Args:
        idempotency_key (str):
        body (ContactBulkRequest | Unset): The member vocabulary is closed: a member not listed
            here is refused rather than ignored. Every member is optional: what the body omits is left
            exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactTypeNotCreatable | InvalidAlertDelay | InvalidUrl | TooManyItems | UnknownEnumValue | UnknownParameter | UnsupportedReportChannel | ValidationFailed | DuplicateContact | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ContactBulkRequest | Unset = UNSET,
    idempotency_key: str,
) -> Response[
    ContactTypeNotCreatable
    | InvalidAlertDelay
    | InvalidUrl
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | UnsupportedReportChannel
    | ValidationFailed
    | DuplicateContact
    | IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | JobAcceptedView
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
]:
    """Create, update and delete many contacts as one asynchronous job.

     Submits a batch of contact creations, updates and deletions as a single job and answers immediately
    with a job id to poll for per-item results. Items are applied one at a time, each in its own
    transaction, so a batch can partially succeed and the job reports exactly which items landed. Check
    a batch in advance with bulk-validate. A create the account's package has no room for is created
    paused rather than refused, unless onOverlimit says otherwise. An Idempotency-Key is mandatory,
    because a retry would duplicate rows and re-send paid confirmation messages. The 202 carries a
    Retry-After header saying how long to wait before the first poll, sized on how much work was
    accepted.

    Args:
        idempotency_key (str):
        body (ContactBulkRequest | Unset): The member vocabulary is closed: a member not listed
            here is refused rather than ignored. Every member is optional: what the body omits is left
            exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactTypeNotCreatable | InvalidAlertDelay | InvalidUrl | TooManyItems | UnknownEnumValue | UnknownParameter | UnsupportedReportChannel | ValidationFailed | DuplicateContact | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
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
    body: ContactBulkRequest | Unset = UNSET,
    idempotency_key: str,
) -> (
    ContactTypeNotCreatable
    | InvalidAlertDelay
    | InvalidUrl
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | UnsupportedReportChannel
    | ValidationFailed
    | DuplicateContact
    | IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | JobAcceptedView
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    """Create, update and delete many contacts as one asynchronous job.

     Submits a batch of contact creations, updates and deletions as a single job and answers immediately
    with a job id to poll for per-item results. Items are applied one at a time, each in its own
    transaction, so a batch can partially succeed and the job reports exactly which items landed. Check
    a batch in advance with bulk-validate. A create the account's package has no room for is created
    paused rather than refused, unless onOverlimit says otherwise. An Idempotency-Key is mandatory,
    because a retry would duplicate rows and re-send paid confirmation messages. The 202 carries a
    Retry-After header saying how long to wait before the first poll, sized on how much work was
    accepted.

    Args:
        idempotency_key (str):
        body (ContactBulkRequest | Unset): The member vocabulary is closed: a member not listed
            here is refused rather than ignored. Every member is optional: what the body omits is left
            exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactTypeNotCreatable | InvalidAlertDelay | InvalidUrl | TooManyItems | UnknownEnumValue | UnknownParameter | UnsupportedReportChannel | ValidationFailed | DuplicateContact | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | JobAcceptedView | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
