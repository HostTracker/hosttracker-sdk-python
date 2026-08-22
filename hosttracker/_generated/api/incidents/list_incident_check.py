from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_cursor import InvalidCursor
from ...models.invalid_limit import InvalidLimit
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.list_incident_check_expand_item import ListIncidentCheckExpandItem
from ...models.list_incident_check_fields_item import ListIncidentCheckFieldsItem
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.package_limit import PackageLimit
from ...models.quota_exceeded import QuotaExceeded
from ...models.result_page import ResultPage
from ...models.unknown_expand import UnknownExpand
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    expand: list[ListIncidentCheckExpandItem] | Unset = UNSET,
    fields: list[ListIncidentCheckFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_expand: list[str] | Unset = UNSET
    if not isinstance(expand, Unset):
        json_expand = []
        for expand_item_data in expand:
            expand_item: str = expand_item_data
            json_expand.append(expand_item)

    params["expand"] = json_expand

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
        "url": "/monitor/incident/{id}/check".format(
            id=quote(str(id), safe=""),
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
    | PackageLimit
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | ResultPage
    | None
):
    if response.status_code == 200:
        response_200 = ResultPage.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = InvalidToken.from_dict(response.json())

        return response_401

    if response.status_code == 403:

        def _parse_response_403(data: object) -> InsufficientRights | IpNotAllowed | MissingScope | PackageLimit:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_0 = PackageLimit.from_dict(data)

                return response_403_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_1 = MissingScope.from_dict(data)

                return response_403_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_403_type_2 = InsufficientRights.from_dict(data)

                return response_403_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_403_type_3 = IpNotAllowed.from_dict(data)

            return response_403_type_3

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
        ) -> InvalidCursor | InvalidLimit | UnknownExpand | UnknownField | UnknownParameter:
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
    | PackageLimit
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | ResultPage
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    expand: list[ListIncidentCheckExpandItem] | Unset = UNSET,
    fields: list[ListIncidentCheckFieldsItem] | Unset = UNSET,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | ResultPage
]:
    """List the failing checks recorded inside one incident.

     Returns a page of the failed checks that occurred during one incident, each linking to its full
    result and page snapshot. Use it to see exactly what happened check by check during an outage,
    rather than re-deriving the episode from the raw result feed. Availability depends on the account's
    plan, and a plan refusal names the feature it needs. Each row carries the monitor's identifying
    projection and the recheck constellation behind the failure. Ask for expand=metrics to decode each
    check's stored measurements and, from the same document, the assertion rules it failed and the
    policy codes it violated - the per-check counterpart of the detail the incident's own timeline
    carries for the transitions that opened and closed the episode.

    Args:
        id (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        expand (list[ListIncidentCheckExpandItem] | Unset):
        fields (list[ListIncidentCheckFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidCursor | InvalidLimit | UnknownExpand | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | ResultPage]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        cursor=cursor,
        expand=expand,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    expand: list[ListIncidentCheckExpandItem] | Unset = UNSET,
    fields: list[ListIncidentCheckFieldsItem] | Unset = UNSET,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | ResultPage
    | None
):
    """List the failing checks recorded inside one incident.

     Returns a page of the failed checks that occurred during one incident, each linking to its full
    result and page snapshot. Use it to see exactly what happened check by check during an outage,
    rather than re-deriving the episode from the raw result feed. Availability depends on the account's
    plan, and a plan refusal names the feature it needs. Each row carries the monitor's identifying
    projection and the recheck constellation behind the failure. Ask for expand=metrics to decode each
    check's stored measurements and, from the same document, the assertion rules it failed and the
    policy codes it violated - the per-check counterpart of the detail the incident's own timeline
    carries for the transitions that opened and closed the episode.

    Args:
        id (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        expand (list[ListIncidentCheckExpandItem] | Unset):
        fields (list[ListIncidentCheckFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidCursor | InvalidLimit | UnknownExpand | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | ResultPage
    """

    return sync_detailed(
        id=id,
        client=client,
        limit=limit,
        cursor=cursor,
        expand=expand,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    expand: list[ListIncidentCheckExpandItem] | Unset = UNSET,
    fields: list[ListIncidentCheckFieldsItem] | Unset = UNSET,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | ResultPage
]:
    """List the failing checks recorded inside one incident.

     Returns a page of the failed checks that occurred during one incident, each linking to its full
    result and page snapshot. Use it to see exactly what happened check by check during an outage,
    rather than re-deriving the episode from the raw result feed. Availability depends on the account's
    plan, and a plan refusal names the feature it needs. Each row carries the monitor's identifying
    projection and the recheck constellation behind the failure. Ask for expand=metrics to decode each
    check's stored measurements and, from the same document, the assertion rules it failed and the
    policy codes it violated - the per-check counterpart of the detail the incident's own timeline
    carries for the transitions that opened and closed the episode.

    Args:
        id (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        expand (list[ListIncidentCheckExpandItem] | Unset):
        fields (list[ListIncidentCheckFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidCursor | InvalidLimit | UnknownExpand | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | ResultPage]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        cursor=cursor,
        expand=expand,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    expand: list[ListIncidentCheckExpandItem] | Unset = UNSET,
    fields: list[ListIncidentCheckFieldsItem] | Unset = UNSET,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | PackageLimit
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | ResultPage
    | None
):
    """List the failing checks recorded inside one incident.

     Returns a page of the failed checks that occurred during one incident, each linking to its full
    result and page snapshot. Use it to see exactly what happened check by check during an outage,
    rather than re-deriving the episode from the raw result feed. Availability depends on the account's
    plan, and a plan refusal names the feature it needs. Each row carries the monitor's identifying
    projection and the recheck constellation behind the failure. Ask for expand=metrics to decode each
    check's stored measurements and, from the same document, the assertion rules it failed and the
    policy codes it violated - the per-check counterpart of the detail the incident's own timeline
    carries for the transitions that opened and closed the episode.

    Args:
        id (str):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        expand (list[ListIncidentCheckExpandItem] | Unset):
        fields (list[ListIncidentCheckFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | PackageLimit | InternalError | InvalidCursor | InvalidLimit | UnknownExpand | UnknownField | UnknownParameter | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | ResultPage
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            limit=limit,
            cursor=cursor,
            expand=expand,
            fields=fields,
        )
    ).parsed
