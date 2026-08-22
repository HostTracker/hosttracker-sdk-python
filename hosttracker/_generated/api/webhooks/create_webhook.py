from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.duplicate_resource import DuplicateResource
from ...models.idempotency_key_conflict import IdempotencyKeyConflict
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.invalid_url import InvalidUrl
from ...models.ip_not_allowed import IpNotAllowed
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.package_limit import PackageLimit
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.too_many_items import TooManyItems
from ...models.unknown_event_type import UnknownEventType
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.validation_failed import ValidationFailed
from ...models.webhook_view import WebhookView
from ...models.webhook_write_request import WebhookWriteRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: WebhookWriteRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhook",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DuplicateResource
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | InvalidUrl
    | TooManyItems
    | UnknownEventType
    | UnknownParameter
    | ValidationFailed
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | WebhookView
    | None
):
    if response.status_code == 201:
        response_201 = WebhookView.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = MalformedRequest.from_dict(response.json())

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

    if response.status_code == 405:
        response_405 = MethodNotAllowed.from_dict(response.json())

        return response_405

    if response.status_code == 409:

        def _parse_response_409(data: object) -> DuplicateResource | IdempotencyKeyConflict:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_409_type_0 = IdempotencyKeyConflict.from_dict(data)

                return response_409_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_409_type_1 = DuplicateResource.from_dict(data)

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
        ) -> InvalidUrl | TooManyItems | UnknownEventType | UnknownParameter | ValidationFailed:
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
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_2 = InvalidUrl.from_dict(data)

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
    DuplicateResource
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | InvalidUrl
    | TooManyItems
    | UnknownEventType
    | UnknownParameter
    | ValidationFailed
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | WebhookView
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
    body: WebhookWriteRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    DuplicateResource
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | InvalidUrl
    | TooManyItems
    | UnknownEventType
    | UnknownParameter
    | ValidationFailed
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | WebhookView
]:
    """Register a webhook to receive signed event deliveries.

     Registers an endpoint that receives signed HTTP deliveries for the events and monitors you name.
    This response is the only place the full signing secret is ever returned - generate one here or
    supply your own, and store it, because every later read shows only that a secret is set. A url that
    already has a webhook is refused rather than silently duplicated. Optional custom request headers
    travel with every delivery; names in the HT- and webhook- namespaces are reserved for the delivery's
    own headers and are refused.

    Args:
        idempotency_key (str | Unset):
        body (WebhookWriteRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DuplicateResource | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | InvalidUrl | TooManyItems | UnknownEventType | UnknownParameter | ValidationFailed | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType | WebhookView]
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
    body: WebhookWriteRequest,
    idempotency_key: str | Unset = UNSET,
) -> (
    DuplicateResource
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | InvalidUrl
    | TooManyItems
    | UnknownEventType
    | UnknownParameter
    | ValidationFailed
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | WebhookView
    | None
):
    """Register a webhook to receive signed event deliveries.

     Registers an endpoint that receives signed HTTP deliveries for the events and monitors you name.
    This response is the only place the full signing secret is ever returned - generate one here or
    supply your own, and store it, because every later read shows only that a secret is set. A url that
    already has a webhook is refused rather than silently duplicated. Optional custom request headers
    travel with every delivery; names in the HT- and webhook- namespaces are reserved for the delivery's
    own headers and are refused.

    Args:
        idempotency_key (str | Unset):
        body (WebhookWriteRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DuplicateResource | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | InvalidUrl | TooManyItems | UnknownEventType | UnknownParameter | ValidationFailed | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType | WebhookView
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WebhookWriteRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    DuplicateResource
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | InvalidUrl
    | TooManyItems
    | UnknownEventType
    | UnknownParameter
    | ValidationFailed
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | WebhookView
]:
    """Register a webhook to receive signed event deliveries.

     Registers an endpoint that receives signed HTTP deliveries for the events and monitors you name.
    This response is the only place the full signing secret is ever returned - generate one here or
    supply your own, and store it, because every later read shows only that a secret is set. A url that
    already has a webhook is refused rather than silently duplicated. Optional custom request headers
    travel with every delivery; names in the HT- and webhook- namespaces are reserved for the delivery's
    own headers and are refused.

    Args:
        idempotency_key (str | Unset):
        body (WebhookWriteRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DuplicateResource | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | InvalidUrl | TooManyItems | UnknownEventType | UnknownParameter | ValidationFailed | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType | WebhookView]
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
    body: WebhookWriteRequest,
    idempotency_key: str | Unset = UNSET,
) -> (
    DuplicateResource
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | InvalidUrl
    | TooManyItems
    | UnknownEventType
    | UnknownParameter
    | ValidationFailed
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | WebhookView
    | None
):
    """Register a webhook to receive signed event deliveries.

     Registers an endpoint that receives signed HTTP deliveries for the events and monitors you name.
    This response is the only place the full signing secret is ever returned - generate one here or
    supply your own, and store it, because every later read shows only that a secret is set. A url that
    already has a webhook is refused rather than silently duplicated. Optional custom request headers
    travel with every delivery; names in the HT- and webhook- namespaces are reserved for the delivery's
    own headers and are refused.

    Args:
        idempotency_key (str | Unset):
        body (WebhookWriteRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DuplicateResource | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | InvalidUrl | TooManyItems | UnknownEventType | UnknownParameter | ValidationFailed | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType | WebhookView
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
