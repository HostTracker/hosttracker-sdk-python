from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.filter_required import FilterRequired
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_settings import InvalidSettings
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.monitor_bulk_delete_validate_view import MonitorBulkDeleteValidateView
from ...models.monitor_bulk_update_validate_request import MonitorBulkUpdateValidateRequest
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.too_many_items import TooManyItems
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: MonitorBulkUpdateValidateRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/monitor/bulk-update-validate",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FilterRequired
    | InvalidSettings
    | TooManyItems
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
    | MonitorBulkDeleteValidateView
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    if response.status_code == 200:
        response_200 = MonitorBulkDeleteValidateView.from_dict(response.json())

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
        ) -> FilterRequired | InvalidSettings | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = InvalidSettings.from_dict(data)

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
                response_422_type_3 = FilterRequired.from_dict(data)

                return response_422_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_4 = TooManyItems.from_dict(data)

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
    FilterRequired
    | InvalidSettings
    | TooManyItems
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
    | MonitorBulkDeleteValidateView
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
    body: MonitorBulkUpdateValidateRequest | Unset = UNSET,
) -> Response[
    FilterRequired
    | InvalidSettings
    | TooManyItems
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
    | MonitorBulkDeleteValidateView
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
]:
    """Check which monitors a bulk edit would touch, without changing anything.

     Takes the same targets a bulk update takes - explicit ids or a filter - and answers how many
    monitors they select together with a sample of them, identified by name, url and type. The patch is
    parsed too, so a malformed change is reported here rather than as one failed item per monitor.
    Nothing is written. Run it before submitting a filter-driven edit, so the set being changed is one a
    human has seen.

    Args:
        body (MonitorBulkUpdateValidateRequest | Unset): The member vocabulary is closed: a member
            not listed here is refused rather than ignored. Every member is optional: what the body
            omits is left exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilterRequired | InvalidSettings | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | MonitorBulkDeleteValidateView | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
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
    body: MonitorBulkUpdateValidateRequest | Unset = UNSET,
) -> (
    FilterRequired
    | InvalidSettings
    | TooManyItems
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
    | MonitorBulkDeleteValidateView
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    """Check which monitors a bulk edit would touch, without changing anything.

     Takes the same targets a bulk update takes - explicit ids or a filter - and answers how many
    monitors they select together with a sample of them, identified by name, url and type. The patch is
    parsed too, so a malformed change is reported here rather than as one failed item per monitor.
    Nothing is written. Run it before submitting a filter-driven edit, so the set being changed is one a
    human has seen.

    Args:
        body (MonitorBulkUpdateValidateRequest | Unset): The member vocabulary is closed: a member
            not listed here is refused rather than ignored. Every member is optional: what the body
            omits is left exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilterRequired | InvalidSettings | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | MonitorBulkDeleteValidateView | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MonitorBulkUpdateValidateRequest | Unset = UNSET,
) -> Response[
    FilterRequired
    | InvalidSettings
    | TooManyItems
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
    | MonitorBulkDeleteValidateView
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
]:
    """Check which monitors a bulk edit would touch, without changing anything.

     Takes the same targets a bulk update takes - explicit ids or a filter - and answers how many
    monitors they select together with a sample of them, identified by name, url and type. The patch is
    parsed too, so a malformed change is reported here rather than as one failed item per monitor.
    Nothing is written. Run it before submitting a filter-driven edit, so the set being changed is one a
    human has seen.

    Args:
        body (MonitorBulkUpdateValidateRequest | Unset): The member vocabulary is closed: a member
            not listed here is refused rather than ignored. Every member is optional: what the body
            omits is left exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilterRequired | InvalidSettings | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | MonitorBulkDeleteValidateView | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MonitorBulkUpdateValidateRequest | Unset = UNSET,
) -> (
    FilterRequired
    | InvalidSettings
    | TooManyItems
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
    | MonitorBulkDeleteValidateView
    | PayloadTooLarge
    | QuotaExceeded
    | UnsupportedMediaType
    | None
):
    """Check which monitors a bulk edit would touch, without changing anything.

     Takes the same targets a bulk update takes - explicit ids or a filter - and answers how many
    monitors they select together with a sample of them, identified by name, url and type. The patch is
    parsed too, so a malformed change is reported here rather than as one failed item per monitor.
    Nothing is written. Run it before submitting a filter-driven edit, so the set being changed is one a
    human has seen.

    Args:
        body (MonitorBulkUpdateValidateRequest | Unset): The member vocabulary is closed: a member
            not listed here is refused rather than ignored. Every member is optional: what the body
            omits is left exactly as it was.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilterRequired | InvalidSettings | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | MonitorBulkDeleteValidateView | PayloadTooLarge | QuotaExceeded | UnsupportedMediaType
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
