from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_page import ContactPage
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_cursor import InvalidCursor
from ...models.invalid_limit import InvalidLimit
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.list_contact_expand_item import ListContactExpandItem
from ...models.list_contact_fields_item import ListContactFieldsItem
from ...models.list_contact_sort import ListContactSort
from ...models.list_contact_type_item import ListContactTypeItem
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_expand import UnknownExpand
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: list[str] | Unset = UNSET,
    type_: list[ListContactTypeItem] | Unset = UNSET,
    confirmed: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    sort: ListContactSort | Unset = UNSET,
    expand: list[ListContactExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListContactFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_id: list[str] | Unset = UNSET
    if not isinstance(id, Unset):
        json_id = id

    params["id"] = json_id

    json_type_: list[str] | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = []
        for type_item_data in type_:
            type_item: str = type_item_data
            json_type_.append(type_item)

    params["type"] = json_type_

    params["confirmed"] = confirmed

    params["q"] = q

    params["updatedSince"] = updated_since

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_expand: list[str] | Unset = UNSET
    if not isinstance(expand, Unset):
        json_expand = []
        for expand_item_data in expand:
            expand_item: str = expand_item_data
            json_expand.append(expand_item)

    params["expand"] = json_expand

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
        "url": "/contact",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ContactPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    if response.status_code == 200:
        response_200 = ContactPage.from_dict(response.json())

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
        ) -> (
            InvalidCursor
            | InvalidLimit
            | UnknownEnumValue
            | UnknownExpand
            | UnknownField
            | UnknownParameter
            | ValidationFailed
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = UnknownExpand.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_1 = UnknownField.from_dict(data)

                return response_422_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_2 = ValidationFailed.from_dict(data)

                return response_422_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_3 = InvalidCursor.from_dict(data)

                return response_422_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_4 = InvalidLimit.from_dict(data)

                return response_422_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_5 = UnknownEnumValue.from_dict(data)

                return response_422_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_6 = UnknownParameter.from_dict(data)

            return response_422_type_6

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
    ContactPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
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
    id: list[str] | Unset = UNSET,
    type_: list[ListContactTypeItem] | Unset = UNSET,
    confirmed: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    sort: ListContactSort | Unset = UNSET,
    expand: list[ListContactExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListContactFieldsItem] | Unset = UNSET,
) -> Response[
    ContactPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
]:
    """List the account's contacts, filtered and cursor-paginated.

     Returns a page of contacts - the addresses alerts and reports are delivered to - narrowed by id,
    type, confirmation state or a free-text search over name and address. Use expand to embed each
    contact's subscriptions, its message template or the groups it belongs to, and updatedSince for an
    incremental poll. Fetch one contact by id when only one is wanted. Order it with
    sort=created|name|address, optionally suffixed :asc or :desc (sort=name:desc); without a suffix
    created reads newest-first and the text columns A to Z. There is no separate order parameter.

    Args:
        id (list[str] | Unset):
        type_ (list[ListContactTypeItem] | Unset):
        confirmed (bool | Unset):
        q (str | Unset):
        updated_since (str | Unset):
        sort (ListContactSort | Unset):
        expand (list[ListContactExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListContactFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        id=id,
        type_=type_,
        confirmed=confirmed,
        q=q,
        updated_since=updated_since,
        sort=sort,
        expand=expand,
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
    id: list[str] | Unset = UNSET,
    type_: list[ListContactTypeItem] | Unset = UNSET,
    confirmed: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    sort: ListContactSort | Unset = UNSET,
    expand: list[ListContactExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListContactFieldsItem] | Unset = UNSET,
) -> (
    ContactPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    """List the account's contacts, filtered and cursor-paginated.

     Returns a page of contacts - the addresses alerts and reports are delivered to - narrowed by id,
    type, confirmation state or a free-text search over name and address. Use expand to embed each
    contact's subscriptions, its message template or the groups it belongs to, and updatedSince for an
    incremental poll. Fetch one contact by id when only one is wanted. Order it with
    sort=created|name|address, optionally suffixed :asc or :desc (sort=name:desc); without a suffix
    created reads newest-first and the text columns A to Z. There is no separate order parameter.

    Args:
        id (list[str] | Unset):
        type_ (list[ListContactTypeItem] | Unset):
        confirmed (bool | Unset):
        q (str | Unset):
        updated_since (str | Unset):
        sort (ListContactSort | Unset):
        expand (list[ListContactExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListContactFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | QuotaExceeded
    """

    return sync_detailed(
        client=client,
        id=id,
        type_=type_,
        confirmed=confirmed,
        q=q,
        updated_since=updated_since,
        sort=sort,
        expand=expand,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: list[str] | Unset = UNSET,
    type_: list[ListContactTypeItem] | Unset = UNSET,
    confirmed: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    sort: ListContactSort | Unset = UNSET,
    expand: list[ListContactExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListContactFieldsItem] | Unset = UNSET,
) -> Response[
    ContactPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
]:
    """List the account's contacts, filtered and cursor-paginated.

     Returns a page of contacts - the addresses alerts and reports are delivered to - narrowed by id,
    type, confirmation state or a free-text search over name and address. Use expand to embed each
    contact's subscriptions, its message template or the groups it belongs to, and updatedSince for an
    incremental poll. Fetch one contact by id when only one is wanted. Order it with
    sort=created|name|address, optionally suffixed :asc or :desc (sort=name:desc); without a suffix
    created reads newest-first and the text columns A to Z. There is no separate order parameter.

    Args:
        id (list[str] | Unset):
        type_ (list[ListContactTypeItem] | Unset):
        confirmed (bool | Unset):
        q (str | Unset):
        updated_since (str | Unset):
        sort (ListContactSort | Unset):
        expand (list[ListContactExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListContactFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        id=id,
        type_=type_,
        confirmed=confirmed,
        q=q,
        updated_since=updated_since,
        sort=sort,
        expand=expand,
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: list[str] | Unset = UNSET,
    type_: list[ListContactTypeItem] | Unset = UNSET,
    confirmed: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    sort: ListContactSort | Unset = UNSET,
    expand: list[ListContactExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListContactFieldsItem] | Unset = UNSET,
) -> (
    ContactPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    """List the account's contacts, filtered and cursor-paginated.

     Returns a page of contacts - the addresses alerts and reports are delivered to - narrowed by id,
    type, confirmation state or a free-text search over name and address. Use expand to embed each
    contact's subscriptions, its message template or the groups it belongs to, and updatedSince for an
    incremental poll. Fetch one contact by id when only one is wanted. Order it with
    sort=created|name|address, optionally suffixed :asc or :desc (sort=name:desc); without a suffix
    created reads newest-first and the text columns A to Z. There is no separate order parameter.

    Args:
        id (list[str] | Unset):
        type_ (list[ListContactTypeItem] | Unset):
        confirmed (bool | Unset):
        q (str | Unset):
        updated_since (str | Unset):
        sort (ListContactSort | Unset):
        expand (list[ListContactExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListContactFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | QuotaExceeded
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            type_=type_,
            confirmed=confirmed,
            q=q,
            updated_since=updated_since,
            sort=sort,
            expand=expand,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
