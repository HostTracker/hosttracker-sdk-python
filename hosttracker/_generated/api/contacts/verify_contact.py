from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_already_confirmed import ContactAlreadyConfirmed
from ...models.contact_verify_request import ContactVerifyRequest
from ...models.contact_view import ContactView
from ...models.idempotency_key_conflict import IdempotencyKeyConflict
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_confirmation_code import InvalidConfirmationCode
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: ContactVerifyRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/contact/{id}/confirmation/verify".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ContactAlreadyConfirmed
    | IdempotencyKeyConflict
    | ContactView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidConfirmationCode
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    if response.status_code == 200:
        response_200 = ContactView.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = NotFound.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = MethodNotAllowed.from_dict(response.json())

        return response_405

    if response.status_code == 409:

        def _parse_response_409(data: object) -> ContactAlreadyConfirmed | IdempotencyKeyConflict:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_409_type_0 = IdempotencyKeyConflict.from_dict(data)

                return response_409_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_409_type_1 = ContactAlreadyConfirmed.from_dict(data)

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

        def _parse_response_422(data: object) -> InvalidConfirmationCode | UnknownParameter | ValidationFailed:
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
                response_422_type_1 = InvalidConfirmationCode.from_dict(data)

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
    ContactAlreadyConfirmed
    | IdempotencyKeyConflict
    | ContactView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidConfirmationCode
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MalformedRequest
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
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: ContactVerifyRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    ContactAlreadyConfirmed
    | IdempotencyKeyConflict
    | ContactView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidConfirmationCode
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
]:
    """Confirm a contact with the code it received.

     Submits the code delivered to a contact and, when it is correct and still valid, marks the contact
    confirmed and answers with the contact as it now stands. A wrong or expired code is refused with how
    many attempts remain and when the code expires, so a client can tell 'try again' from 'ask for a new
    one'. Confirming an already-confirmed contact is reported distinctly from a fresh success.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (ContactVerifyRequest): The confirmation code a contact received.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactAlreadyConfirmed | IdempotencyKeyConflict | ContactView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidConfirmationCode | UnknownParameter | ValidationFailed | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
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
    body: ContactVerifyRequest,
    idempotency_key: str | Unset = UNSET,
) -> (
    ContactAlreadyConfirmed
    | IdempotencyKeyConflict
    | ContactView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidConfirmationCode
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    """Confirm a contact with the code it received.

     Submits the code delivered to a contact and, when it is correct and still valid, marks the contact
    confirmed and answers with the contact as it now stands. A wrong or expired code is refused with how
    many attempts remain and when the code expires, so a client can tell 'try again' from 'ask for a new
    one'. Confirming an already-confirmed contact is reported distinctly from a fresh success.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (ContactVerifyRequest): The confirmation code a contact received.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactAlreadyConfirmed | IdempotencyKeyConflict | ContactView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidConfirmationCode | UnknownParameter | ValidationFailed | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
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
    body: ContactVerifyRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    ContactAlreadyConfirmed
    | IdempotencyKeyConflict
    | ContactView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidConfirmationCode
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
]:
    """Confirm a contact with the code it received.

     Submits the code delivered to a contact and, when it is correct and still valid, marks the contact
    confirmed and answers with the contact as it now stands. A wrong or expired code is refused with how
    many attempts remain and when the code expires, so a client can tell 'try again' from 'ask for a new
    one'. Confirming an already-confirmed contact is reported distinctly from a fresh success.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (ContactVerifyRequest): The confirmation code a contact received.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactAlreadyConfirmed | IdempotencyKeyConflict | ContactView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidConfirmationCode | UnknownParameter | ValidationFailed | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
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
    body: ContactVerifyRequest,
    idempotency_key: str | Unset = UNSET,
) -> (
    ContactAlreadyConfirmed
    | IdempotencyKeyConflict
    | ContactView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidConfirmationCode
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    """Confirm a contact with the code it received.

     Submits the code delivered to a contact and, when it is correct and still valid, marks the contact
    confirmed and answers with the contact as it now stands. A wrong or expired code is refused with how
    many attempts remain and when the code expires, so a client can tell 'try again' from 'ask for a new
    one'. Confirming an already-confirmed contact is reported distinctly from a fresh success.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (ContactVerifyRequest): The confirmation code a contact received.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactAlreadyConfirmed | IdempotencyKeyConflict | ContactView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidConfirmationCode | UnknownParameter | ValidationFailed | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
