from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_bulk_delete_validate_request import ContactBulkDeleteValidateRequest
from ...models.contact_bulk_delete_validate_view import ContactBulkDeleteValidateView
from ...models.filter_required import FilterRequired
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.validation_failed import ValidationFailed
from ...types import Response


def _get_kwargs(
    *,
    body: ContactBulkDeleteValidateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/contact/bulk-delete-validate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ContactBulkDeleteValidateView
    | FilterRequired
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    if response.status_code == 200:
        response_200 = ContactBulkDeleteValidateView.from_dict(response.json())

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

        def _parse_response_422(
            data: object,
        ) -> FilterRequired | UnknownEnumValue | UnknownParameter | ValidationFailed:
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
    ContactBulkDeleteValidateView
    | FilterRequired
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
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
    body: ContactBulkDeleteValidateRequest,
) -> Response[
    ContactBulkDeleteValidateView
    | FilterRequired
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
]:
    """Check which contacts a delete filter selects, without deleting anything.

     Resolves a filter and answers how many contacts it selects together with a sample of them,
    identified by name and address. Nothing is written. It is the verification step of a bulk delete:
    run it, show a human what is about to go, then send the same filter to the delete itself, which acts
    on it directly. The answer is a snapshot - contacts created or removed between the two calls change
    what the delete resolves, which is why the delete reports its own count as well.

    Args:
        body (ContactBulkDeleteValidateRequest): The member vocabulary is closed: a member not
            listed here is refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactBulkDeleteValidateView | FilterRequired | UnknownEnumValue | UnknownParameter | ValidationFailed | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
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
    body: ContactBulkDeleteValidateRequest,
) -> (
    ContactBulkDeleteValidateView
    | FilterRequired
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    """Check which contacts a delete filter selects, without deleting anything.

     Resolves a filter and answers how many contacts it selects together with a sample of them,
    identified by name and address. Nothing is written. It is the verification step of a bulk delete:
    run it, show a human what is about to go, then send the same filter to the delete itself, which acts
    on it directly. The answer is a snapshot - contacts created or removed between the two calls change
    what the delete resolves, which is why the delete reports its own count as well.

    Args:
        body (ContactBulkDeleteValidateRequest): The member vocabulary is closed: a member not
            listed here is refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactBulkDeleteValidateView | FilterRequired | UnknownEnumValue | UnknownParameter | ValidationFailed | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ContactBulkDeleteValidateRequest,
) -> Response[
    ContactBulkDeleteValidateView
    | FilterRequired
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
]:
    """Check which contacts a delete filter selects, without deleting anything.

     Resolves a filter and answers how many contacts it selects together with a sample of them,
    identified by name and address. Nothing is written. It is the verification step of a bulk delete:
    run it, show a human what is about to go, then send the same filter to the delete itself, which acts
    on it directly. The answer is a snapshot - contacts created or removed between the two calls change
    what the delete resolves, which is why the delete reports its own count as well.

    Args:
        body (ContactBulkDeleteValidateRequest): The member vocabulary is closed: a member not
            listed here is refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactBulkDeleteValidateView | FilterRequired | UnknownEnumValue | UnknownParameter | ValidationFailed | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ContactBulkDeleteValidateRequest,
) -> (
    ContactBulkDeleteValidateView
    | FilterRequired
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    """Check which contacts a delete filter selects, without deleting anything.

     Resolves a filter and answers how many contacts it selects together with a sample of them,
    identified by name and address. Nothing is written. It is the verification step of a bulk delete:
    run it, show a human what is about to go, then send the same filter to the delete itself, which acts
    on it directly. The answer is a snapshot - contacts created or removed between the two calls change
    what the delete resolves, which is why the delete reports its own count as well.

    Args:
        body (ContactBulkDeleteValidateRequest): The member vocabulary is closed: a member not
            listed here is refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactBulkDeleteValidateView | FilterRequired | UnknownEnumValue | UnknownParameter | ValidationFailed | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
