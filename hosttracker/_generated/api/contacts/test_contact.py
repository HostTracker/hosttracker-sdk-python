from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_test_request import ContactTestRequest
from ...models.contact_test_result import ContactTestResult
from ...models.idempotency_key_conflict import IdempotencyKeyConflict
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.package_limit import PackageLimit
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.rate_limited import RateLimited
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.upstream_error import UpstreamError
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: ContactTestRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/contact/{id}/test".format(
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
    ContactTestResult
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | RateLimited
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | UpstreamError
    | None
):
    if response.status_code == 200:
        response_200 = ContactTestResult.from_dict(response.json())

        return response_200

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

        def _parse_response_422(data: object) -> UnknownEnumValue | UnknownParameter | ValidationFailed:
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
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_2 = UnknownParameter.from_dict(data)

            return response_422_type_2

        response_422 = _parse_response_422(response.json())

        return response_422

    if response.status_code == 429:

        def _parse_response_429(data: object) -> QuotaExceeded | RateLimited:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_429_type_0 = QuotaExceeded.from_dict(data)

                return response_429_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_429_type_1 = RateLimited.from_dict(data)

            return response_429_type_1

        response_429 = _parse_response_429(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = InternalError.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = UpstreamError.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ContactTestResult
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | RateLimited
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | UpstreamError
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
    body: ContactTestRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    ContactTestResult
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | RateLimited
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | UpstreamError
]:
    """Send a real test alert to a confirmed contact.

     Sends a test notification through the same delivery pipeline production alerts use, so it proves
    actual delivery rather than only formatting, and reports the outcome synchronously rather than
    handing back a job. Use it while setting an integration up. Test sends are rate-limited, and a
    contact that is not yet confirmed or is suppressed by the account's plan is refused.

    For an `http` contact the answer additionally carries `exchange` - the raw request that was posted
    to the endpoint and the raw response that came back - which is what makes this a webhook diagnostic
    rather than only a delivery outcome.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (ContactTestRequest | Unset): Which alert type the test delivery should render.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactTestResult | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | RateLimited | UnknownEnumValue | UnknownParameter | ValidationFailed | UnsupportedMediaType | UpstreamError]
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
    body: ContactTestRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> (
    ContactTestResult
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | RateLimited
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | UpstreamError
    | None
):
    """Send a real test alert to a confirmed contact.

     Sends a test notification through the same delivery pipeline production alerts use, so it proves
    actual delivery rather than only formatting, and reports the outcome synchronously rather than
    handing back a job. Use it while setting an integration up. Test sends are rate-limited, and a
    contact that is not yet confirmed or is suppressed by the account's plan is refused.

    For an `http` contact the answer additionally carries `exchange` - the raw request that was posted
    to the endpoint and the raw response that came back - which is what makes this a webhook diagnostic
    rather than only a delivery outcome.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (ContactTestRequest | Unset): Which alert type the test delivery should render.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactTestResult | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | RateLimited | UnknownEnumValue | UnknownParameter | ValidationFailed | UnsupportedMediaType | UpstreamError
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
    body: ContactTestRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    ContactTestResult
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | RateLimited
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | UpstreamError
]:
    """Send a real test alert to a confirmed contact.

     Sends a test notification through the same delivery pipeline production alerts use, so it proves
    actual delivery rather than only formatting, and reports the outcome synchronously rather than
    handing back a job. Use it while setting an integration up. Test sends are rate-limited, and a
    contact that is not yet confirmed or is suppressed by the account's plan is refused.

    For an `http` contact the answer additionally carries `exchange` - the raw request that was posted
    to the endpoint and the raw response that came back - which is what makes this a webhook diagnostic
    rather than only a delivery outcome.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (ContactTestRequest | Unset): Which alert type the test delivery should render.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactTestResult | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | RateLimited | UnknownEnumValue | UnknownParameter | ValidationFailed | UnsupportedMediaType | UpstreamError]
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
    body: ContactTestRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> (
    ContactTestResult
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | RateLimited
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | UpstreamError
    | None
):
    """Send a real test alert to a confirmed contact.

     Sends a test notification through the same delivery pipeline production alerts use, so it proves
    actual delivery rather than only formatting, and reports the outcome synchronously rather than
    handing back a job. Use it while setting an integration up. Test sends are rate-limited, and a
    contact that is not yet confirmed or is suppressed by the account's plan is refused.

    For an `http` contact the answer additionally carries `exchange` - the raw request that was posted
    to the endpoint and the raw response that came back - which is what makes this a webhook diagnostic
    rather than only a delivery outcome.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (ContactTestRequest | Unset): Which alert type the test delivery should render.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactTestResult | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | RateLimited | UnknownEnumValue | UnknownParameter | ValidationFailed | UnsupportedMediaType | UpstreamError
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
