from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_grouped_alert_subscription_page import ContactGroupedAlertSubscriptionPage
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.list_alert_by_contact_contact_type_item import (
    ListAlertByContactContactTypeItem,
)
from ...models.list_alert_by_contact_fields_item import (
    ListAlertByContactFieldsItem,
)
from ...models.list_alert_by_contact_monitor_type_item import (
    ListAlertByContactMonitorTypeItem,
)
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    monitor_id: list[str] | Unset = UNSET,
    monitor_type: list[ListAlertByContactMonitorTypeItem] | Unset = UNSET,
    monitor_tag: list[str] | Unset = UNSET,
    monitor_url: list[str] | Unset = UNSET,
    monitor_like: bool | Unset = UNSET,
    monitor_q: str | Unset = UNSET,
    contact_id: list[str] | Unset = UNSET,
    contact_type: list[ListAlertByContactContactTypeItem] | Unset = UNSET,
    contact_confirmed: bool | Unset = UNSET,
    contact_q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAlertByContactFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_monitor_id: list[str] | Unset = UNSET
    if not isinstance(monitor_id, Unset):
        json_monitor_id = monitor_id

    params["monitor.id"] = json_monitor_id

    json_monitor_type: list[str] | Unset = UNSET
    if not isinstance(monitor_type, Unset):
        json_monitor_type = []
        for monitor_type_item_data in monitor_type:
            monitor_type_item: str = monitor_type_item_data
            json_monitor_type.append(monitor_type_item)

    params["monitor.type"] = json_monitor_type

    json_monitor_tag: list[str] | Unset = UNSET
    if not isinstance(monitor_tag, Unset):
        json_monitor_tag = monitor_tag

    params["monitor.tag"] = json_monitor_tag

    json_monitor_url: list[str] | Unset = UNSET
    if not isinstance(monitor_url, Unset):
        json_monitor_url = monitor_url

    params["monitor.url"] = json_monitor_url

    params["monitor.like"] = monitor_like

    params["monitor.q"] = monitor_q

    json_contact_id: list[str] | Unset = UNSET
    if not isinstance(contact_id, Unset):
        json_contact_id = contact_id

    params["contact.id"] = json_contact_id

    json_contact_type: list[str] | Unset = UNSET
    if not isinstance(contact_type, Unset):
        json_contact_type = []
        for contact_type_item_data in contact_type:
            contact_type_item: str = contact_type_item_data
            json_contact_type.append(contact_type_item)

    params["contact.type"] = json_contact_type

    params["contact.confirmed"] = contact_confirmed

    params["contact.q"] = contact_q

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
        "url": "/alert/by-contact",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ContactGroupedAlertSubscriptionPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | None
):
    if response.status_code == 200:
        response_200 = ContactGroupedAlertSubscriptionPage.from_dict(response.json())

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

    if response.status_code == 405:
        response_405 = MethodNotAllowed.from_dict(response.json())

        return response_405

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
    ContactGroupedAlertSubscriptionPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
    | ValidationFailed
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
    monitor_id: list[str] | Unset = UNSET,
    monitor_type: list[ListAlertByContactMonitorTypeItem] | Unset = UNSET,
    monitor_tag: list[str] | Unset = UNSET,
    monitor_url: list[str] | Unset = UNSET,
    monitor_like: bool | Unset = UNSET,
    monitor_q: str | Unset = UNSET,
    contact_id: list[str] | Unset = UNSET,
    contact_type: list[ListAlertByContactContactTypeItem] | Unset = UNSET,
    contact_confirmed: bool | Unset = UNSET,
    contact_q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAlertByContactFieldsItem] | Unset = UNSET,
) -> Response[
    ContactGroupedAlertSubscriptionPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
    | ValidationFailed
]:
    """List every alert subscription on the account, grouped by contact.

     The same alert wiring as listAlertSubscription, grouped one element per contact with its subscribed
    monitors nested underneath. Takes the same filters as the flat list; the mirror of
    listAlertByMonitor.

    Args:
        monitor_id (list[str] | Unset):
        monitor_type (list[ListAlertByContactMonitorTypeItem] | Unset):
        monitor_tag (list[str] | Unset):
        monitor_url (list[str] | Unset):
        monitor_like (bool | Unset):
        monitor_q (str | Unset):
        contact_id (list[str] | Unset):
        contact_type (list[ListAlertByContactContactTypeItem] | Unset):
        contact_confirmed (bool | Unset):
        contact_q (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListAlertByContactFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactGroupedAlertSubscriptionPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | QuotaExceeded | UnknownField | UnknownParameter | ValidationFailed]
    """

    kwargs = _get_kwargs(
        monitor_id=monitor_id,
        monitor_type=monitor_type,
        monitor_tag=monitor_tag,
        monitor_url=monitor_url,
        monitor_like=monitor_like,
        monitor_q=monitor_q,
        contact_id=contact_id,
        contact_type=contact_type,
        contact_confirmed=contact_confirmed,
        contact_q=contact_q,
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
    monitor_id: list[str] | Unset = UNSET,
    monitor_type: list[ListAlertByContactMonitorTypeItem] | Unset = UNSET,
    monitor_tag: list[str] | Unset = UNSET,
    monitor_url: list[str] | Unset = UNSET,
    monitor_like: bool | Unset = UNSET,
    monitor_q: str | Unset = UNSET,
    contact_id: list[str] | Unset = UNSET,
    contact_type: list[ListAlertByContactContactTypeItem] | Unset = UNSET,
    contact_confirmed: bool | Unset = UNSET,
    contact_q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAlertByContactFieldsItem] | Unset = UNSET,
) -> (
    ContactGroupedAlertSubscriptionPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | None
):
    """List every alert subscription on the account, grouped by contact.

     The same alert wiring as listAlertSubscription, grouped one element per contact with its subscribed
    monitors nested underneath. Takes the same filters as the flat list; the mirror of
    listAlertByMonitor.

    Args:
        monitor_id (list[str] | Unset):
        monitor_type (list[ListAlertByContactMonitorTypeItem] | Unset):
        monitor_tag (list[str] | Unset):
        monitor_url (list[str] | Unset):
        monitor_like (bool | Unset):
        monitor_q (str | Unset):
        contact_id (list[str] | Unset):
        contact_type (list[ListAlertByContactContactTypeItem] | Unset):
        contact_confirmed (bool | Unset):
        contact_q (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListAlertByContactFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactGroupedAlertSubscriptionPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | QuotaExceeded | UnknownField | UnknownParameter | ValidationFailed
    """

    return sync_detailed(
        client=client,
        monitor_id=monitor_id,
        monitor_type=monitor_type,
        monitor_tag=monitor_tag,
        monitor_url=monitor_url,
        monitor_like=monitor_like,
        monitor_q=monitor_q,
        contact_id=contact_id,
        contact_type=contact_type,
        contact_confirmed=contact_confirmed,
        contact_q=contact_q,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    monitor_id: list[str] | Unset = UNSET,
    monitor_type: list[ListAlertByContactMonitorTypeItem] | Unset = UNSET,
    monitor_tag: list[str] | Unset = UNSET,
    monitor_url: list[str] | Unset = UNSET,
    monitor_like: bool | Unset = UNSET,
    monitor_q: str | Unset = UNSET,
    contact_id: list[str] | Unset = UNSET,
    contact_type: list[ListAlertByContactContactTypeItem] | Unset = UNSET,
    contact_confirmed: bool | Unset = UNSET,
    contact_q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAlertByContactFieldsItem] | Unset = UNSET,
) -> Response[
    ContactGroupedAlertSubscriptionPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
    | ValidationFailed
]:
    """List every alert subscription on the account, grouped by contact.

     The same alert wiring as listAlertSubscription, grouped one element per contact with its subscribed
    monitors nested underneath. Takes the same filters as the flat list; the mirror of
    listAlertByMonitor.

    Args:
        monitor_id (list[str] | Unset):
        monitor_type (list[ListAlertByContactMonitorTypeItem] | Unset):
        monitor_tag (list[str] | Unset):
        monitor_url (list[str] | Unset):
        monitor_like (bool | Unset):
        monitor_q (str | Unset):
        contact_id (list[str] | Unset):
        contact_type (list[ListAlertByContactContactTypeItem] | Unset):
        contact_confirmed (bool | Unset):
        contact_q (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListAlertByContactFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactGroupedAlertSubscriptionPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | QuotaExceeded | UnknownField | UnknownParameter | ValidationFailed]
    """

    kwargs = _get_kwargs(
        monitor_id=monitor_id,
        monitor_type=monitor_type,
        monitor_tag=monitor_tag,
        monitor_url=monitor_url,
        monitor_like=monitor_like,
        monitor_q=monitor_q,
        contact_id=contact_id,
        contact_type=contact_type,
        contact_confirmed=contact_confirmed,
        contact_q=contact_q,
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    monitor_id: list[str] | Unset = UNSET,
    monitor_type: list[ListAlertByContactMonitorTypeItem] | Unset = UNSET,
    monitor_tag: list[str] | Unset = UNSET,
    monitor_url: list[str] | Unset = UNSET,
    monitor_like: bool | Unset = UNSET,
    monitor_q: str | Unset = UNSET,
    contact_id: list[str] | Unset = UNSET,
    contact_type: list[ListAlertByContactContactTypeItem] | Unset = UNSET,
    contact_confirmed: bool | Unset = UNSET,
    contact_q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListAlertByContactFieldsItem] | Unset = UNSET,
) -> (
    ContactGroupedAlertSubscriptionPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | None
):
    """List every alert subscription on the account, grouped by contact.

     The same alert wiring as listAlertSubscription, grouped one element per contact with its subscribed
    monitors nested underneath. Takes the same filters as the flat list; the mirror of
    listAlertByMonitor.

    Args:
        monitor_id (list[str] | Unset):
        monitor_type (list[ListAlertByContactMonitorTypeItem] | Unset):
        monitor_tag (list[str] | Unset):
        monitor_url (list[str] | Unset):
        monitor_like (bool | Unset):
        monitor_q (str | Unset):
        contact_id (list[str] | Unset):
        contact_type (list[ListAlertByContactContactTypeItem] | Unset):
        contact_confirmed (bool | Unset):
        contact_q (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListAlertByContactFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactGroupedAlertSubscriptionPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | QuotaExceeded | UnknownField | UnknownParameter | ValidationFailed
    """

    return (
        await asyncio_detailed(
            client=client,
            monitor_id=monitor_id,
            monitor_type=monitor_type,
            monitor_tag=monitor_tag,
            monitor_url=monitor_url,
            monitor_like=monitor_like,
            monitor_q=monitor_q,
            contact_id=contact_id,
            contact_type=contact_type,
            contact_confirmed=contact_confirmed,
            contact_q=contact_q,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
