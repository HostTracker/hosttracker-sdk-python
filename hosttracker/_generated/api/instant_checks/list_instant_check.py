from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ic_history_page import IcHistoryPage
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_cursor import InvalidCursor
from ...models.invalid_limit import InvalidLimit
from ...models.invalid_range import InvalidRange
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.list_instant_check_fields_item import ListInstantCheckFieldsItem
from ...models.list_instant_check_type_item import ListInstantCheckTypeItem
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    type_: list[ListInstantCheckTypeItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListInstantCheckFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    json_type_: list[str] | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = []
        for type_item_data in type_:
            type_item: str = type_item_data
            json_type_.append(type_item)

    params["type"] = json_type_

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
        "url": "/check",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    IcHistoryPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    if response.status_code == 200:
        response_200 = IcHistoryPage.from_dict(response.json())

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

        def _parse_response_422(
            data: object,
        ) -> InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownField | UnknownParameter:
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
                response_422_type_1 = InvalidCursor.from_dict(data)

                return response_422_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_2 = InvalidLimit.from_dict(data)

                return response_422_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_3 = InvalidRange.from_dict(data)

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
    IcHistoryPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
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
    type_: list[ListInstantCheckTypeItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListInstantCheckFieldsItem] | Unset = UNSET,
) -> Response[
    IcHistoryPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
]:
    """List the account's past instant checks.

     Returns a page of the instant checks this account has run, newest first, optionally narrowed by time
    window or check type. Use it to find or audit a past ad-hoc check; to read one check's outcome,
    address it directly by the identifiers the start call returned.

    Args:
        from_ (int | Unset):
        to (int | Unset):
        type_ (list[ListInstantCheckTypeItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListInstantCheckFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IcHistoryPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        type_=type_,
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
    type_: list[ListInstantCheckTypeItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListInstantCheckFieldsItem] | Unset = UNSET,
) -> (
    IcHistoryPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    """List the account's past instant checks.

     Returns a page of the instant checks this account has run, newest first, optionally narrowed by time
    window or check type. Use it to find or audit a past ad-hoc check; to read one check's outcome,
    address it directly by the identifiers the start call returned.

    Args:
        from_ (int | Unset):
        to (int | Unset):
        type_ (list[ListInstantCheckTypeItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListInstantCheckFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IcHistoryPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | QuotaExceeded
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        type_=type_,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    type_: list[ListInstantCheckTypeItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListInstantCheckFieldsItem] | Unset = UNSET,
) -> Response[
    IcHistoryPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
]:
    """List the account's past instant checks.

     Returns a page of the instant checks this account has run, newest first, optionally narrowed by time
    window or check type. Use it to find or audit a past ad-hoc check; to read one check's outcome,
    address it directly by the identifiers the start call returned.

    Args:
        from_ (int | Unset):
        to (int | Unset):
        type_ (list[ListInstantCheckTypeItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListInstantCheckFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IcHistoryPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        type_=type_,
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
    type_: list[ListInstantCheckTypeItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListInstantCheckFieldsItem] | Unset = UNSET,
) -> (
    IcHistoryPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    """List the account's past instant checks.

     Returns a page of the instant checks this account has run, newest first, optionally narrowed by time
    window or check type. Use it to find or audit a past ad-hoc check; to read one check's outcome,
    address it directly by the identifiers the start call returned.

    Args:
        from_ (int | Unset):
        to (int | Unset):
        type_ (list[ListInstantCheckTypeItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListInstantCheckFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IcHistoryPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | QuotaExceeded
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            type_=type_,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
