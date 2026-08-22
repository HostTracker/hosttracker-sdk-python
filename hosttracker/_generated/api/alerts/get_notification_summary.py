from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_notification_summary_fields_item import (
    GetNotificationSummaryFieldsItem,
)
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_range import InvalidRange
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.notification_summary_page import NotificationSummaryPage
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    contact: list[str] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[GetNotificationSummaryFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    json_contact: list[str] | Unset = UNSET
    if not isinstance(contact, Unset):
        json_contact = contact

    params["contact"] = json_contact

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
        "url": "/contact/notification/summary",
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
    | InvalidRange
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotificationSummaryPage
    | QuotaExceeded
    | None
):
    if response.status_code == 200:
        response_200 = NotificationSummaryPage.from_dict(response.json())

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

        def _parse_response_422(data: object) -> InvalidRange | UnknownField | UnknownParameter | ValidationFailed:
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
                response_422_type_2 = InvalidRange.from_dict(data)

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
    | InvalidRange
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotificationSummaryPage
    | QuotaExceeded
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
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    contact: list[str] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[GetNotificationSummaryFieldsItem] | Unset = UNSET,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidRange
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotificationSummaryPage
    | QuotaExceeded
]:
    """Get per-contact delivery counts by outcome and day.

     Returns one row per (contact, delivery outcome, UTC day) with the count of notifications delivered
    in that cell, over the requested window (the last month when no window is given). Use it to chart
    delivery volume or spot a silently failing channel without walking the whole log; outcomes use the
    same vocabulary the log's outcome filter takes.

    Args:
        from_ (int | Unset):
        to (int | Unset):
        contact (list[str] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[GetNotificationSummaryFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidRange | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | NotificationSummaryPage | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        contact=contact,
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
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    contact: list[str] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[GetNotificationSummaryFieldsItem] | Unset = UNSET,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidRange
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotificationSummaryPage
    | QuotaExceeded
    | None
):
    """Get per-contact delivery counts by outcome and day.

     Returns one row per (contact, delivery outcome, UTC day) with the count of notifications delivered
    in that cell, over the requested window (the last month when no window is given). Use it to chart
    delivery volume or spot a silently failing channel without walking the whole log; outcomes use the
    same vocabulary the log's outcome filter takes.

    Args:
        from_ (int | Unset):
        to (int | Unset):
        contact (list[str] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[GetNotificationSummaryFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidRange | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | NotificationSummaryPage | QuotaExceeded
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        contact=contact,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    contact: list[str] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[GetNotificationSummaryFieldsItem] | Unset = UNSET,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidRange
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotificationSummaryPage
    | QuotaExceeded
]:
    """Get per-contact delivery counts by outcome and day.

     Returns one row per (contact, delivery outcome, UTC day) with the count of notifications delivered
    in that cell, over the requested window (the last month when no window is given). Use it to chart
    delivery volume or spot a silently failing channel without walking the whole log; outcomes use the
    same vocabulary the log's outcome filter takes.

    Args:
        from_ (int | Unset):
        to (int | Unset):
        contact (list[str] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[GetNotificationSummaryFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidRange | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | NotificationSummaryPage | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        contact=contact,
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    contact: list[str] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[GetNotificationSummaryFieldsItem] | Unset = UNSET,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidRange
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotificationSummaryPage
    | QuotaExceeded
    | None
):
    """Get per-contact delivery counts by outcome and day.

     Returns one row per (contact, delivery outcome, UTC day) with the count of notifications delivered
    in that cell, over the requested window (the last month when no window is given). Use it to chart
    delivery volume or spot a silently failing channel without walking the whole log; outcomes use the
    same vocabulary the log's outcome filter takes.

    Args:
        from_ (int | Unset):
        to (int | Unset):
        contact (list[str] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[GetNotificationSummaryFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidRange | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | NotificationSummaryPage | QuotaExceeded
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            contact=contact,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
