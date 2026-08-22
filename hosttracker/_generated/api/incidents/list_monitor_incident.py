from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_page import IncidentPage
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_cursor import InvalidCursor
from ...models.invalid_limit import InvalidLimit
from ...models.invalid_range import InvalidRange
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.list_monitor_incident_expand_item import (
    ListMonitorIncidentExpandItem,
)
from ...models.list_monitor_incident_fields_item import (
    ListMonitorIncidentFieldsItem,
)
from ...models.list_monitor_incident_severity_item import (
    ListMonitorIncidentSeverityItem,
)
from ...models.list_monitor_incident_state_item import (
    ListMonitorIncidentStateItem,
)
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.not_found import NotFound
from ...models.quota_exceeded import QuotaExceeded
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_expand import UnknownExpand
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    monitor_id: UUID,
    *,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    severity: list[ListMonitorIncidentSeverityItem] | Unset = UNSET,
    state: list[ListMonitorIncidentStateItem] | Unset = UNSET,
    expand: list[ListMonitorIncidentExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorIncidentFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to

    json_severity: list[str] | Unset = UNSET
    if not isinstance(severity, Unset):
        json_severity = []
        for severity_item_data in severity:
            severity_item: str = severity_item_data
            json_severity.append(severity_item)

    params["severity"] = json_severity

    json_state: list[str] | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = []
        for state_item_data in state:
            state_item: str = state_item_data
            json_state.append(state_item)

    params["state"] = json_state

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
        "url": "/monitor/{monitor_id}/incident".format(
            monitor_id=quote(str(monitor_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    IncidentPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownExpand
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
        response_200 = IncidentPage.from_dict(response.json())

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
                response_422_type_5 = InvalidRange.from_dict(data)

                return response_422_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_6 = UnknownEnumValue.from_dict(data)

                return response_422_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_7 = UnknownParameter.from_dict(data)

            return response_422_type_7

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
    IncidentPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownExpand
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
    monitor_id: UUID,
    *,
    client: AuthenticatedClient,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    severity: list[ListMonitorIncidentSeverityItem] | Unset = UNSET,
    state: list[ListMonitorIncidentStateItem] | Unset = UNSET,
    expand: list[ListMonitorIncidentExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorIncidentFieldsItem] | Unset = UNSET,
) -> Response[
    IncidentPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
]:
    """List one monitor's down-episodes.

     Returns a page of the monitor's incidents, newest first, with the same window, severity, state and
    expansion options as the collection read, and no sort parameter - a single monitor's page has
    nothing to group by. Use it when the monitor is already known; the collection read at
    /monitor/incident serves cross-monitor and account-wide questions. Nothing is embedded by default:
    ask for expand=monitor for the monitor's identifying projection, and expand=monitor.settings /
    monitor.subscription / monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks
    inside it. expand=recheck adds the constellation that opened each episode.

    Args:
        monitor_id (UUID):
        from_ (int | Unset):
        to (int | Unset):
        severity (list[ListMonitorIncidentSeverityItem] | Unset):
        state (list[ListMonitorIncidentStateItem] | Unset):
        expand (list[ListMonitorIncidentExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMonitorIncidentFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        monitor_id=monitor_id,
        from_=from_,
        to=to,
        severity=severity,
        state=state,
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
    monitor_id: UUID,
    *,
    client: AuthenticatedClient,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    severity: list[ListMonitorIncidentSeverityItem] | Unset = UNSET,
    state: list[ListMonitorIncidentStateItem] | Unset = UNSET,
    expand: list[ListMonitorIncidentExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorIncidentFieldsItem] | Unset = UNSET,
) -> (
    IncidentPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | None
):
    """List one monitor's down-episodes.

     Returns a page of the monitor's incidents, newest first, with the same window, severity, state and
    expansion options as the collection read, and no sort parameter - a single monitor's page has
    nothing to group by. Use it when the monitor is already known; the collection read at
    /monitor/incident serves cross-monitor and account-wide questions. Nothing is embedded by default:
    ask for expand=monitor for the monitor's identifying projection, and expand=monitor.settings /
    monitor.subscription / monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks
    inside it. expand=recheck adds the constellation that opened each episode.

    Args:
        monitor_id (UUID):
        from_ (int | Unset):
        to (int | Unset):
        severity (list[ListMonitorIncidentSeverityItem] | Unset):
        state (list[ListMonitorIncidentStateItem] | Unset):
        expand (list[ListMonitorIncidentExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMonitorIncidentFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded
    """

    return sync_detailed(
        monitor_id=monitor_id,
        client=client,
        from_=from_,
        to=to,
        severity=severity,
        state=state,
        expand=expand,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    monitor_id: UUID,
    *,
    client: AuthenticatedClient,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    severity: list[ListMonitorIncidentSeverityItem] | Unset = UNSET,
    state: list[ListMonitorIncidentStateItem] | Unset = UNSET,
    expand: list[ListMonitorIncidentExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorIncidentFieldsItem] | Unset = UNSET,
) -> Response[
    IncidentPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
]:
    """List one monitor's down-episodes.

     Returns a page of the monitor's incidents, newest first, with the same window, severity, state and
    expansion options as the collection read, and no sort parameter - a single monitor's page has
    nothing to group by. Use it when the monitor is already known; the collection read at
    /monitor/incident serves cross-monitor and account-wide questions. Nothing is embedded by default:
    ask for expand=monitor for the monitor's identifying projection, and expand=monitor.settings /
    monitor.subscription / monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks
    inside it. expand=recheck adds the constellation that opened each episode.

    Args:
        monitor_id (UUID):
        from_ (int | Unset):
        to (int | Unset):
        severity (list[ListMonitorIncidentSeverityItem] | Unset):
        state (list[ListMonitorIncidentStateItem] | Unset):
        expand (list[ListMonitorIncidentExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMonitorIncidentFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded]
    """

    kwargs = _get_kwargs(
        monitor_id=monitor_id,
        from_=from_,
        to=to,
        severity=severity,
        state=state,
        expand=expand,
        limit=limit,
        cursor=cursor,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    monitor_id: UUID,
    *,
    client: AuthenticatedClient,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    severity: list[ListMonitorIncidentSeverityItem] | Unset = UNSET,
    state: list[ListMonitorIncidentStateItem] | Unset = UNSET,
    expand: list[ListMonitorIncidentExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[ListMonitorIncidentFieldsItem] | Unset = UNSET,
) -> (
    IncidentPage
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InvalidToken
    | MethodNotAllowed
    | NotFound
    | QuotaExceeded
    | None
):
    """List one monitor's down-episodes.

     Returns a page of the monitor's incidents, newest first, with the same window, severity, state and
    expansion options as the collection read, and no sort parameter - a single monitor's page has
    nothing to group by. Use it when the monitor is already known; the collection read at
    /monitor/incident serves cross-monitor and account-wide questions. Nothing is embedded by default:
    ask for expand=monitor for the monitor's identifying projection, and expand=monitor.settings /
    monitor.subscription / monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks
    inside it. expand=recheck adds the constellation that opened each episode.

    Args:
        monitor_id (UUID):
        from_ (int | Unset):
        to (int | Unset):
        severity (list[ListMonitorIncidentSeverityItem] | Unset):
        state (list[ListMonitorIncidentStateItem] | Unset):
        expand (list[ListMonitorIncidentExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[ListMonitorIncidentFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentPage | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidCursor | InvalidLimit | InvalidRange | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InvalidToken | MethodNotAllowed | NotFound | QuotaExceeded
    """

    return (
        await asyncio_detailed(
            monitor_id=monitor_id,
            client=client,
            from_=from_,
            to=to,
            severity=severity,
            state=state,
            expand=expand,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
