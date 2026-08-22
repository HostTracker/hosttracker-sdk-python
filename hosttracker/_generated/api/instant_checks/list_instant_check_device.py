from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ic_device_page import IcDevicePage
from ...models.internal_error import InternalError
from ...models.list_instant_check_device_fields_item import (
    ListInstantCheckDeviceFieldsItem,
)
from ...models.method_not_allowed import MethodNotAllowed
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListInstantCheckDeviceFieldsItem] | Unset = UNSET,
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
        "url": "/check/device",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IcDevicePage | InternalError | MethodNotAllowed | UnknownField | UnknownParameter | None:
    if response.status_code == 200:
        response_200 = IcDevicePage.from_dict(response.json())

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
) -> Response[IcDevicePage | InternalError | MethodNotAllowed | UnknownField | UnknownParameter]:
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
    fields: list[ListInstantCheckDeviceFieldsItem] | Unset = UNSET,
) -> Response[IcDevicePage | InternalError | MethodNotAllowed | UnknownField | UnknownParameter]:
    """List the device profiles a page-loading check can emulate.

     Returns the device profiles a waterfall check can be run as - the browser is emulated as that
    device, which changes the viewport, the pixel density and the user agent the target sees. A row's
    device is the value the deviceEmulation setting takes, on an instant check and on a monitor alike.
    Rows arrive in the order a picker should offer them. The same names ride the waterfall row of the
    instant-check type catalogue; read this endpoint when the profiles themselves are what you are
    after.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListInstantCheckDeviceFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IcDevicePage | InternalError | MethodNotAllowed | UnknownField | UnknownParameter]
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
    fields: list[ListInstantCheckDeviceFieldsItem] | Unset = UNSET,
) -> IcDevicePage | InternalError | MethodNotAllowed | UnknownField | UnknownParameter | None:
    """List the device profiles a page-loading check can emulate.

     Returns the device profiles a waterfall check can be run as - the browser is emulated as that
    device, which changes the viewport, the pixel density and the user agent the target sees. A row's
    device is the value the deviceEmulation setting takes, on an instant check and on a monitor alike.
    Rows arrive in the order a picker should offer them. The same names ride the waterfall row of the
    instant-check type catalogue; read this endpoint when the profiles themselves are what you are
    after.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListInstantCheckDeviceFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IcDevicePage | InternalError | MethodNotAllowed | UnknownField | UnknownParameter
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
    fields: list[ListInstantCheckDeviceFieldsItem] | Unset = UNSET,
) -> Response[IcDevicePage | InternalError | MethodNotAllowed | UnknownField | UnknownParameter]:
    """List the device profiles a page-loading check can emulate.

     Returns the device profiles a waterfall check can be run as - the browser is emulated as that
    device, which changes the viewport, the pixel density and the user agent the target sees. A row's
    device is the value the deviceEmulation setting takes, on an instant check and on a monitor alike.
    Rows arrive in the order a picker should offer them. The same names ride the waterfall row of the
    instant-check type catalogue; read this endpoint when the profiles themselves are what you are
    after.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListInstantCheckDeviceFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IcDevicePage | InternalError | MethodNotAllowed | UnknownField | UnknownParameter]
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
    fields: list[ListInstantCheckDeviceFieldsItem] | Unset = UNSET,
) -> IcDevicePage | InternalError | MethodNotAllowed | UnknownField | UnknownParameter | None:
    """List the device profiles a page-loading check can emulate.

     Returns the device profiles a waterfall check can be run as - the browser is emulated as that
    device, which changes the viewport, the pixel density and the user agent the target sees. A row's
    device is the value the deviceEmulation setting takes, on an instant check and on a monitor alike.
    Rows arrive in the order a picker should offer them. The same names ride the waterfall row of the
    instant-check type catalogue; read this endpoint when the profiles themselves are what you are
    after.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListInstantCheckDeviceFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IcDevicePage | InternalError | MethodNotAllowed | UnknownField | UnknownParameter
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
