from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_monitor_result_expand_item import GetMonitorResultExpandItem
from ...models.get_monitor_result_fields_item import GetMonitorResultFieldsItem
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.quota_exceeded import QuotaExceeded
from ...models.result_view import ResultView
from ...models.service_unavailable import ServiceUnavailable
from ...models.unknown_expand import UnknownExpand
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    monitor_id: UUID,
    id: str,
    *,
    expand: list[GetMonitorResultExpandItem] | Unset = UNSET,
    fields: list[GetMonitorResultFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

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
        "url": "/monitor/{monitor_id}/result/{id}".format(
            monitor_id=quote(str(monitor_id), safe=""),
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
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | ResultView
    | ServiceUnavailable
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | None
):
    if response.status_code == 200:
        response_200 = ResultView.from_dict(response.json())

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

        def _parse_response_422(data: object) -> UnknownExpand | UnknownField | UnknownParameter:
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

    if response.status_code == 503:
        response_503 = ServiceUnavailable.from_dict(response.json())

        return response_503

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
    | NotFound
    | QuotaExceeded
    | ResultView
    | ServiceUnavailable
    | UnknownExpand
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
    id: str,
    *,
    client: AuthenticatedClient,
    expand: list[GetMonitorResultExpandItem] | Unset = UNSET,
    fields: list[GetMonitorResultFieldsItem] | Unset = UNSET,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | ResultView
    | ServiceUnavailable
    | UnknownExpand
    | UnknownField
    | UnknownParameter
]:
    """Get one check result in full detail.

     Returns everything recorded for a single check: the verdict from each monitoring location, the
    timing breakdown, the decoded error, and any recheck that confirmed or refuted a failure. Use it
    once a result id is in hand; the list endpoint returns the same shape but is the wrong tool for one
    row. The response also says whether a page snapshot was captured for this check. Nothing is embedded
    by default: ask for expand=monitor for the monitor's identifying projection, and
    expand=monitor.settings / monitor.subscription / monitor.lastIncident / monitor.maintenance to embed
    the monitor's own blocks inside it. Ask for expand=metrics to decode the check's stored measurements
    and, from the same document, the assertion rules it failed and the policy codes it violated.

    Args:
        monitor_id (UUID):
        id (str):
        expand (list[GetMonitorResultExpandItem] | Unset):
        fields (list[GetMonitorResultFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | ResultView | ServiceUnavailable | UnknownExpand | UnknownField | UnknownParameter]
    """

    kwargs = _get_kwargs(
        monitor_id=monitor_id,
        id=id,
        expand=expand,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    monitor_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
    expand: list[GetMonitorResultExpandItem] | Unset = UNSET,
    fields: list[GetMonitorResultFieldsItem] | Unset = UNSET,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | ResultView
    | ServiceUnavailable
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | None
):
    """Get one check result in full detail.

     Returns everything recorded for a single check: the verdict from each monitoring location, the
    timing breakdown, the decoded error, and any recheck that confirmed or refuted a failure. Use it
    once a result id is in hand; the list endpoint returns the same shape but is the wrong tool for one
    row. The response also says whether a page snapshot was captured for this check. Nothing is embedded
    by default: ask for expand=monitor for the monitor's identifying projection, and
    expand=monitor.settings / monitor.subscription / monitor.lastIncident / monitor.maintenance to embed
    the monitor's own blocks inside it. Ask for expand=metrics to decode the check's stored measurements
    and, from the same document, the assertion rules it failed and the policy codes it violated.

    Args:
        monitor_id (UUID):
        id (str):
        expand (list[GetMonitorResultExpandItem] | Unset):
        fields (list[GetMonitorResultFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | ResultView | ServiceUnavailable | UnknownExpand | UnknownField | UnknownParameter
    """

    return sync_detailed(
        monitor_id=monitor_id,
        id=id,
        client=client,
        expand=expand,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    monitor_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
    expand: list[GetMonitorResultExpandItem] | Unset = UNSET,
    fields: list[GetMonitorResultFieldsItem] | Unset = UNSET,
) -> Response[
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | ResultView
    | ServiceUnavailable
    | UnknownExpand
    | UnknownField
    | UnknownParameter
]:
    """Get one check result in full detail.

     Returns everything recorded for a single check: the verdict from each monitoring location, the
    timing breakdown, the decoded error, and any recheck that confirmed or refuted a failure. Use it
    once a result id is in hand; the list endpoint returns the same shape but is the wrong tool for one
    row. The response also says whether a page snapshot was captured for this check. Nothing is embedded
    by default: ask for expand=monitor for the monitor's identifying projection, and
    expand=monitor.settings / monitor.subscription / monitor.lastIncident / monitor.maintenance to embed
    the monitor's own blocks inside it. Ask for expand=metrics to decode the check's stored measurements
    and, from the same document, the assertion rules it failed and the policy codes it violated.

    Args:
        monitor_id (UUID):
        id (str):
        expand (list[GetMonitorResultExpandItem] | Unset):
        fields (list[GetMonitorResultFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | ResultView | ServiceUnavailable | UnknownExpand | UnknownField | UnknownParameter]
    """

    kwargs = _get_kwargs(
        monitor_id=monitor_id,
        id=id,
        expand=expand,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    monitor_id: UUID,
    id: str,
    *,
    client: AuthenticatedClient,
    expand: list[GetMonitorResultExpandItem] | Unset = UNSET,
    fields: list[GetMonitorResultFieldsItem] | Unset = UNSET,
) -> (
    InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | ResultView
    | ServiceUnavailable
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | None
):
    """Get one check result in full detail.

     Returns everything recorded for a single check: the verdict from each monitoring location, the
    timing breakdown, the decoded error, and any recheck that confirmed or refuted a failure. Use it
    once a result id is in hand; the list endpoint returns the same shape but is the wrong tool for one
    row. The response also says whether a page snapshot was captured for this check. Nothing is embedded
    by default: ask for expand=monitor for the monitor's identifying projection, and
    expand=monitor.settings / monitor.subscription / monitor.lastIncident / monitor.maintenance to embed
    the monitor's own blocks inside it. Ask for expand=metrics to decode the check's stored measurements
    and, from the same document, the assertion rules it failed and the policy codes it violated.

    Args:
        monitor_id (UUID):
        id (str):
        expand (list[GetMonitorResultExpandItem] | Unset):
        fields (list[GetMonitorResultFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | ResultView | ServiceUnavailable | UnknownExpand | UnknownField | UnknownParameter
    """

    return (
        await asyncio_detailed(
            monitor_id=monitor_id,
            id=id,
            client=client,
            expand=expand,
            fields=fields,
        )
    ).parsed
