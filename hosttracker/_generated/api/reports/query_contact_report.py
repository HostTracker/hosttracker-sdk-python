from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_report_query_request import ContactReportQueryRequest
from ...models.contact_report_subscription_page import ContactReportSubscriptionPage
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.malformed_request import MalformedRequest
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.payload_too_large import PayloadTooLarge
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...models.unsupported_media_type import UnsupportedMediaType
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    body: ContactReportQueryRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/contact/{id}/report/q".format(
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
    ContactReportSubscriptionPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | None
):
    if response.status_code == 200:
        response_200 = ContactReportSubscriptionPage.from_dict(response.json())

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

    if response.status_code == 413:
        response_413 = PayloadTooLarge.from_dict(response.json())

        return response_413

    if response.status_code == 415:
        response_415 = UnsupportedMediaType.from_dict(response.json())

        return response_415

    if response.status_code == 422:

        def _parse_response_422(data: object) -> UnknownField | UnknownParameter | ValidationFailed:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = UnknownField.from_dict(data)

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
    ContactReportSubscriptionPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnknownField
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
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: ContactReportQueryRequest | Unset = UNSET,
) -> Response[
    ContactReportSubscriptionPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
]:
    """Query the same collection as listContactReport, with the parameters in a JSON body.

     Takes exactly the parameters listContactReport accepts on the query string, as one JSON object: a
    list-valued filter as a JSON array, everything else as a string, number or boolean, and null for a
    parameter you are not sending. An empty object reads the collection unfiltered. The answer is byte-
    identical to what listContactReport returns for the same values, and the caller needs the same scope
    - this is a read that happens to use POST, so it starts no job, writes nothing and takes no
    idempotency key. Reach for it when the filter is too long or too awkward for a url - a few hundred
    ids, free text carrying reserved characters - and stay on listContactReport otherwise, since a GET
    can be cached and a POST cannot. A member this operation does not define is refused, exactly as an
    unknown query parameter is.

    Args:
        id (UUID):
        body (ContactReportQueryRequest | Unset): The parameters, as one JSON object. A list-
            valued filter is a JSON array; everything else is a string, number or boolean. An omitted
            member and an explicit null both mean the parameter was not sent, and an empty array means
            it was sent empty - which every list filter refuses, exactly as it refuses an empty value
            on the query string.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactReportSubscriptionPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnknownField | UnknownParameter | ValidationFailed | UnsupportedMediaType]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: ContactReportQueryRequest | Unset = UNSET,
) -> (
    ContactReportSubscriptionPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | None
):
    """Query the same collection as listContactReport, with the parameters in a JSON body.

     Takes exactly the parameters listContactReport accepts on the query string, as one JSON object: a
    list-valued filter as a JSON array, everything else as a string, number or boolean, and null for a
    parameter you are not sending. An empty object reads the collection unfiltered. The answer is byte-
    identical to what listContactReport returns for the same values, and the caller needs the same scope
    - this is a read that happens to use POST, so it starts no job, writes nothing and takes no
    idempotency key. Reach for it when the filter is too long or too awkward for a url - a few hundred
    ids, free text carrying reserved characters - and stay on listContactReport otherwise, since a GET
    can be cached and a POST cannot. A member this operation does not define is refused, exactly as an
    unknown query parameter is.

    Args:
        id (UUID):
        body (ContactReportQueryRequest | Unset): The parameters, as one JSON object. A list-
            valued filter is a JSON array; everything else is a string, number or boolean. An omitted
            member and an explicit null both mean the parameter was not sent, and an empty array means
            it was sent empty - which every list filter refuses, exactly as it refuses an empty value
            on the query string.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactReportSubscriptionPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnknownField | UnknownParameter | ValidationFailed | UnsupportedMediaType
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: ContactReportQueryRequest | Unset = UNSET,
) -> Response[
    ContactReportSubscriptionPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
]:
    """Query the same collection as listContactReport, with the parameters in a JSON body.

     Takes exactly the parameters listContactReport accepts on the query string, as one JSON object: a
    list-valued filter as a JSON array, everything else as a string, number or boolean, and null for a
    parameter you are not sending. An empty object reads the collection unfiltered. The answer is byte-
    identical to what listContactReport returns for the same values, and the caller needs the same scope
    - this is a read that happens to use POST, so it starts no job, writes nothing and takes no
    idempotency key. Reach for it when the filter is too long or too awkward for a url - a few hundred
    ids, free text carrying reserved characters - and stay on listContactReport otherwise, since a GET
    can be cached and a POST cannot. A member this operation does not define is refused, exactly as an
    unknown query parameter is.

    Args:
        id (UUID):
        body (ContactReportQueryRequest | Unset): The parameters, as one JSON object. A list-
            valued filter is a JSON array; everything else is a string, number or boolean. An omitted
            member and an explicit null both mean the parameter was not sent, and an empty array means
            it was sent empty - which every list filter refuses, exactly as it refuses an empty value
            on the query string.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactReportSubscriptionPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnknownField | UnknownParameter | ValidationFailed | UnsupportedMediaType]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: ContactReportQueryRequest | Unset = UNSET,
) -> (
    ContactReportSubscriptionPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MalformedRequest
    | MethodNotAllowed
    | NotFound
    | PayloadTooLarge
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | UnsupportedMediaType
    | None
):
    """Query the same collection as listContactReport, with the parameters in a JSON body.

     Takes exactly the parameters listContactReport accepts on the query string, as one JSON object: a
    list-valued filter as a JSON array, everything else as a string, number or boolean, and null for a
    parameter you are not sending. An empty object reads the collection unfiltered. The answer is byte-
    identical to what listContactReport returns for the same values, and the caller needs the same scope
    - this is a read that happens to use POST, so it starts no job, writes nothing and takes no
    idempotency key. Reach for it when the filter is too long or too awkward for a url - a few hundred
    ids, free text carrying reserved characters - and stay on listContactReport otherwise, since a GET
    can be cached and a POST cannot. A member this operation does not define is refused, exactly as an
    unknown query parameter is.

    Args:
        id (UUID):
        body (ContactReportQueryRequest | Unset): The parameters, as one JSON object. A list-
            valued filter is a JSON array; everything else is a string, number or boolean. An omitted
            member and an explicit null both mean the parameter was not sent, and an empty array means
            it was sent empty - which every list filter refuses, exactly as it refuses an empty value
            on the query string.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactReportSubscriptionPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MalformedRequest | MethodNotAllowed | NotFound | PayloadTooLarge | QuotaExceeded | UnknownField | UnknownParameter | ValidationFailed | UnsupportedMediaType
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
