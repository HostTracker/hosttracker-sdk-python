from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_ip_page import AgentIpPage
from ...models.internal_error import InternalError
from ...models.invalid_cursor import InvalidCursor
from ...models.invalid_limit import InvalidLimit
from ...models.list_agent_ip_family_item import ListAgentIpFamilyItem
from ...models.list_agent_ip_fields_item import ListAgentIpFieldsItem
from ...models.method_not_allowed import MethodNotAllowed
from ...models.rate_limited import RateLimited
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    country: list[str] | Unset = UNSET,
    family: list[ListAgentIpFamilyItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAgentIpFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_country: list[str] | Unset = UNSET
    if not isinstance(country, Unset):
        json_country = country

    params["country"] = json_country

    json_family: list[str] | Unset = UNSET
    if not isinstance(family, Unset):
        json_family = []
        for family_item_data in family:
            family_item: str = family_item_data
            json_family.append(family_item)

    params["family"] = json_family

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
        "url": "/agent/ip",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AgentIpPage
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | MethodNotAllowed
    | RateLimited
    | None
):
    if response.status_code == 200:
        response_200 = AgentIpPage.from_dict(response.json())

        return response_200

    if response.status_code == 405:
        response_405 = MethodNotAllowed.from_dict(response.json())

        return response_405

    if response.status_code == 422:

        def _parse_response_422(
            data: object,
        ) -> InvalidCursor | InvalidLimit | UnknownField | UnknownParameter | ValidationFailed:
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
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_2 = InvalidCursor.from_dict(data)

                return response_422_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_3 = InvalidLimit.from_dict(data)

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
        response_429 = RateLimited.from_dict(response.json())

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
    AgentIpPage
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | MethodNotAllowed
    | RateLimited
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
    country: list[str] | Unset = UNSET,
    family: list[ListAgentIpFamilyItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAgentIpFieldsItem] | Unset = UNSET,
) -> Response[
    AgentIpPage
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | MethodNotAllowed
    | RateLimited
]:
    """List the IP addresses monitoring checks originate from.

     Returns the addresses checks are sent from, for allow-listing in a firewall or in a monitored
    service's access rules. It needs no token - an allow-listing script frequently runs before any
    credential exists on the machine it is provisioning - and a token is honoured if you send one: the
    answer is identical, and the call is metered on your account's own reference bucket instead of the
    one shared by everyone calling from your address. Every response carries the rate-limit headers.

    Args:
        country (list[str] | Unset):
        family (list[ListAgentIpFamilyItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListAgentIpFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentIpPage | InternalError | InvalidCursor | InvalidLimit | UnknownField | UnknownParameter | ValidationFailed | MethodNotAllowed | RateLimited]
    """

    kwargs = _get_kwargs(
        country=country,
        family=family,
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
    country: list[str] | Unset = UNSET,
    family: list[ListAgentIpFamilyItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAgentIpFieldsItem] | Unset = UNSET,
) -> (
    AgentIpPage
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | MethodNotAllowed
    | RateLimited
    | None
):
    """List the IP addresses monitoring checks originate from.

     Returns the addresses checks are sent from, for allow-listing in a firewall or in a monitored
    service's access rules. It needs no token - an allow-listing script frequently runs before any
    credential exists on the machine it is provisioning - and a token is honoured if you send one: the
    answer is identical, and the call is metered on your account's own reference bucket instead of the
    one shared by everyone calling from your address. Every response carries the rate-limit headers.

    Args:
        country (list[str] | Unset):
        family (list[ListAgentIpFamilyItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListAgentIpFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentIpPage | InternalError | InvalidCursor | InvalidLimit | UnknownField | UnknownParameter | ValidationFailed | MethodNotAllowed | RateLimited
    """

    return sync_detailed(
        client=client,
        country=country,
        family=family,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    country: list[str] | Unset = UNSET,
    family: list[ListAgentIpFamilyItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAgentIpFieldsItem] | Unset = UNSET,
) -> Response[
    AgentIpPage
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | MethodNotAllowed
    | RateLimited
]:
    """List the IP addresses monitoring checks originate from.

     Returns the addresses checks are sent from, for allow-listing in a firewall or in a monitored
    service's access rules. It needs no token - an allow-listing script frequently runs before any
    credential exists on the machine it is provisioning - and a token is honoured if you send one: the
    answer is identical, and the call is metered on your account's own reference bucket instead of the
    one shared by everyone calling from your address. Every response carries the rate-limit headers.

    Args:
        country (list[str] | Unset):
        family (list[ListAgentIpFamilyItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListAgentIpFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentIpPage | InternalError | InvalidCursor | InvalidLimit | UnknownField | UnknownParameter | ValidationFailed | MethodNotAllowed | RateLimited]
    """

    kwargs = _get_kwargs(
        country=country,
        family=family,
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    country: list[str] | Unset = UNSET,
    family: list[ListAgentIpFamilyItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAgentIpFieldsItem] | Unset = UNSET,
) -> (
    AgentIpPage
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | MethodNotAllowed
    | RateLimited
    | None
):
    """List the IP addresses monitoring checks originate from.

     Returns the addresses checks are sent from, for allow-listing in a firewall or in a monitored
    service's access rules. It needs no token - an allow-listing script frequently runs before any
    credential exists on the machine it is provisioning - and a token is honoured if you send one: the
    answer is identical, and the call is metered on your account's own reference bucket instead of the
    one shared by everyone calling from your address. Every response carries the rate-limit headers.

    Args:
        country (list[str] | Unset):
        family (list[ListAgentIpFamilyItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListAgentIpFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentIpPage | InternalError | InvalidCursor | InvalidLimit | UnknownField | UnknownParameter | ValidationFailed | MethodNotAllowed | RateLimited
    """

    return (
        await asyncio_detailed(
            client=client,
            country=country,
            family=family,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
