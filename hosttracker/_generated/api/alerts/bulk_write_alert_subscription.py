from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_subscription_bulk_request import AlertSubscriptionBulkRequest
from ...models.idempotency_key_conflict import IdempotencyKeyConflict
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.subscription_bulk_receipt import SubscriptionBulkReceipt
from ...models.too_many_items import TooManyItems
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AlertSubscriptionBulkRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/alert/bulk",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | SubscriptionBulkReceipt
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | None
):
    if response.status_code == 200:
        response_200 = SubscriptionBulkReceipt.from_dict(response.json())

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

        def _parse_response_422(data: object) -> TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed:
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
                response_422_type_2 = TooManyItems.from_dict(data)

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
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | SubscriptionBulkReceipt
    | TooManyItems
    | UnknownEnumValue
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
    body: AlertSubscriptionBulkRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | SubscriptionBulkReceipt
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
]:
    """Wire and unwire many alert subscriptions in one transaction.

     Applies a whole subscription change at once: create[] and delete[] each hold entries, and an entry
    is the cross product of its monitors, its contacts and its alert types. Set allMonitors (or
    allContacts) to let the entries that omit that list mean every one on the account - only one of the
    two sides may be a wildcard, and an entry may not name a list the wildcard already covers. Use it
    instead of the per-pair PUT whenever more than one pair changes: everything is validated first and
    applied in ONE transaction, so a partial result is impossible, and an id the account does not own is
    refused naming the entry it came from. The answer says what actually changed. Both write scopes are
    required on every call, because the door writes on the monitor side and the contact side alike.

    Args:
        idempotency_key (str | Unset):
        body (AlertSubscriptionBulkRequest | Unset): The member vocabulary is closed: a member not
            listed here is refused rather than ignored. Every member is optional: what the body omits
            is left exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | SubscriptionBulkReceipt | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | UnsupportedMediaType]
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
    body: AlertSubscriptionBulkRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> (
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | SubscriptionBulkReceipt
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | None
):
    """Wire and unwire many alert subscriptions in one transaction.

     Applies a whole subscription change at once: create[] and delete[] each hold entries, and an entry
    is the cross product of its monitors, its contacts and its alert types. Set allMonitors (or
    allContacts) to let the entries that omit that list mean every one on the account - only one of the
    two sides may be a wildcard, and an entry may not name a list the wildcard already covers. Use it
    instead of the per-pair PUT whenever more than one pair changes: everything is validated first and
    applied in ONE transaction, so a partial result is impossible, and an id the account does not own is
    refused naming the entry it came from. The answer says what actually changed. Both write scopes are
    required on every call, because the door writes on the monitor side and the contact side alike.

    Args:
        idempotency_key (str | Unset):
        body (AlertSubscriptionBulkRequest | Unset): The member vocabulary is closed: a member not
            listed here is refused rather than ignored. Every member is optional: what the body omits
            is left exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | SubscriptionBulkReceipt | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | UnsupportedMediaType
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AlertSubscriptionBulkRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | SubscriptionBulkReceipt
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
]:
    """Wire and unwire many alert subscriptions in one transaction.

     Applies a whole subscription change at once: create[] and delete[] each hold entries, and an entry
    is the cross product of its monitors, its contacts and its alert types. Set allMonitors (or
    allContacts) to let the entries that omit that list mean every one on the account - only one of the
    two sides may be a wildcard, and an entry may not name a list the wildcard already covers. Use it
    instead of the per-pair PUT whenever more than one pair changes: everything is validated first and
    applied in ONE transaction, so a partial result is impossible, and an id the account does not own is
    refused naming the entry it came from. The answer says what actually changed. Both write scopes are
    required on every call, because the door writes on the monitor side and the contact side alike.

    Args:
        idempotency_key (str | Unset):
        body (AlertSubscriptionBulkRequest | Unset): The member vocabulary is closed: a member not
            listed here is refused rather than ignored. Every member is optional: what the body omits
            is left exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | SubscriptionBulkReceipt | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | UnsupportedMediaType]
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
    body: AlertSubscriptionBulkRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> (
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | SubscriptionBulkReceipt
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | None
):
    """Wire and unwire many alert subscriptions in one transaction.

     Applies a whole subscription change at once: create[] and delete[] each hold entries, and an entry
    is the cross product of its monitors, its contacts and its alert types. Set allMonitors (or
    allContacts) to let the entries that omit that list mean every one on the account - only one of the
    two sides may be a wildcard, and an entry may not name a list the wildcard already covers. Use it
    instead of the per-pair PUT whenever more than one pair changes: everything is validated first and
    applied in ONE transaction, so a partial result is impossible, and an id the account does not own is
    refused naming the entry it came from. The answer says what actually changed. Both write scopes are
    required on every call, because the door writes on the monitor side and the contact side alike.

    Args:
        idempotency_key (str | Unset):
        body (AlertSubscriptionBulkRequest | Unset): The member vocabulary is closed: a member not
            listed here is refused rather than ignored. Every member is optional: what the body omits
            is left exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | SubscriptionBulkReceipt | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | UnsupportedMediaType
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
