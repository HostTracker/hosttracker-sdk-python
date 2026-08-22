from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.credential_write_only import CredentialWriteOnly
from ...models.duplicate_monitor import DuplicateMonitor
from ...models.idempotency_key_conflict import IdempotencyKeyConflict
from ...models.insufficient_agents import InsufficientAgents
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.interval_below_type_floor import IntervalBelowTypeFloor
from ...models.invalid_interval import InvalidInterval
from ...models.invalid_settings import InvalidSettings
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.monitor_patch_request import MonitorPatchRequest
from ...models.monitor_view import MonitorView
from ...models.not_found import NotFound
from ...models.package_interval_conflict import PackageIntervalConflict
from ...models.package_limit import PackageLimit
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.type_immutable import TypeImmutable
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_parameter import UnknownParameter
from ...models.unknown_pool import UnknownPool
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: MonitorPatchRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/monitor/{id}".format(
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
    CredentialWriteOnly
    | InsufficientAgents
    | IntervalBelowTypeFloor
    | InvalidInterval
    | InvalidSettings
    | TypeImmutable
    | UnknownEnumValue
    | UnknownParameter
    | UnknownPool
    | ValidationFailed
    | DuplicateMonitor
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageIntervalConflict
    | PackageLimit
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | MonitorView
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    if response.status_code == 200:
        response_200 = MonitorView.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = MalformedRequest.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = NotFound.from_dict(response.json())

        return response_404

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
            CredentialWriteOnly
            | InsufficientAgents
            | IntervalBelowTypeFloor
            | InvalidInterval
            | InvalidSettings
            | TypeImmutable
            | UnknownEnumValue
            | UnknownParameter
            | UnknownPool
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
                response_422_type_4 = InvalidSettings.from_dict(data)

                return response_422_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_5 = CredentialWriteOnly.from_dict(data)

                return response_422_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_6 = ValidationFailed.from_dict(data)

                return response_422_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_7 = UnknownEnumValue.from_dict(data)

                return response_422_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_8 = TypeImmutable.from_dict(data)

                return response_422_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_9 = UnknownParameter.from_dict(data)

            return response_422_type_9

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
    CredentialWriteOnly
    | InsufficientAgents
    | IntervalBelowTypeFloor
    | InvalidInterval
    | InvalidSettings
    | TypeImmutable
    | UnknownEnumValue
    | UnknownParameter
    | UnknownPool
    | ValidationFailed
    | DuplicateMonitor
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageIntervalConflict
    | PackageLimit
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | MonitorView
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
    body: MonitorPatchRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    CredentialWriteOnly
    | InsufficientAgents
    | IntervalBelowTypeFloor
    | InvalidInterval
    | InvalidSettings
    | TypeImmutable
    | UnknownEnumValue
    | UnknownParameter
    | UnknownPool
    | ValidationFailed
    | DuplicateMonitor
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageIntervalConflict
    | PackageLimit
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | MonitorView
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
]:
    """Partially update a monitor and get the updated resource back.

     Applies a partial update: a member the body omits is left alone, and an explicit null clears an
    optional field. The response is the monitor exactly as a read would render it, so no follow-up fetch
    is needed. A monitor's type cannot change after creation - create a new monitor instead - and inline
    contacts are create-only, so wire additional contacts through the contact endpoints.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (MonitorPatchRequest | Unset): The member vocabulary is closed: a member not listed
            here is refused rather than ignored. Every member is optional: what the body omits is left
            exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CredentialWriteOnly | InsufficientAgents | IntervalBelowTypeFloor | InvalidInterval | InvalidSettings | TypeImmutable | UnknownEnumValue | UnknownParameter | UnknownPool | ValidationFailed | DuplicateMonitor | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | PackageIntervalConflict | PackageLimit | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | MonitorView | NotFound | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
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
    body: MonitorPatchRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> (
    CredentialWriteOnly
    | InsufficientAgents
    | IntervalBelowTypeFloor
    | InvalidInterval
    | InvalidSettings
    | TypeImmutable
    | UnknownEnumValue
    | UnknownParameter
    | UnknownPool
    | ValidationFailed
    | DuplicateMonitor
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageIntervalConflict
    | PackageLimit
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | MonitorView
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    """Partially update a monitor and get the updated resource back.

     Applies a partial update: a member the body omits is left alone, and an explicit null clears an
    optional field. The response is the monitor exactly as a read would render it, so no follow-up fetch
    is needed. A monitor's type cannot change after creation - create a new monitor instead - and inline
    contacts are create-only, so wire additional contacts through the contact endpoints.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (MonitorPatchRequest | Unset): The member vocabulary is closed: a member not listed
            here is refused rather than ignored. Every member is optional: what the body omits is left
            exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CredentialWriteOnly | InsufficientAgents | IntervalBelowTypeFloor | InvalidInterval | InvalidSettings | TypeImmutable | UnknownEnumValue | UnknownParameter | UnknownPool | ValidationFailed | DuplicateMonitor | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | PackageIntervalConflict | PackageLimit | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | MonitorView | NotFound | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
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
    body: MonitorPatchRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    CredentialWriteOnly
    | InsufficientAgents
    | IntervalBelowTypeFloor
    | InvalidInterval
    | InvalidSettings
    | TypeImmutable
    | UnknownEnumValue
    | UnknownParameter
    | UnknownPool
    | ValidationFailed
    | DuplicateMonitor
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageIntervalConflict
    | PackageLimit
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | MonitorView
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
]:
    """Partially update a monitor and get the updated resource back.

     Applies a partial update: a member the body omits is left alone, and an explicit null clears an
    optional field. The response is the monitor exactly as a read would render it, so no follow-up fetch
    is needed. A monitor's type cannot change after creation - create a new monitor instead - and inline
    contacts are create-only, so wire additional contacts through the contact endpoints.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (MonitorPatchRequest | Unset): The member vocabulary is closed: a member not listed
            here is refused rather than ignored. Every member is optional: what the body omits is left
            exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CredentialWriteOnly | InsufficientAgents | IntervalBelowTypeFloor | InvalidInterval | InvalidSettings | TypeImmutable | UnknownEnumValue | UnknownParameter | UnknownPool | ValidationFailed | DuplicateMonitor | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | PackageIntervalConflict | PackageLimit | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | MonitorView | NotFound | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
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
    body: MonitorPatchRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> (
    CredentialWriteOnly
    | InsufficientAgents
    | IntervalBelowTypeFloor
    | InvalidInterval
    | InvalidSettings
    | TypeImmutable
    | UnknownEnumValue
    | UnknownParameter
    | UnknownPool
    | ValidationFailed
    | DuplicateMonitor
    | IdempotencyKeyConflict
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageIntervalConflict
    | PackageLimit
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | MonitorView
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    """Partially update a monitor and get the updated resource back.

     Applies a partial update: a member the body omits is left alone, and an explicit null clears an
    optional field. The response is the monitor exactly as a read would render it, so no follow-up fetch
    is needed. A monitor's type cannot change after creation - create a new monitor instead - and inline
    contacts are create-only, so wire additional contacts through the contact endpoints.

    Args:
        id (UUID):
        idempotency_key (str | Unset):
        body (MonitorPatchRequest | Unset): The member vocabulary is closed: a member not listed
            here is refused rather than ignored. Every member is optional: what the body omits is left
            exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CredentialWriteOnly | InsufficientAgents | IntervalBelowTypeFloor | InvalidInterval | InvalidSettings | TypeImmutable | UnknownEnumValue | UnknownParameter | UnknownPool | ValidationFailed | DuplicateMonitor | IdempotencyKeyConflict | InsufficientRights | IpNotAllowed | MissingScope | PackageIntervalConflict | PackageLimit | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | MonitorView | NotFound | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
