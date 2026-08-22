from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.idempotency_key_conflict import IdempotencyKeyConflict
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.package_limit import PackageLimit
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.report_subscription_bulk_request import ReportSubscriptionBulkRequest
from ...models.subscription_bulk_receipt import SubscriptionBulkReceipt
from ...models.too_many_items import TooManyItems
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.unsupported_report_channel import UnsupportedReportChannel
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ReportSubscriptionBulkRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/report/bulk",
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
    | PackageLimit
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
    | UnsupportedReportChannel
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
        ) -> TooManyItems | UnknownEnumValue | UnknownParameter | UnsupportedReportChannel | ValidationFailed:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = UnsupportedReportChannel.from_dict(data)

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
                response_422_type_2 = UnknownEnumValue.from_dict(data)

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
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
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
    | UnsupportedReportChannel
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
    body: ReportSubscriptionBulkRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
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
    | UnsupportedReportChannel
    | ValidationFailed
    | UnsupportedMediaType
]:
    """Wire and unwire many report subscriptions in one transaction.

     The report twin of the alert diff door: create[] and delete[] hold entries, each the cross product
    of its monitors, its contacts and its frequencies, applied in ONE transaction after the whole
    request validates. Set allMonitors (or allContacts) to mean every one on the account - one side
    only. Scheduled reports go to email contacts: an explicitly named contact of another type is refused
    naming it, and allContacts covers the account's email contacts. A frequency the package does not
    include is refused before anything is written. Both write scopes are required on every call, because
    the door writes on the monitor side and the contact side alike.

    Args:
        idempotency_key (str | Unset):
        body (ReportSubscriptionBulkRequest | Unset): The member vocabulary is closed: a member
            not listed here is refused rather than ignored. Every member is optional: what the body
            omits is left exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | SubscriptionBulkReceipt | TooManyItems | UnknownEnumValue | UnknownParameter | UnsupportedReportChannel | ValidationFailed | UnsupportedMediaType]
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
    body: ReportSubscriptionBulkRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> (
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
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
    | UnsupportedReportChannel
    | ValidationFailed
    | UnsupportedMediaType
    | None
):
    """Wire and unwire many report subscriptions in one transaction.

     The report twin of the alert diff door: create[] and delete[] hold entries, each the cross product
    of its monitors, its contacts and its frequencies, applied in ONE transaction after the whole
    request validates. Set allMonitors (or allContacts) to mean every one on the account - one side
    only. Scheduled reports go to email contacts: an explicitly named contact of another type is refused
    naming it, and allContacts covers the account's email contacts. A frequency the package does not
    include is refused before anything is written. Both write scopes are required on every call, because
    the door writes on the monitor side and the contact side alike.

    Args:
        idempotency_key (str | Unset):
        body (ReportSubscriptionBulkRequest | Unset): The member vocabulary is closed: a member
            not listed here is refused rather than ignored. Every member is optional: what the body
            omits is left exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | SubscriptionBulkReceipt | TooManyItems | UnknownEnumValue | UnknownParameter | UnsupportedReportChannel | ValidationFailed | UnsupportedMediaType
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ReportSubscriptionBulkRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
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
    | UnsupportedReportChannel
    | ValidationFailed
    | UnsupportedMediaType
]:
    """Wire and unwire many report subscriptions in one transaction.

     The report twin of the alert diff door: create[] and delete[] hold entries, each the cross product
    of its monitors, its contacts and its frequencies, applied in ONE transaction after the whole
    request validates. Set allMonitors (or allContacts) to mean every one on the account - one side
    only. Scheduled reports go to email contacts: an explicitly named contact of another type is refused
    naming it, and allContacts covers the account's email contacts. A frequency the package does not
    include is refused before anything is written. Both write scopes are required on every call, because
    the door writes on the monitor side and the contact side alike.

    Args:
        idempotency_key (str | Unset):
        body (ReportSubscriptionBulkRequest | Unset): The member vocabulary is closed: a member
            not listed here is refused rather than ignored. Every member is optional: what the body
            omits is left exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | SubscriptionBulkReceipt | TooManyItems | UnknownEnumValue | UnknownParameter | UnsupportedReportChannel | ValidationFailed | UnsupportedMediaType]
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
    body: ReportSubscriptionBulkRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> (
    IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
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
    | UnsupportedReportChannel
    | ValidationFailed
    | UnsupportedMediaType
    | None
):
    """Wire and unwire many report subscriptions in one transaction.

     The report twin of the alert diff door: create[] and delete[] hold entries, each the cross product
    of its monitors, its contacts and its frequencies, applied in ONE transaction after the whole
    request validates. Set allMonitors (or allContacts) to mean every one on the account - one side
    only. Scheduled reports go to email contacts: an explicitly named contact of another type is refused
    naming it, and allContacts covers the account's email contacts. A frequency the package does not
    include is refused before anything is written. Both write scopes are required on every call, because
    the door writes on the monitor side and the contact side alike.

    Args:
        idempotency_key (str | Unset):
        body (ReportSubscriptionBulkRequest | Unset): The member vocabulary is closed: a member
            not listed here is refused rather than ignored. Every member is optional: what the body
            omits is left exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | PayloadTooLarge | QuotaExceeded | SubscriptionBulkReceipt | TooManyItems | UnknownEnumValue | UnknownParameter | UnsupportedReportChannel | ValidationFailed | UnsupportedMediaType
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
