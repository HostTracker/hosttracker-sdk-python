from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_log_page import AlertLogPage
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_cursor import InvalidCursor
from ...models.invalid_limit import InvalidLimit
from ...models.invalid_range import InvalidRange
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.list_contact_notification_expand_item import (
    ListContactNotificationExpandItem,
)
from ...models.list_contact_notification_fields_item import (
    ListContactNotificationFieldsItem,
)
from ...models.list_contact_notification_outcome_item import (
    ListContactNotificationOutcomeItem,
)
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    outcome: list[ListContactNotificationOutcomeItem] | Unset = UNSET,
    expand: list[ListContactNotificationExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListContactNotificationFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    json_outcome: list[str] | Unset = UNSET
    if not isinstance(outcome, Unset):
        json_outcome = []
        for outcome_item_data in outcome:
            outcome_item: str = outcome_item_data
            json_outcome.append(outcome_item)

    params["outcome"] = json_outcome

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
        "url": "/contact/{id}/notification".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AlertLogPage
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
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | None
):
    if response.status_code == 200:
        response_200 = AlertLogPage.from_dict(response.json())

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

        def _parse_response_422(
            data: object,
        ) -> (
            InvalidCursor
            | InvalidLimit
            | InvalidRange
            | UnknownEnumValue
            | UnknownField
            | UnknownParameter
            | ValidationFailed
        ):
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
                response_422_type_4 = InvalidRange.from_dict(data)

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
    AlertLogPage
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
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    outcome: list[ListContactNotificationOutcomeItem] | Unset = UNSET,
    expand: list[ListContactNotificationExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListContactNotificationFieldsItem] | Unset = UNSET,
) -> Response[
    AlertLogPage
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
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
]:
    """List one contact's delivered notifications, newest first.

     Returns a page of the notifications delivered to the contact in the path, with the same window and
    outcome filters, the same row shape and the same expansions as the account-wide list. Use it when
    the question is about one address; the collection read at /contact/notification serves cross-contact
    audits.

    Args:
        id (UUID):
        from_ (int | Unset):
        to (int | Unset):
        outcome (list[ListContactNotificationOutcomeItem] | Unset):
        expand (list[ListContactNotificationExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListContactNotificationFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertLogPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        id=id,
        from_=from_,
        to=to,
        outcome=outcome,
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
    id: UUID,
    *,
    client: AuthenticatedClient,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    outcome: list[ListContactNotificationOutcomeItem] | Unset = UNSET,
    expand: list[ListContactNotificationExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListContactNotificationFieldsItem] | Unset = UNSET,
) -> (
    AlertLogPage
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
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | None
):
    """List one contact's delivered notifications, newest first.

     Returns a page of the notifications delivered to the contact in the path, with the same window and
    outcome filters, the same row shape and the same expansions as the account-wide list. Use it when
    the question is about one address; the collection read at /contact/notification serves cross-contact
    audits.

    Args:
        id (UUID):
        from_ (int | Unset):
        to (int | Unset):
        outcome (list[ListContactNotificationOutcomeItem] | Unset):
        expand (list[ListContactNotificationExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListContactNotificationFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertLogPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded
    """

    return sync_detailed(
        id=id,
        client=client,
        from_=from_,
        to=to,
        outcome=outcome,
        expand=expand,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    outcome: list[ListContactNotificationOutcomeItem] | Unset = UNSET,
    expand: list[ListContactNotificationExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListContactNotificationFieldsItem] | Unset = UNSET,
) -> Response[
    AlertLogPage
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
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
]:
    """List one contact's delivered notifications, newest first.

     Returns a page of the notifications delivered to the contact in the path, with the same window and
    outcome filters, the same row shape and the same expansions as the account-wide list. Use it when
    the question is about one address; the collection read at /contact/notification serves cross-contact
    audits.

    Args:
        id (UUID):
        from_ (int | Unset):
        to (int | Unset):
        outcome (list[ListContactNotificationOutcomeItem] | Unset):
        expand (list[ListContactNotificationExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListContactNotificationFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AlertLogPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        id=id,
        from_=from_,
        to=to,
        outcome=outcome,
        expand=expand,
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    outcome: list[ListContactNotificationOutcomeItem] | Unset = UNSET,
    expand: list[ListContactNotificationExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListContactNotificationFieldsItem] | Unset = UNSET,
) -> (
    AlertLogPage
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
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | None
):
    """List one contact's delivered notifications, newest first.

     Returns a page of the notifications delivered to the contact in the path, with the same window and
    outcome filters, the same row shape and the same expansions as the account-wide list. Use it when
    the question is about one address; the collection read at /contact/notification serves cross-contact
    audits.

    Args:
        id (UUID):
        from_ (int | Unset):
        to (int | Unset):
        outcome (list[ListContactNotificationOutcomeItem] | Unset):
        expand (list[ListContactNotificationExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListContactNotificationFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AlertLogPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            from_=from_,
            to=to,
            outcome=outcome,
            expand=expand,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
