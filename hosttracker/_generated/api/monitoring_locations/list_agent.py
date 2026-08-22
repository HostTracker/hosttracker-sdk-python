from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_page import AgentPage
from ...models.internal_error import InternalError
from ...models.invalid_cursor import InvalidCursor
from ...models.invalid_limit import InvalidLimit
from ...models.list_agent_capability_item import ListAgentCapabilityItem
from ...models.list_agent_fields_item import ListAgentFieldsItem
from ...models.method_not_allowed import MethodNotAllowed
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    country: list[str] | Unset = UNSET,
    pool: list[str] | Unset = UNSET,
    capability: list[ListAgentCapabilityItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAgentFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_country: list[str] | Unset = UNSET
    if not isinstance(country, Unset):
        json_country = country

    params["country"] = json_country

    json_pool: list[str] | Unset = UNSET
    if not isinstance(pool, Unset):
        json_pool = pool

    params["pool"] = json_pool

    json_capability: list[str] | Unset = UNSET
    if not isinstance(capability, Unset):
        json_capability = []
        for capability_item_data in capability:
            capability_item: str = capability_item_data
            json_capability.append(capability_item)

    params["capability"] = json_capability

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
        "url": "/agent",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AgentPage
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | MethodNotAllowed
    | None
):
    if response.status_code == 200:
        response_200 = AgentPage.from_dict(response.json())

        return response_200

    if response.status_code == 405:
        response_405 = MethodNotAllowed.from_dict(response.json())

        return response_405

    if response.status_code == 422:

        def _parse_response_422(
            data: object,
        ) -> InvalidCursor | InvalidLimit | UnknownEnumValue | UnknownField | UnknownParameter | ValidationFailed:
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
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_4 = UnknownEnumValue.from_dict(data)

                return response_422_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_5 = UnknownParameter.from_dict(data)

            return response_422_type_5

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
) -> Response[
    AgentPage
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | MethodNotAllowed
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
    pool: list[str] | Unset = UNSET,
    capability: list[ListAgentCapabilityItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAgentFieldsItem] | Unset = UNSET,
) -> Response[
    AgentPage
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | MethodNotAllowed
]:
    """List the monitoring locations checks can run from.

     Returns a page of monitoring locations with each one's country, provider, capabilities and pool
    memberships. Filter by country, pool or capability to find the locations that suit a particular
    check before configuring where a monitor runs from. The fleet is shared infrastructure, so this list
    is the same for every account.

    Args:
        country (list[str] | Unset):
        pool (list[str] | Unset):
        capability (list[ListAgentCapabilityItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListAgentFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentPage | InternalError | InvalidCursor | InvalidLimit | UnknownEnumValue | UnknownField | UnknownParameter | ValidationFailed | MethodNotAllowed]
    """

    kwargs = _get_kwargs(
        country=country,
        pool=pool,
        capability=capability,
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
    pool: list[str] | Unset = UNSET,
    capability: list[ListAgentCapabilityItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAgentFieldsItem] | Unset = UNSET,
) -> (
    AgentPage
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | MethodNotAllowed
    | None
):
    """List the monitoring locations checks can run from.

     Returns a page of monitoring locations with each one's country, provider, capabilities and pool
    memberships. Filter by country, pool or capability to find the locations that suit a particular
    check before configuring where a monitor runs from. The fleet is shared infrastructure, so this list
    is the same for every account.

    Args:
        country (list[str] | Unset):
        pool (list[str] | Unset):
        capability (list[ListAgentCapabilityItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListAgentFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentPage | InternalError | InvalidCursor | InvalidLimit | UnknownEnumValue | UnknownField | UnknownParameter | ValidationFailed | MethodNotAllowed
    """

    return sync_detailed(
        client=client,
        country=country,
        pool=pool,
        capability=capability,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    country: list[str] | Unset = UNSET,
    pool: list[str] | Unset = UNSET,
    capability: list[ListAgentCapabilityItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAgentFieldsItem] | Unset = UNSET,
) -> Response[
    AgentPage
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | MethodNotAllowed
]:
    """List the monitoring locations checks can run from.

     Returns a page of monitoring locations with each one's country, provider, capabilities and pool
    memberships. Filter by country, pool or capability to find the locations that suit a particular
    check before configuring where a monitor runs from. The fleet is shared infrastructure, so this list
    is the same for every account.

    Args:
        country (list[str] | Unset):
        pool (list[str] | Unset):
        capability (list[ListAgentCapabilityItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListAgentFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentPage | InternalError | InvalidCursor | InvalidLimit | UnknownEnumValue | UnknownField | UnknownParameter | ValidationFailed | MethodNotAllowed]
    """

    kwargs = _get_kwargs(
        country=country,
        pool=pool,
        capability=capability,
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
    pool: list[str] | Unset = UNSET,
    capability: list[ListAgentCapabilityItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAgentFieldsItem] | Unset = UNSET,
) -> (
    AgentPage
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | MethodNotAllowed
    | None
):
    """List the monitoring locations checks can run from.

     Returns a page of monitoring locations with each one's country, provider, capabilities and pool
    memberships. Filter by country, pool or capability to find the locations that suit a particular
    check before configuring where a monitor runs from. The fleet is shared infrastructure, so this list
    is the same for every account.

    Args:
        country (list[str] | Unset):
        pool (list[str] | Unset):
        capability (list[ListAgentCapabilityItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListAgentFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentPage | InternalError | InvalidCursor | InvalidLimit | UnknownEnumValue | UnknownField | UnknownParameter | ValidationFailed | MethodNotAllowed
    """

    return (
        await asyncio_detailed(
            client=client,
            country=country,
            pool=pool,
            capability=capability,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
