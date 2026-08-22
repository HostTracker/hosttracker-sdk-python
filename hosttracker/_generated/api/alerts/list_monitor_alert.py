from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.list_monitor_alert_fields_item import ListMonitorAlertFieldsItem
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.monitor_alert_subscription_page import MonitorAlertSubscriptionPage
from ...models.not_found import NotFound
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    monitor_id: UUID,
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorAlertFieldsItem] | Unset = UNSET,
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
        "url": "/monitor/{monitor_id}/alert".format(
            monitor_id=quote(str(monitor_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | MonitorAlertSubscriptionPage
    | NotFound
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
    | None
):
    if response.status_code == 200:
        response_200 = MonitorAlertSubscriptionPage.from_dict(response.json())

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
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | MonitorAlertSubscriptionPage
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
    monitor_id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorAlertFieldsItem] | Unset = UNSET,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | MonitorAlertSubscriptionPage
    | NotFound
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
]:
    """List the contacts this monitor alerts, with each contact's alert-type set.

     Returns who is alerted when this monitor changes state - one row per contact, each carrying the set
    of alert types (up/down/repeatedlyDown) that contact receives. Set the subscription with PUT
    /monitor/{monitorId}/alert/{contactId}. The contact's address is included only when the token also
    carries a contact read scope - a monitor-scoped token sees which contact it is, not how to reach it.

    Args:
        monitor_id (UUID):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMonitorAlertFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | MonitorAlertSubscriptionPage | NotFound | QuotaExceeded | UnknownField | UnknownParameter]
    """

    kwargs = _get_kwargs(
        monitor_id=monitor_id,
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    monitor_id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorAlertFieldsItem] | Unset = UNSET,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | MonitorAlertSubscriptionPage
    | NotFound
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
    | None
):
    """List the contacts this monitor alerts, with each contact's alert-type set.

     Returns who is alerted when this monitor changes state - one row per contact, each carrying the set
    of alert types (up/down/repeatedlyDown) that contact receives. Set the subscription with PUT
    /monitor/{monitorId}/alert/{contactId}. The contact's address is included only when the token also
    carries a contact read scope - a monitor-scoped token sees which contact it is, not how to reach it.

    Args:
        monitor_id (UUID):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMonitorAlertFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | MonitorAlertSubscriptionPage | NotFound | QuotaExceeded | UnknownField | UnknownParameter
    """

    return sync_detailed(
        monitor_id=monitor_id,
        client=client,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    monitor_id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorAlertFieldsItem] | Unset = UNSET,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | MonitorAlertSubscriptionPage
    | NotFound
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
]:
    """List the contacts this monitor alerts, with each contact's alert-type set.

     Returns who is alerted when this monitor changes state - one row per contact, each carrying the set
    of alert types (up/down/repeatedlyDown) that contact receives. Set the subscription with PUT
    /monitor/{monitorId}/alert/{contactId}. The contact's address is included only when the token also
    carries a contact read scope - a monitor-scoped token sees which contact it is, not how to reach it.

    Args:
        monitor_id (UUID):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMonitorAlertFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | MonitorAlertSubscriptionPage | NotFound | QuotaExceeded | UnknownField | UnknownParameter]
    """

    kwargs = _get_kwargs(
        monitor_id=monitor_id,
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    monitor_id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorAlertFieldsItem] | Unset = UNSET,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | MonitorAlertSubscriptionPage
    | NotFound
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
    | None
):
    """List the contacts this monitor alerts, with each contact's alert-type set.

     Returns who is alerted when this monitor changes state - one row per contact, each carrying the set
    of alert types (up/down/repeatedlyDown) that contact receives. Set the subscription with PUT
    /monitor/{monitorId}/alert/{contactId}. The contact's address is included only when the token also
    carries a contact read scope - a monitor-scoped token sees which contact it is, not how to reach it.

    Args:
        monitor_id (UUID):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMonitorAlertFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | MonitorAlertSubscriptionPage | NotFound | QuotaExceeded | UnknownField | UnknownParameter
    """

    return (
        await asyncio_detailed(
            monitor_id=monitor_id,
            client=client,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
