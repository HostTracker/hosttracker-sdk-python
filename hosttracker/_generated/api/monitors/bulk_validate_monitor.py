from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.monitor_bulk_validate_request import MonitorBulkValidateRequest
from ...models.monitor_bulk_validate_view import MonitorBulkValidateView
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.too_many_items import TooManyItems
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.validation_failed import ValidationFailed
from ...types import Response


def _get_kwargs(
    *,
    body: MonitorBulkValidateRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/monitor/bulk-validate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | MonitorBulkValidateView
    | PayloadTooLarge
    | QuotaExceeded
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | None
):
    if response.status_code == 200:
        response_200 = MonitorBulkValidateView.from_dict(response.json())

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
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | MonitorBulkValidateView
    | PayloadTooLarge
    | QuotaExceeded
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
    body: MonitorBulkValidateRequest,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | MonitorBulkValidateView
    | PayloadTooLarge
    | QuotaExceeded
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
]:
    """Validate a batch of monitor definitions without creating anything.

     Runs the validation a bulk create would run, over the same body, and answers immediately with one
    verdict per item: whether it would be accepted, the errors that would refuse it, and whether the
    account's package still has room for it. The package verdict is computed across the batch in order,
    so item 51 is judged against the room the first fifty would consume. Nothing is written and no job
    is created. It accepts exactly the batch size the create does - the account's own cap - so a batch
    that passes here is one the create will take. It requires the write scope because it evaluates a
    write.

    Args:
        body (MonitorBulkValidateRequest): The member vocabulary is closed: a member not listed
            here is refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | MonitorBulkValidateView | PayloadTooLarge | QuotaExceeded | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | UnsupportedMediaType]
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
    body: MonitorBulkValidateRequest,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | MonitorBulkValidateView
    | PayloadTooLarge
    | QuotaExceeded
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | None
):
    """Validate a batch of monitor definitions without creating anything.

     Runs the validation a bulk create would run, over the same body, and answers immediately with one
    verdict per item: whether it would be accepted, the errors that would refuse it, and whether the
    account's package still has room for it. The package verdict is computed across the batch in order,
    so item 51 is judged against the room the first fifty would consume. Nothing is written and no job
    is created. It accepts exactly the batch size the create does - the account's own cap - so a batch
    that passes here is one the create will take. It requires the write scope because it evaluates a
    write.

    Args:
        body (MonitorBulkValidateRequest): The member vocabulary is closed: a member not listed
            here is refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | MonitorBulkValidateView | PayloadTooLarge | QuotaExceeded | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | UnsupportedMediaType
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MonitorBulkValidateRequest,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | MonitorBulkValidateView
    | PayloadTooLarge
    | QuotaExceeded
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
]:
    """Validate a batch of monitor definitions without creating anything.

     Runs the validation a bulk create would run, over the same body, and answers immediately with one
    verdict per item: whether it would be accepted, the errors that would refuse it, and whether the
    account's package still has room for it. The package verdict is computed across the batch in order,
    so item 51 is judged against the room the first fifty would consume. Nothing is written and no job
    is created. It accepts exactly the batch size the create does - the account's own cap - so a batch
    that passes here is one the create will take. It requires the write scope because it evaluates a
    write.

    Args:
        body (MonitorBulkValidateRequest): The member vocabulary is closed: a member not listed
            here is refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | MonitorBulkValidateView | PayloadTooLarge | QuotaExceeded | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | UnsupportedMediaType]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MonitorBulkValidateRequest,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | MonitorBulkValidateView
    | PayloadTooLarge
    | QuotaExceeded
    | TooManyItems
    | UnknownEnumValue
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | None
):
    """Validate a batch of monitor definitions without creating anything.

     Runs the validation a bulk create would run, over the same body, and answers immediately with one
    verdict per item: whether it would be accepted, the errors that would refuse it, and whether the
    account's package still has room for it. The package verdict is computed across the batch in order,
    so item 51 is judged against the room the first fifty would consume. Nothing is written and no job
    is created. It accepts exactly the batch size the create does - the account's own cap - so a batch
    that passes here is one the create will take. It requires the write scope because it evaluates a
    write.

    Args:
        body (MonitorBulkValidateRequest): The member vocabulary is closed: a member not listed
            here is refused rather than ignored.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | MonitorBulkValidateView | PayloadTooLarge | QuotaExceeded | TooManyItems | UnknownEnumValue | UnknownParameter | ValidationFailed | UnsupportedMediaType
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
