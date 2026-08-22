from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generated_report_view import GeneratedReportView
from ...models.get_report_fields_item import GetReportFieldsItem
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    fields: list[GetReportFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item: str = fields_item_data
            json_fields.append(fields_item)

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/monitor/report/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GeneratedReportView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
    | None
):
    if response.status_code == 200:
        response_200 = GeneratedReportView.from_dict(response.json())

        return response_200

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

    if response.status_code == 422:

        def _parse_response_422(data: object) -> UnknownField | UnknownParameter:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = UnknownField.from_dict(data)

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
    GeneratedReportView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    fields: list[GetReportFieldsItem] | Unset = UNSET,
) -> Response[
    GeneratedReportView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
]:
    """Get a generated report's metadata.

     Returns what a report covers - its type, format, time range, monitors and expiry - without
    transferring the document itself. Use it to check that a report is still available, or to describe
    one in a list, before spending the bandwidth of a download. A report past its expiry answers not-
    found rather than a state value.

    Args:
        id (str):
        fields (list[GetReportFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GeneratedReportView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownField | UnknownParameter]
    """

    kwargs = _get_kwargs(
        id=id,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    fields: list[GetReportFieldsItem] | Unset = UNSET,
) -> (
    GeneratedReportView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
    | None
):
    """Get a generated report's metadata.

     Returns what a report covers - its type, format, time range, monitors and expiry - without
    transferring the document itself. Use it to check that a report is still available, or to describe
    one in a list, before spending the bandwidth of a download. A report past its expiry answers not-
    found rather than a state value.

    Args:
        id (str):
        fields (list[GetReportFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GeneratedReportView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownField | UnknownParameter
    """

    return sync_detailed(
        id=id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    fields: list[GetReportFieldsItem] | Unset = UNSET,
) -> Response[
    GeneratedReportView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
]:
    """Get a generated report's metadata.

     Returns what a report covers - its type, format, time range, monitors and expiry - without
    transferring the document itself. Use it to check that a report is still available, or to describe
    one in a list, before spending the bandwidth of a download. A report past its expiry answers not-
    found rather than a state value.

    Args:
        id (str):
        fields (list[GetReportFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GeneratedReportView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownField | UnknownParameter]
    """

    kwargs = _get_kwargs(
        id=id,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    fields: list[GetReportFieldsItem] | Unset = UNSET,
) -> (
    GeneratedReportView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
    | None
):
    """Get a generated report's metadata.

     Returns what a report covers - its type, format, time range, monitors and expiry - without
    transferring the document itself. Use it to check that a report is still available, or to describe
    one in a list, before spending the bandwidth of a download. A report past its expiry answers not-
    found rather than a state value.

    Args:
        id (str):
        fields (list[GetReportFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GeneratedReportView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownField | UnknownParameter
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            fields=fields,
        )
    ).parsed
