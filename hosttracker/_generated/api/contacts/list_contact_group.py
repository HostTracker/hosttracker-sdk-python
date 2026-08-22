from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_group_page import ContactGroupPage
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_cursor import InvalidCursor
from ...models.invalid_limit import InvalidLimit
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.list_contact_group_fields_item import ListContactGroupFieldsItem
from ...models.list_contact_group_sort import ListContactGroupSort
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    sort: ListContactGroupSort | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListContactGroupFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

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
        "url": "/contact/group",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ContactGroupPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    if response.status_code == 200:
        response_200 = ContactGroupPage.from_dict(response.json())

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
        ) -> InvalidCursor | InvalidLimit | UnknownEnumValue | UnknownField | UnknownParameter:
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
                response_422_type_3 = UnknownEnumValue.from_dict(data)

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
    ContactGroupPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
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
    sort: ListContactGroupSort | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListContactGroupFieldsItem] | Unset = UNSET,
) -> Response[
    ContactGroupPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
]:
    """List the account's contact groups.

     Returns every contact group with its full membership snapshot - each member as the contact's
    identifying projection plus its event selection. A group is a PASSIVE preset: applying one means
    reading it and writing the subscriptions you want through the subscription endpoints; membership by
    itself subscribes nothing. Sortable: sort=name|created, optionally suffixed :asc or :desc (default
    name ascending, the list's shipped order).

    Args:
        sort (ListContactGroupSort | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListContactGroupFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactGroupPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownEnumValue | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        sort=sort,
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
    sort: ListContactGroupSort | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListContactGroupFieldsItem] | Unset = UNSET,
) -> (
    ContactGroupPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    """List the account's contact groups.

     Returns every contact group with its full membership snapshot - each member as the contact's
    identifying projection plus its event selection. A group is a PASSIVE preset: applying one means
    reading it and writing the subscriptions you want through the subscription endpoints; membership by
    itself subscribes nothing. Sortable: sort=name|created, optionally suffixed :asc or :desc (default
    name ascending, the list's shipped order).

    Args:
        sort (ListContactGroupSort | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListContactGroupFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactGroupPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownEnumValue | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | QuotaExceeded
    """

    return sync_detailed(
        client=client,
        sort=sort,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    sort: ListContactGroupSort | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListContactGroupFieldsItem] | Unset = UNSET,
) -> Response[
    ContactGroupPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
]:
    """List the account's contact groups.

     Returns every contact group with its full membership snapshot - each member as the contact's
    identifying projection plus its event selection. A group is a PASSIVE preset: applying one means
    reading it and writing the subscriptions you want through the subscription endpoints; membership by
    itself subscribes nothing. Sortable: sort=name|created, optionally suffixed :asc or :desc (default
    name ascending, the list's shipped order).

    Args:
        sort (ListContactGroupSort | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListContactGroupFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactGroupPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownEnumValue | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        sort=sort,
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    sort: ListContactGroupSort | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListContactGroupFieldsItem] | Unset = UNSET,
) -> (
    ContactGroupPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    """List the account's contact groups.

     Returns every contact group with its full membership snapshot - each member as the contact's
    identifying projection plus its event selection. A group is a PASSIVE preset: applying one means
    reading it and writing the subscriptions you want through the subscription endpoints; membership by
    itself subscribes nothing. Sortable: sort=name|created, optionally suffixed :asc or :desc (default
    name ascending, the list's shipped order).

    Args:
        sort (ListContactGroupSort | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListContactGroupFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactGroupPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownEnumValue | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | QuotaExceeded
    """

    return (
        await asyncio_detailed(
            client=client,
            sort=sort,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
