from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_incident_expand_item import GetIncidentExpandItem
from ...models.get_incident_fields_item import GetIncidentFieldsItem
from ...models.incident_view import IncidentView
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_expand import UnknownExpand
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    expand: list[GetIncidentExpandItem] | Unset = UNSET,
    fields: list[GetIncidentFieldsItem] | Unset = UNSET,
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
        "url": "/monitor/incident/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    IncidentView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | None
):
    if response.status_code == 200:
        response_200 = IncidentView.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    IncidentView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
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
    id: str,
    *,
    client: AuthenticatedClient,
    expand: list[GetIncidentExpandItem] | Unset = UNSET,
    fields: list[GetIncidentFieldsItem] | Unset = UNSET,
) -> Response[
    IncidentView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownExpand
    | UnknownField
    | UnknownParameter
]:
    """Get one incident, with the transitions that opened and closed it.

     Returns a single incident including the transition that opened it, the transition that closed it if
    it is resolved, and the per-location verdicts recorded at each. Use it when an incident id is
    already in hand and the whole timeline is wanted; the list endpoint returns the same rows but is the
    wrong tool for one. The response carries the underlying check ids, so a result can be read directly
    from here. Each timeline entry also carries the assertion rules that failed and the policy codes
    that were violated, when the check recorded any. Nothing is embedded by default: ask for
    expand=monitor for the monitor's identifying projection, and expand=monitor.settings /
    monitor.subscription / monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks
    inside it. expand=recheck adds the episode-level constellation beside the timeline.

    Args:
        id (str):
        expand (list[GetIncidentExpandItem] | Unset):
        fields (list[GetIncidentFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownExpand | UnknownField | UnknownParameter]
    """

    kwargs = _get_kwargs(
        id=id,
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
    expand: list[GetIncidentExpandItem] | Unset = UNSET,
    fields: list[GetIncidentFieldsItem] | Unset = UNSET,
) -> (
    IncidentView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | None
):
    """Get one incident, with the transitions that opened and closed it.

     Returns a single incident including the transition that opened it, the transition that closed it if
    it is resolved, and the per-location verdicts recorded at each. Use it when an incident id is
    already in hand and the whole timeline is wanted; the list endpoint returns the same rows but is the
    wrong tool for one. The response carries the underlying check ids, so a result can be read directly
    from here. Each timeline entry also carries the assertion rules that failed and the policy codes
    that were violated, when the check recorded any. Nothing is embedded by default: ask for
    expand=monitor for the monitor's identifying projection, and expand=monitor.settings /
    monitor.subscription / monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks
    inside it. expand=recheck adds the episode-level constellation beside the timeline.

    Args:
        id (str):
        expand (list[GetIncidentExpandItem] | Unset):
        fields (list[GetIncidentFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownExpand | UnknownField | UnknownParameter
    """

    return sync_detailed(
        id=id,
        client=client,
        expand=expand,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    expand: list[GetIncidentExpandItem] | Unset = UNSET,
    fields: list[GetIncidentFieldsItem] | Unset = UNSET,
) -> Response[
    IncidentView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownExpand
    | UnknownField
    | UnknownParameter
]:
    """Get one incident, with the transitions that opened and closed it.

     Returns a single incident including the transition that opened it, the transition that closed it if
    it is resolved, and the per-location verdicts recorded at each. Use it when an incident id is
    already in hand and the whole timeline is wanted; the list endpoint returns the same rows but is the
    wrong tool for one. The response carries the underlying check ids, so a result can be read directly
    from here. Each timeline entry also carries the assertion rules that failed and the policy codes
    that were violated, when the check recorded any. Nothing is embedded by default: ask for
    expand=monitor for the monitor's identifying projection, and expand=monitor.settings /
    monitor.subscription / monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks
    inside it. expand=recheck adds the episode-level constellation beside the timeline.

    Args:
        id (str):
        expand (list[GetIncidentExpandItem] | Unset):
        fields (list[GetIncidentFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownExpand | UnknownField | UnknownParameter]
    """

    kwargs = _get_kwargs(
        id=id,
        expand=expand,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    expand: list[GetIncidentExpandItem] | Unset = UNSET,
    fields: list[GetIncidentFieldsItem] | Unset = UNSET,
) -> (
    IncidentView
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | None
):
    """Get one incident, with the transitions that opened and closed it.

     Returns a single incident including the transition that opened it, the transition that closed it if
    it is resolved, and the per-location verdicts recorded at each. Use it when an incident id is
    already in hand and the whole timeline is wanted; the list endpoint returns the same rows but is the
    wrong tool for one. The response carries the underlying check ids, so a result can be read directly
    from here. Each timeline entry also carries the assertion rules that failed and the policy codes
    that were violated, when the check recorded any. Nothing is embedded by default: ask for
    expand=monitor for the monitor's identifying projection, and expand=monitor.settings /
    monitor.subscription / monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks
    inside it. expand=recheck adds the episode-level constellation beside the timeline.

    Args:
        id (str):
        expand (list[GetIncidentExpandItem] | Unset):
        fields (list[GetIncidentFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentView | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded | UnknownExpand | UnknownField | UnknownParameter
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            expand=expand,
            fields=fields,
        )
    ).parsed
