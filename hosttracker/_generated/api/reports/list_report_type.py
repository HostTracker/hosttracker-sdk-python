from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_error import InternalError
from ...models.list_report_type_fields_item import ListReportTypeFieldsItem
from ...models.method_not_allowed import MethodNotAllowed
from ...models.report_type_page import ReportTypePage
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListReportTypeFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

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
        "url": "/report/type",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InternalError | MethodNotAllowed | ReportTypePage | UnknownField | UnknownParameter | None:
    if response.status_code == 200:
        response_200 = ReportTypePage.from_dict(response.json())

        return response_200

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

    if response.status_code == 500:
        response_500 = InternalError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[InternalError | MethodNotAllowed | ReportTypePage | UnknownField | UnknownParameter]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListReportTypeFieldsItem] | Unset = UNSET,
) -> Response[InternalError | MethodNotAllowed | ReportTypePage | UnknownField | UnknownParameter]:
    """List the report types, formats and schedules available.

     Returns the catalogue of report types the account can generate, with the output formats, content
    sections and delivery frequencies each supports. Use it to build a report request form or to
    validate a type before generating - frequencies are published as words, so nothing here has to be
    decoded.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListReportTypeFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalError | MethodNotAllowed | ReportTypePage | UnknownField | UnknownParameter]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListReportTypeFieldsItem] | Unset = UNSET,
) -> InternalError | MethodNotAllowed | ReportTypePage | UnknownField | UnknownParameter | None:
    """List the report types, formats and schedules available.

     Returns the catalogue of report types the account can generate, with the output formats, content
    sections and delivery frequencies each supports. Use it to build a report request form or to
    validate a type before generating - frequencies are published as words, so nothing here has to be
    decoded.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListReportTypeFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalError | MethodNotAllowed | ReportTypePage | UnknownField | UnknownParameter
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListReportTypeFieldsItem] | Unset = UNSET,
) -> Response[InternalError | MethodNotAllowed | ReportTypePage | UnknownField | UnknownParameter]:
    """List the report types, formats and schedules available.

     Returns the catalogue of report types the account can generate, with the output formats, content
    sections and delivery frequencies each supports. Use it to build a report request form or to
    validate a type before generating - frequencies are published as words, so nothing here has to be
    decoded.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListReportTypeFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalError | MethodNotAllowed | ReportTypePage | UnknownField | UnknownParameter]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListReportTypeFieldsItem] | Unset = UNSET,
) -> InternalError | MethodNotAllowed | ReportTypePage | UnknownField | UnknownParameter | None:
    """List the report types, formats and schedules available.

     Returns the catalogue of report types the account can generate, with the output formats, content
    sections and delivery frequencies each supports. Use it to build a report request form or to
    validate a type before generating - frequencies are published as words, so nothing here has to be
    decoded.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListReportTypeFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalError | MethodNotAllowed | ReportTypePage | UnknownField | UnknownParameter
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
