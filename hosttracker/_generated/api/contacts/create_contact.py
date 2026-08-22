from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_type_not_creatable import ContactTypeNotCreatable
from ...models.contact_write_request import ContactWriteRequest
from ...models.contact_write_result import ContactWriteResult
from ...models.idempotency_key_conflict import IdempotencyKeyConflict
from ...models.idempotency_key_required import IdempotencyKeyRequired
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_alert_delay import InvalidAlertDelay
from ...models.invalid_token import InvalidToken
from ...models.invalid_url import InvalidUrl
from ...models.ip_not_allowed import IpNotAllowed
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.package_limit import PackageLimit
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.unsupported_report_channel import UnsupportedReportChannel
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ContactWriteRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/contact",
    }

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
    | UnknownEnumValue
    | UnknownParameter
    | UnsupportedReportChannel
    | ValidationFailed
    | ContactWriteResult
    | IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    if response.status_code == 200:
        response_200 = ContactWriteResult.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = ContactWriteResult.from_dict(response.json())

        return response_201

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
        ) -> (
            ContactTypeNotCreatable
            | InvalidAlertDelay
            | InvalidUrl
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
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_6 = UnknownParameter.from_dict(data)

            return response_422_type_6

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
    | UnknownEnumValue
    | UnknownParameter
    | UnsupportedReportChannel
    | ValidationFailed
    | ContactWriteResult
    | IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
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
    body: ContactWriteRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    ContactTypeNotCreatable
    | InvalidAlertDelay
    | InvalidUrl
    | UnknownEnumValue
    | UnknownParameter
    | UnsupportedReportChannel
    | ValidationFailed
    | ContactWriteResult
    | IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
]:
    """Create a contact, or bind to the matching one that already exists.

     Creates a delivery contact and, for a channel that needs confirming, issues and sends its
    confirmation code in the same call. When a contact with the same type, address, gateway and alert
    delay already exists, the request binds to it instead of creating a duplicate - and the status says
    which happened, 201 for a new row and 200 for a bind. Alert and report subscriptions can be wired in
    the same request, riding this same contact:write.

    An `Idempotency-Key` is required, because sending a confirmation code costs money and a retry would
    send it twice. The types it is not required for are `http` and `webPush`, which have no out-of-band
    channel to confirm through and are created already confirmed - so always sending a key is correct
    for every type.

    An `email` address is also checked for deliverability: a domain that publishes no mail host (no MX,
    no A/AAAA fallback, or a null-MX declaration) can only ever bounce, so it is refused as
    `validation_failed` with reason `undeliverable_domain` instead of being stored. The check fails open
    - a DNS error or timeout admits the address - so a resolver hiccup can never lock out a real one.

    `webPush` is created from the browser's own push subscription (`pushSubscription`) instead of an
    `address`, and the server pushes a verification message to it before writing anything: an
    unreachable subscription is refused rather than stored. A browser this account has already
    registered binds to the contact it already has, like any other duplicate key.

    Args:
        idempotency_key (str | Unset):
        body (ContactWriteRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactTypeNotCreatable | InvalidAlertDelay | InvalidUrl | UnknownEnumValue | UnknownParameter | UnsupportedReportChannel | ValidationFailed | ContactWriteResult | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
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
    body: ContactWriteRequest,
    idempotency_key: str | Unset = UNSET,
) -> (
    ContactTypeNotCreatable
    | InvalidAlertDelay
    | InvalidUrl
    | UnknownEnumValue
    | UnknownParameter
    | UnsupportedReportChannel
    | ValidationFailed
    | ContactWriteResult
    | IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    """Create a contact, or bind to the matching one that already exists.

     Creates a delivery contact and, for a channel that needs confirming, issues and sends its
    confirmation code in the same call. When a contact with the same type, address, gateway and alert
    delay already exists, the request binds to it instead of creating a duplicate - and the status says
    which happened, 201 for a new row and 200 for a bind. Alert and report subscriptions can be wired in
    the same request, riding this same contact:write.

    An `Idempotency-Key` is required, because sending a confirmation code costs money and a retry would
    send it twice. The types it is not required for are `http` and `webPush`, which have no out-of-band
    channel to confirm through and are created already confirmed - so always sending a key is correct
    for every type.

    An `email` address is also checked for deliverability: a domain that publishes no mail host (no MX,
    no A/AAAA fallback, or a null-MX declaration) can only ever bounce, so it is refused as
    `validation_failed` with reason `undeliverable_domain` instead of being stored. The check fails open
    - a DNS error or timeout admits the address - so a resolver hiccup can never lock out a real one.

    `webPush` is created from the browser's own push subscription (`pushSubscription`) instead of an
    `address`, and the server pushes a verification message to it before writing anything: an
    unreachable subscription is refused rather than stored. A browser this account has already
    registered binds to the contact it already has, like any other duplicate key.

    Args:
        idempotency_key (str | Unset):
        body (ContactWriteRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactTypeNotCreatable | InvalidAlertDelay | InvalidUrl | UnknownEnumValue | UnknownParameter | UnsupportedReportChannel | ValidationFailed | ContactWriteResult | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ContactWriteRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    ContactTypeNotCreatable
    | InvalidAlertDelay
    | InvalidUrl
    | UnknownEnumValue
    | UnknownParameter
    | UnsupportedReportChannel
    | ValidationFailed
    | ContactWriteResult
    | IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
]:
    """Create a contact, or bind to the matching one that already exists.

     Creates a delivery contact and, for a channel that needs confirming, issues and sends its
    confirmation code in the same call. When a contact with the same type, address, gateway and alert
    delay already exists, the request binds to it instead of creating a duplicate - and the status says
    which happened, 201 for a new row and 200 for a bind. Alert and report subscriptions can be wired in
    the same request, riding this same contact:write.

    An `Idempotency-Key` is required, because sending a confirmation code costs money and a retry would
    send it twice. The types it is not required for are `http` and `webPush`, which have no out-of-band
    channel to confirm through and are created already confirmed - so always sending a key is correct
    for every type.

    An `email` address is also checked for deliverability: a domain that publishes no mail host (no MX,
    no A/AAAA fallback, or a null-MX declaration) can only ever bounce, so it is refused as
    `validation_failed` with reason `undeliverable_domain` instead of being stored. The check fails open
    - a DNS error or timeout admits the address - so a resolver hiccup can never lock out a real one.

    `webPush` is created from the browser's own push subscription (`pushSubscription`) instead of an
    `address`, and the server pushes a verification message to it before writing anything: an
    unreachable subscription is refused rather than stored. A browser this account has already
    registered binds to the contact it already has, like any other duplicate key.

    Args:
        idempotency_key (str | Unset):
        body (ContactWriteRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactTypeNotCreatable | InvalidAlertDelay | InvalidUrl | UnknownEnumValue | UnknownParameter | UnsupportedReportChannel | ValidationFailed | ContactWriteResult | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
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
    body: ContactWriteRequest,
    idempotency_key: str | Unset = UNSET,
) -> (
    ContactTypeNotCreatable
    | InvalidAlertDelay
    | InvalidUrl
    | UnknownEnumValue
    | UnknownParameter
    | UnsupportedReportChannel
    | ValidationFailed
    | ContactWriteResult
    | IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    """Create a contact, or bind to the matching one that already exists.

     Creates a delivery contact and, for a channel that needs confirming, issues and sends its
    confirmation code in the same call. When a contact with the same type, address, gateway and alert
    delay already exists, the request binds to it instead of creating a duplicate - and the status says
    which happened, 201 for a new row and 200 for a bind. Alert and report subscriptions can be wired in
    the same request, riding this same contact:write.

    An `Idempotency-Key` is required, because sending a confirmation code costs money and a retry would
    send it twice. The types it is not required for are `http` and `webPush`, which have no out-of-band
    channel to confirm through and are created already confirmed - so always sending a key is correct
    for every type.

    An `email` address is also checked for deliverability: a domain that publishes no mail host (no MX,
    no A/AAAA fallback, or a null-MX declaration) can only ever bounce, so it is refused as
    `validation_failed` with reason `undeliverable_domain` instead of being stored. The check fails open
    - a DNS error or timeout admits the address - so a resolver hiccup can never lock out a real one.

    `webPush` is created from the browser's own push subscription (`pushSubscription`) instead of an
    `address`, and the server pushes a verification message to it before writing anything: an
    unreachable subscription is refused rather than stored. A browser this account has already
    registered binds to the contact it already has, like any other duplicate key.

    Args:
        idempotency_key (str | Unset):
        body (ContactWriteRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactTypeNotCreatable | InvalidAlertDelay | InvalidUrl | UnknownEnumValue | UnknownParameter | UnsupportedReportChannel | ValidationFailed | ContactWriteResult | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
