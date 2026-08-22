from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.confirmation_view import ConfirmationView
from ...models.contact_already_confirmed import ContactAlreadyConfirmed
from ...models.idempotency_key_conflict import IdempotencyKeyConflict
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.quota_exceeded import QuotaExceeded
from ...models.rate_limited import RateLimited
from ...models.unknown_parameter import UnknownParameter
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/contact/{id}/confirmation".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ConfirmationView
    | ContactAlreadyConfirmed
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | RateLimited
    | UnknownParameter
    | ValidationFailed
    | None
):
    if response.status_code == 200:
        response_200 = ConfirmationView.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = ConfirmationView.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ConfirmationView
    | ContactAlreadyConfirmed
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | RateLimited
    | UnknownParameter
    | ValidationFailed
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
    idempotency_key: str | Unset = UNSET,
) -> Response[
    ConfirmationView
    | ContactAlreadyConfirmed
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | RateLimited
    | UnknownParameter
    | ValidationFailed
]:
    """Resend the confirmation code for an unconfirmed contact.

     Reissues the confirmation code for a contact, for when the code sent at creation never arrived or
    its validity window has passed. A code that is still valid is sent again unchanged rather than
    replaced, so a resend can never invalidate a code the recipient is already reading. Resends are
    rate-limited per contact and a refusal names when to try again.

    Args:
        id (UUID):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmationView | ContactAlreadyConfirmed | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | RateLimited | UnknownParameter | ValidationFailed]
    """

    kwargs = _get_kwargs(
        id=id,
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
    idempotency_key: str | Unset = UNSET,
) -> (
    ConfirmationView
    | ContactAlreadyConfirmed
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | RateLimited
    | UnknownParameter
    | ValidationFailed
    | None
):
    """Resend the confirmation code for an unconfirmed contact.

     Reissues the confirmation code for a contact, for when the code sent at creation never arrived or
    its validity window has passed. A code that is still valid is sent again unchanged rather than
    replaced, so a resend can never invalidate a code the recipient is already reading. Resends are
    rate-limited per contact and a refusal names when to try again.

    Args:
        id (UUID):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfirmationView | ContactAlreadyConfirmed | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | RateLimited | UnknownParameter | ValidationFailed
    """

    return sync_detailed(
        id=id,
        client=client,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    ConfirmationView
    | ContactAlreadyConfirmed
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | RateLimited
    | UnknownParameter
    | ValidationFailed
]:
    """Resend the confirmation code for an unconfirmed contact.

     Reissues the confirmation code for a contact, for when the code sent at creation never arrived or
    its validity window has passed. A code that is still valid is sent again unchanged rather than
    replaced, so a resend can never invalidate a code the recipient is already reading. Resends are
    rate-limited per contact and a refusal names when to try again.

    Args:
        id (UUID):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfirmationView | ContactAlreadyConfirmed | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | RateLimited | UnknownParameter | ValidationFailed]
    """

    kwargs = _get_kwargs(
        id=id,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> (
    ConfirmationView
    | ContactAlreadyConfirmed
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | RateLimited
    | UnknownParameter
    | ValidationFailed
    | None
):
    """Resend the confirmation code for an unconfirmed contact.

     Reissues the confirmation code for a contact, for when the code sent at creation never arrived or
    its validity window has passed. A code that is still valid is sent again unchanged rather than
    replaced, so a resend can never invalidate a code the recipient is already reading. Resends are
    rate-limited per contact and a refusal names when to try again.

    Args:
        id (UUID):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfirmationView | ContactAlreadyConfirmed | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | RateLimited | UnknownParameter | ValidationFailed
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            idempotency_key=idempotency_key,
        )
    ).parsed
