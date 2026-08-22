from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_cursor import InvalidCursor
from ...models.invalid_limit import InvalidLimit
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.job_list_item_page import JobListItemPage
from ...models.list_job_fields_item import ListJobFieldsItem
from ...models.list_job_state_item import ListJobStateItem
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    kind: list[str] | Unset = UNSET,
    state: list[ListJobStateItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListJobFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_kind: list[str] | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind

    params["kind"] = json_kind

    json_state: list[str] | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item: str = state_item_data
            json_state.append(state_item)

    params["state"] = json_state

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
        "url": "/job",
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
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | JobListItemPage
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    if response.status_code == 200:
        response_200 = JobListItemPage.from_dict(response.json())

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
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | JobListItemPage
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
    kind: list[str] | Unset = UNSET,
    state: list[ListJobStateItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListJobFieldsItem] | Unset = UNSET,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | JobListItemPage
    | MethodNotAllowed
    | QuotaExceeded
]:
    """List this account's recent asynchronous operations.

     Returns a page of the asynchronous operations this account has started, newest first, optionally
    narrowed by kind or state. Reach for it when a job id was lost between starting the work and polling
    it, or to show what is currently running. Rows carry each job's state, progress and counts but not
    its per-item results - follow a row's results url to read those. Jobs are readable for seven days,
    which is what bounds this list.

    Args:
        kind (list[str] | Unset):
        state (list[ListJobStateItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListJobFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownEnumValue | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | JobListItemPage | MethodNotAllowed | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        kind=kind,
        state=state,
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
    kind: list[str] | Unset = UNSET,
    state: list[ListJobStateItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListJobFieldsItem] | Unset = UNSET,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | JobListItemPage
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    """List this account's recent asynchronous operations.

     Returns a page of the asynchronous operations this account has started, newest first, optionally
    narrowed by kind or state. Reach for it when a job id was lost between starting the work and polling
    it, or to show what is currently running. Rows carry each job's state, progress and counts but not
    its per-item results - follow a row's results url to read those. Jobs are readable for seven days,
    which is what bounds this list.

    Args:
        kind (list[str] | Unset):
        state (list[ListJobStateItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListJobFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownEnumValue | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | JobListItemPage | MethodNotAllowed | QuotaExceeded
    """

    return sync_detailed(
        client=client,
        kind=kind,
        state=state,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    kind: list[str] | Unset = UNSET,
    state: list[ListJobStateItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListJobFieldsItem] | Unset = UNSET,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | JobListItemPage
    | MethodNotAllowed
    | QuotaExceeded
]:
    """List this account's recent asynchronous operations.

     Returns a page of the asynchronous operations this account has started, newest first, optionally
    narrowed by kind or state. Reach for it when a job id was lost between starting the work and polling
    it, or to show what is currently running. Rows carry each job's state, progress and counts but not
    its per-item results - follow a row's results url to read those. Jobs are readable for seven days,
    which is what bounds this list.

    Args:
        kind (list[str] | Unset):
        state (list[ListJobStateItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListJobFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownEnumValue | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | JobListItemPage | MethodNotAllowed | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        kind=kind,
        state=state,
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    kind: list[str] | Unset = UNSET,
    state: list[ListJobStateItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListJobFieldsItem] | Unset = UNSET,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownEnumValue
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | JobListItemPage
    | MethodNotAllowed
    | QuotaExceeded
    | None
):
    """List this account's recent asynchronous operations.

     Returns a page of the asynchronous operations this account has started, newest first, optionally
    narrowed by kind or state. Reach for it when a job id was lost between starting the work and polling
    it, or to show what is currently running. Rows carry each job's state, progress and counts but not
    its per-item results - follow a row's results url to read those. Jobs are readable for seven days,
    which is what bounds this list.

    Args:
        kind (list[str] | Unset):
        state (list[ListJobStateItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListJobFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | UnknownEnumValue | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | JobListItemPage | MethodNotAllowed | QuotaExceeded
    """

    return (
        await asyncio_detailed(
            client=client,
            kind=kind,
            state=state,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
