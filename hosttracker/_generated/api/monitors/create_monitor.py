from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_type_not_creatable import ContactTypeNotCreatable
from ...models.credential_write_only import CredentialWriteOnly
from ...models.duplicate_monitor import DuplicateMonitor
from ...models.idempotency_key_conflict import IdempotencyKeyConflict
from ...models.idempotency_key_required import IdempotencyKeyRequired
from ...models.insufficient_agents import InsufficientAgents
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.interval_below_type_floor import IntervalBelowTypeFloor
from ...models.invalid_alert_delay import InvalidAlertDelay
from ...models.invalid_interval import InvalidInterval
from ...models.invalid_settings import InvalidSettings
from ...models.invalid_token import InvalidToken
from ...models.invalid_url import InvalidUrl
from ...models.ip_not_allowed import IpNotAllowed
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.monitor_type_discontinued import MonitorTypeDiscontinued
from ...models.monitor_write_request import MonitorWriteRequest
from ...models.monitor_write_result import MonitorWriteResult
from ...models.package_interval_conflict import PackageIntervalConflict
from ...models.package_limit import PackageLimit
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.too_many_items import TooManyItems
from ...models.unknown_contact_ref import UnknownContactRef
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_parameter import UnknownParameter
from ...models.unknown_pool import UnknownPool
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.unsupported_report_channel import UnsupportedReportChannel
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: MonitorWriteRequest,
    dry_run: bool | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    params: dict[str, Any] = {}

    params["dryRun"] = dry_run

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/monitor",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ContactTypeNotCreatable
    | CredentialWriteOnly
    | InsufficientAgents
    | IntervalBelowTypeFloor
    | InvalidAlertDelay
    | InvalidInterval
    | InvalidSettings
    | InvalidUrl
    | MonitorTypeDiscontinued
    | TooManyItems
    | UnknownContactRef
    | UnknownEnumValue
    | UnknownParameter
    | UnknownPool
    | UnsupportedReportChannel
    | ValidationFailed
    | DuplicateMonitor
    | IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageIntervalConflict
    | PackageLimit
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | MonitorWriteResult
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    if response.status_code == 200:
        response_200 = MonitorWriteResult.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = MonitorWriteResult.from_dict(response.json())

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

        def _parse_response_403(
            data: object,
        ) -> InsufficientRights | IpNotAllowed | MissingScope | PackageIntervalConflict | PackageLimit:
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
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_3 = IpNotAllowed.from_dict(data)

                return response_403_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_403_type_4 = PackageIntervalConflict.from_dict(data)

            return response_403_type_4

        response_403 = _parse_response_403(response.json())

        return response_403

    if response.status_code == 405:
        response_405 = MethodNotAllowed.from_dict(response.json())

        return response_405

    if response.status_code == 409:

        def _parse_response_409(data: object) -> DuplicateMonitor | IdempotencyKeyConflict:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_409_type_0 = DuplicateMonitor.from_dict(data)

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
            | CredentialWriteOnly
            | InsufficientAgents
            | IntervalBelowTypeFloor
            | InvalidAlertDelay
            | InvalidInterval
            | InvalidSettings
            | InvalidUrl
            | MonitorTypeDiscontinued
            | TooManyItems
            | UnknownContactRef
            | UnknownEnumValue
            | UnknownParameter
            | UnknownPool
            | UnsupportedReportChannel
            | ValidationFailed
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = InvalidInterval.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_1 = IntervalBelowTypeFloor.from_dict(data)

                return response_422_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_2 = InsufficientAgents.from_dict(data)

                return response_422_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_3 = UnknownPool.from_dict(data)

                return response_422_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_4 = InvalidAlertDelay.from_dict(data)

                return response_422_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_5 = UnsupportedReportChannel.from_dict(data)

                return response_422_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_6 = MonitorTypeDiscontinued.from_dict(data)

                return response_422_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_7 = InvalidSettings.from_dict(data)

                return response_422_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_8 = CredentialWriteOnly.from_dict(data)

                return response_422_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_9 = UnknownContactRef.from_dict(data)

                return response_422_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_10 = ContactTypeNotCreatable.from_dict(data)

                return response_422_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_11 = ValidationFailed.from_dict(data)

                return response_422_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_12 = InvalidUrl.from_dict(data)

                return response_422_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_13 = UnknownEnumValue.from_dict(data)

                return response_422_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_14 = TooManyItems.from_dict(data)

                return response_422_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_15 = UnknownParameter.from_dict(data)

            return response_422_type_15

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
    | CredentialWriteOnly
    | InsufficientAgents
    | IntervalBelowTypeFloor
    | InvalidAlertDelay
    | InvalidInterval
    | InvalidSettings
    | InvalidUrl
    | MonitorTypeDiscontinued
    | TooManyItems
    | UnknownContactRef
    | UnknownEnumValue
    | UnknownParameter
    | UnknownPool
    | UnsupportedReportChannel
    | ValidationFailed
    | DuplicateMonitor
    | IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageIntervalConflict
    | PackageLimit
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | MonitorWriteResult
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
    body: MonitorWriteRequest,
    dry_run: bool | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    ContactTypeNotCreatable
    | CredentialWriteOnly
    | InsufficientAgents
    | IntervalBelowTypeFloor
    | InvalidAlertDelay
    | InvalidInterval
    | InvalidSettings
    | InvalidUrl
    | MonitorTypeDiscontinued
    | TooManyItems
    | UnknownContactRef
    | UnknownEnumValue
    | UnknownParameter
    | UnknownPool
    | UnsupportedReportChannel
    | ValidationFailed
    | DuplicateMonitor
    | IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageIntervalConflict
    | PackageLimit
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | MonitorWriteResult
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
]:
    """Create a monitor, optionally with its contacts and subscriptions in the same call.

     Creates one monitor of the given type and, in the same request, can create or bind the contacts it
    alerts and wire their alert and report subscriptions - which is what makes a full site setup a
    single call rather than a scripted sequence. Send dryRun=true to validate and preview the resulting
    monitor and contact actions without writing anything. onOverlimit chooses what happens when the
    package has no room: fail (the default) refuses the write, disable creates the monitor disabled with
    a package-limit reason. An Idempotency-Key is required whenever the body carries inline contacts,
    because a retry would otherwise re-send paid confirmation messages. `interval` is optional: omit it
    and the monitor is created at the account's default cadence, or - for a type that publishes
    `fixedInterval` on GET /monitor/type, which the product schedules itself - at that pinned cadence. A
    value sent for a pinned type is still checked against the account's intervals and the type's floor.

    Args:
        dry_run (bool | Unset):
        idempotency_key (str | Unset):
        body (MonitorWriteRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactTypeNotCreatable | CredentialWriteOnly | InsufficientAgents | IntervalBelowTypeFloor | InvalidAlertDelay | InvalidInterval | InvalidSettings | InvalidUrl | MonitorTypeDiscontinued | TooManyItems | UnknownContactRef | UnknownEnumValue | UnknownParameter | UnknownPool | UnsupportedReportChannel | ValidationFailed | DuplicateMonitor | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | PackageIntervalConflict | PackageLimit | InternalError | InvalidToken | MethodNotAllowed | MonitorWriteResult | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
    """

    kwargs = _get_kwargs(
        body=body,
        dry_run=dry_run,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: MonitorWriteRequest,
    dry_run: bool | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> (
    ContactTypeNotCreatable
    | CredentialWriteOnly
    | InsufficientAgents
    | IntervalBelowTypeFloor
    | InvalidAlertDelay
    | InvalidInterval
    | InvalidSettings
    | InvalidUrl
    | MonitorTypeDiscontinued
    | TooManyItems
    | UnknownContactRef
    | UnknownEnumValue
    | UnknownParameter
    | UnknownPool
    | UnsupportedReportChannel
    | ValidationFailed
    | DuplicateMonitor
    | IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageIntervalConflict
    | PackageLimit
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | MonitorWriteResult
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    """Create a monitor, optionally with its contacts and subscriptions in the same call.

     Creates one monitor of the given type and, in the same request, can create or bind the contacts it
    alerts and wire their alert and report subscriptions - which is what makes a full site setup a
    single call rather than a scripted sequence. Send dryRun=true to validate and preview the resulting
    monitor and contact actions without writing anything. onOverlimit chooses what happens when the
    package has no room: fail (the default) refuses the write, disable creates the monitor disabled with
    a package-limit reason. An Idempotency-Key is required whenever the body carries inline contacts,
    because a retry would otherwise re-send paid confirmation messages. `interval` is optional: omit it
    and the monitor is created at the account's default cadence, or - for a type that publishes
    `fixedInterval` on GET /monitor/type, which the product schedules itself - at that pinned cadence. A
    value sent for a pinned type is still checked against the account's intervals and the type's floor.

    Args:
        dry_run (bool | Unset):
        idempotency_key (str | Unset):
        body (MonitorWriteRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactTypeNotCreatable | CredentialWriteOnly | InsufficientAgents | IntervalBelowTypeFloor | InvalidAlertDelay | InvalidInterval | InvalidSettings | InvalidUrl | MonitorTypeDiscontinued | TooManyItems | UnknownContactRef | UnknownEnumValue | UnknownParameter | UnknownPool | UnsupportedReportChannel | ValidationFailed | DuplicateMonitor | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | PackageIntervalConflict | PackageLimit | InternalError | InvalidToken | MethodNotAllowed | MonitorWriteResult | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
    """

    return sync_detailed(
        client=client,
        body=body,
        dry_run=dry_run,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MonitorWriteRequest,
    dry_run: bool | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    ContactTypeNotCreatable
    | CredentialWriteOnly
    | InsufficientAgents
    | IntervalBelowTypeFloor
    | InvalidAlertDelay
    | InvalidInterval
    | InvalidSettings
    | InvalidUrl
    | MonitorTypeDiscontinued
    | TooManyItems
    | UnknownContactRef
    | UnknownEnumValue
    | UnknownParameter
    | UnknownPool
    | UnsupportedReportChannel
    | ValidationFailed
    | DuplicateMonitor
    | IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageIntervalConflict
    | PackageLimit
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | MonitorWriteResult
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
]:
    """Create a monitor, optionally with its contacts and subscriptions in the same call.

     Creates one monitor of the given type and, in the same request, can create or bind the contacts it
    alerts and wire their alert and report subscriptions - which is what makes a full site setup a
    single call rather than a scripted sequence. Send dryRun=true to validate and preview the resulting
    monitor and contact actions without writing anything. onOverlimit chooses what happens when the
    package has no room: fail (the default) refuses the write, disable creates the monitor disabled with
    a package-limit reason. An Idempotency-Key is required whenever the body carries inline contacts,
    because a retry would otherwise re-send paid confirmation messages. `interval` is optional: omit it
    and the monitor is created at the account's default cadence, or - for a type that publishes
    `fixedInterval` on GET /monitor/type, which the product schedules itself - at that pinned cadence. A
    value sent for a pinned type is still checked against the account's intervals and the type's floor.

    Args:
        dry_run (bool | Unset):
        idempotency_key (str | Unset):
        body (MonitorWriteRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactTypeNotCreatable | CredentialWriteOnly | InsufficientAgents | IntervalBelowTypeFloor | InvalidAlertDelay | InvalidInterval | InvalidSettings | InvalidUrl | MonitorTypeDiscontinued | TooManyItems | UnknownContactRef | UnknownEnumValue | UnknownParameter | UnknownPool | UnsupportedReportChannel | ValidationFailed | DuplicateMonitor | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | PackageIntervalConflict | PackageLimit | InternalError | InvalidToken | MethodNotAllowed | MonitorWriteResult | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
    """

    kwargs = _get_kwargs(
        body=body,
        dry_run=dry_run,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MonitorWriteRequest,
    dry_run: bool | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> (
    ContactTypeNotCreatable
    | CredentialWriteOnly
    | InsufficientAgents
    | IntervalBelowTypeFloor
    | InvalidAlertDelay
    | InvalidInterval
    | InvalidSettings
    | InvalidUrl
    | MonitorTypeDiscontinued
    | TooManyItems
    | UnknownContactRef
    | UnknownEnumValue
    | UnknownParameter
    | UnknownPool
    | UnsupportedReportChannel
    | ValidationFailed
    | DuplicateMonitor
    | IdempotencyKeyConflict
    | IdempotencyKeyRequired
    | MalformedRequest
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageIntervalConflict
    | PackageLimit
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | MonitorWriteResult
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    """Create a monitor, optionally with its contacts and subscriptions in the same call.

     Creates one monitor of the given type and, in the same request, can create or bind the contacts it
    alerts and wire their alert and report subscriptions - which is what makes a full site setup a
    single call rather than a scripted sequence. Send dryRun=true to validate and preview the resulting
    monitor and contact actions without writing anything. onOverlimit chooses what happens when the
    package has no room: fail (the default) refuses the write, disable creates the monitor disabled with
    a package-limit reason. An Idempotency-Key is required whenever the body carries inline contacts,
    because a retry would otherwise re-send paid confirmation messages. `interval` is optional: omit it
    and the monitor is created at the account's default cadence, or - for a type that publishes
    `fixedInterval` on GET /monitor/type, which the product schedules itself - at that pinned cadence. A
    value sent for a pinned type is still checked against the account's intervals and the type's floor.

    Args:
        dry_run (bool | Unset):
        idempotency_key (str | Unset):
        body (MonitorWriteRequest): The member vocabulary is closed: a member not listed here is
            refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactTypeNotCreatable | CredentialWriteOnly | InsufficientAgents | IntervalBelowTypeFloor | InvalidAlertDelay | InvalidInterval | InvalidSettings | InvalidUrl | MonitorTypeDiscontinued | TooManyItems | UnknownContactRef | UnknownEnumValue | UnknownParameter | UnknownPool | UnsupportedReportChannel | ValidationFailed | DuplicateMonitor | IdempotencyKeyConflict | IdempotencyKeyRequired | MalformedRequest | InsufficientRights | IpNotAllowed | MissingScope | PackageIntervalConflict | PackageLimit | InternalError | InvalidToken | MethodNotAllowed | MonitorWriteResult | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            dry_run=dry_run,
            idempotency_key=idempotency_key,
        )
    ).parsed
