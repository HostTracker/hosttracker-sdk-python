from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_monitor_type_fields_item import GetMonitorTypeFieldsItem
from ...models.internal_error import InternalError
from ...models.method_not_allowed import MethodNotAllowed
from ...models.monitor_type_schema_view import MonitorTypeSchemaView
from ...models.not_found import NotFound
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    type_: str,
    *,
    fields: list[GetMonitorTypeFieldsItem] | Unset = UNSET,
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
        "url": "/monitor/type/{type_}".format(
            type_=quote(str(type_), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InternalError | MethodNotAllowed | MonitorTypeSchemaView | NotFound | UnknownField | UnknownParameter | None:
    if response.status_code == 200:
        response_200 = MonitorTypeSchemaView.from_dict(response.json())

        return response_200

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

    if response.status_code == 500:
        response_500 = InternalError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[InternalError | MethodNotAllowed | MonitorTypeSchemaView | NotFound | UnknownField | UnknownParameter]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: str,
    *,
    client: AuthenticatedClient,
    fields: list[GetMonitorTypeFieldsItem] | Unset = UNSET,
) -> Response[InternalError | MethodNotAllowed | MonitorTypeSchemaView | NotFound | UnknownField | UnknownParameter]:
    """Get one monitor type's catalogue row and its full settings schema.

     Returns the complete JSON Schema describing one type's settings object, together with the catalogue
    row a picker already has, and - for the types that can also run attached to a parent monitor - the
    shape they take there. Use it to validate or generate a settings body for one type; the composite
    schema endpoint answers the same question for all types at once.

    No token is needed. Send one anyway and the catalogue row gains `accountLimits` - this type's
    availability and interval floor under your own package - and the call is metered on your account's
    own reference bucket rather than the one shared by your source address.

    Args:
        type_ (str):
        fields (list[GetMonitorTypeFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalError | MethodNotAllowed | MonitorTypeSchemaView | NotFound | UnknownField | UnknownParameter]
    """

    kwargs = _get_kwargs(
        type_=type_,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_: str,
    *,
    client: AuthenticatedClient,
    fields: list[GetMonitorTypeFieldsItem] | Unset = UNSET,
) -> InternalError | MethodNotAllowed | MonitorTypeSchemaView | NotFound | UnknownField | UnknownParameter | None:
    """Get one monitor type's catalogue row and its full settings schema.

     Returns the complete JSON Schema describing one type's settings object, together with the catalogue
    row a picker already has, and - for the types that can also run attached to a parent monitor - the
    shape they take there. Use it to validate or generate a settings body for one type; the composite
    schema endpoint answers the same question for all types at once.

    No token is needed. Send one anyway and the catalogue row gains `accountLimits` - this type's
    availability and interval floor under your own package - and the call is metered on your account's
    own reference bucket rather than the one shared by your source address.

    Args:
        type_ (str):
        fields (list[GetMonitorTypeFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalError | MethodNotAllowed | MonitorTypeSchemaView | NotFound | UnknownField | UnknownParameter
    """

    return sync_detailed(
        type_=type_,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    type_: str,
    *,
    client: AuthenticatedClient,
    fields: list[GetMonitorTypeFieldsItem] | Unset = UNSET,
) -> Response[InternalError | MethodNotAllowed | MonitorTypeSchemaView | NotFound | UnknownField | UnknownParameter]:
    """Get one monitor type's catalogue row and its full settings schema.

     Returns the complete JSON Schema describing one type's settings object, together with the catalogue
    row a picker already has, and - for the types that can also run attached to a parent monitor - the
    shape they take there. Use it to validate or generate a settings body for one type; the composite
    schema endpoint answers the same question for all types at once.

    No token is needed. Send one anyway and the catalogue row gains `accountLimits` - this type's
    availability and interval floor under your own package - and the call is metered on your account's
    own reference bucket rather than the one shared by your source address.

    Args:
        type_ (str):
        fields (list[GetMonitorTypeFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalError | MethodNotAllowed | MonitorTypeSchemaView | NotFound | UnknownField | UnknownParameter]
    """

    kwargs = _get_kwargs(
        type_=type_,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: str,
    *,
    client: AuthenticatedClient,
    fields: list[GetMonitorTypeFieldsItem] | Unset = UNSET,
) -> InternalError | MethodNotAllowed | MonitorTypeSchemaView | NotFound | UnknownField | UnknownParameter | None:
    """Get one monitor type's catalogue row and its full settings schema.

     Returns the complete JSON Schema describing one type's settings object, together with the catalogue
    row a picker already has, and - for the types that can also run attached to a parent monitor - the
    shape they take there. Use it to validate or generate a settings body for one type; the composite
    schema endpoint answers the same question for all types at once.

    No token is needed. Send one anyway and the catalogue row gains `accountLimits` - this type's
    availability and interval floor under your own package - and the call is metered on your account's
    own reference bucket rather than the one shared by your source address.

    Args:
        type_ (str):
        fields (list[GetMonitorTypeFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalError | MethodNotAllowed | MonitorTypeSchemaView | NotFound | UnknownField | UnknownParameter
    """

    return (
        await asyncio_detailed(
            type_=type_,
            client=client,
            fields=fields,
        )
    ).parsed
