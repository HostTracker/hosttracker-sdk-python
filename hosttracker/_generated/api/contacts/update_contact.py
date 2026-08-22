from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_patch_request import ContactPatchRequest
from ...models.contact_write_result import ContactWriteResult
from ...models.duplicate_contact import DuplicateContact
from ...models.idempotency_key_conflict import IdempotencyKeyConflict
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_alert_delay import InvalidAlertDelay
from ...models.invalid_token import InvalidToken
from ...models.invalid_url import InvalidUrl
from ...models.ip_not_allowed import IpNotAllowed
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.type_immutable import TypeImmutable
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: ContactPatchRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/contact/{id}".format(
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
    ContactWriteResult
    | DuplicateContact
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidAlertDelay
    | InvalidUrl
    | TypeImmutable
    | UnknownEnumValue
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
        response_200 = ContactWriteResult.from_dict(response.json())

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
        ) -> InvalidAlertDelay | InvalidUrl | TypeImmutable | UnknownEnumValue | UnknownParameter | ValidationFailed:
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
                response_422_type_3 = UnknownEnumValue.from_dict(data)

                return response_422_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_4 = TypeImmutable.from_dict(data)

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
    ContactWriteResult
    | DuplicateContact
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidAlertDelay
    | InvalidUrl
    | TypeImmutable
    | UnknownEnumValue
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
    body: ContactPatchRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    ContactWriteResult
    | DuplicateContact
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidAlertDelay
    | InvalidUrl
    | TypeImmutable
    | UnknownEnumValue
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
    """Partially update a contact and get the updated contact back.

     Updates one or more members of a contact; a member the body omits stays as it was, and an explicit
    null clears an optional one. Changing the delivery address resets confirmation and sends a fresh
    code, because the new address has never proved it belongs to you. A NEW email address is also
    checked for deliverability, exactly as on create: a domain with no mail host is refused as
    `validation_failed` with reason `undeliverable_domain` (fail-open on DNS trouble; a body that does
    not touch `address` is never checked). A contact's type cannot change after creation - create
    another contact instead.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (ContactPatchRequest | Unset): The member vocabulary is closed: a member not listed
            here is refused rather than ignored. Every member is optional: what the body omits is left
            exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactWriteResult | DuplicateContact | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidAlertDelay | InvalidUrl | TypeImmutable | UnknownEnumValue | UnknownParameter | ValidationFailed | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
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
    body: ContactPatchRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> (
    ContactWriteResult
    | DuplicateContact
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidAlertDelay
    | InvalidUrl
    | TypeImmutable
    | UnknownEnumValue
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
    """Partially update a contact and get the updated contact back.

     Updates one or more members of a contact; a member the body omits stays as it was, and an explicit
    null clears an optional one. Changing the delivery address resets confirmation and sends a fresh
    code, because the new address has never proved it belongs to you. A NEW email address is also
    checked for deliverability, exactly as on create: a domain with no mail host is refused as
    `validation_failed` with reason `undeliverable_domain` (fail-open on DNS trouble; a body that does
    not touch `address` is never checked). A contact's type cannot change after creation - create
    another contact instead.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (ContactPatchRequest | Unset): The member vocabulary is closed: a member not listed
            here is refused rather than ignored. Every member is optional: what the body omits is left
            exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactWriteResult | DuplicateContact | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidAlertDelay | InvalidUrl | TypeImmutable | UnknownEnumValue | UnknownParameter | ValidationFailed | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
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
    body: ContactPatchRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    ContactWriteResult
    | DuplicateContact
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidAlertDelay
    | InvalidUrl
    | TypeImmutable
    | UnknownEnumValue
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
    """Partially update a contact and get the updated contact back.

     Updates one or more members of a contact; a member the body omits stays as it was, and an explicit
    null clears an optional one. Changing the delivery address resets confirmation and sends a fresh
    code, because the new address has never proved it belongs to you. A NEW email address is also
    checked for deliverability, exactly as on create: a domain with no mail host is refused as
    `validation_failed` with reason `undeliverable_domain` (fail-open on DNS trouble; a body that does
    not touch `address` is never checked). A contact's type cannot change after creation - create
    another contact instead.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (ContactPatchRequest | Unset): The member vocabulary is closed: a member not listed
            here is refused rather than ignored. Every member is optional: what the body omits is left
            exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactWriteResult | DuplicateContact | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidAlertDelay | InvalidUrl | TypeImmutable | UnknownEnumValue | UnknownParameter | ValidationFailed | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
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
    body: ContactPatchRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> (
    ContactWriteResult
    | DuplicateContact
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidAlertDelay
    | InvalidUrl
    | TypeImmutable
    | UnknownEnumValue
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
    """Partially update a contact and get the updated contact back.

     Updates one or more members of a contact; a member the body omits stays as it was, and an explicit
    null clears an optional one. Changing the delivery address resets confirmation and sends a fresh
    code, because the new address has never proved it belongs to you. A NEW email address is also
    checked for deliverability, exactly as on create: a domain with no mail host is refused as
    `validation_failed` with reason `undeliverable_domain` (fail-open on DNS trouble; a body that does
    not touch `address` is never checked). A contact's type cannot change after creation - create
    another contact instead.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (ContactPatchRequest | Unset): The member vocabulary is closed: a member not listed
            here is refused rather than ignored. Every member is optional: what the body omits is left
            exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactWriteResult | DuplicateContact | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidAlertDelay | InvalidUrl | TypeImmutable | UnknownEnumValue | UnknownParameter | ValidationFailed | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
