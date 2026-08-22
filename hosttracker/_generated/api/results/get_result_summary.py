from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.filter_required import FilterRequired
from ...models.get_result_summary_bucket import GetResultSummaryBucket
from ...models.get_result_summary_expand_item import GetResultSummaryExpandItem
from ...models.get_result_summary_fields_item import GetResultSummaryFieldsItem
from ...models.get_result_summary_group_by import GetResultSummaryGroupBy
from ...models.get_result_summary_metrics_item import GetResultSummaryMetricsItem
from ...models.insufficient_rights import InsufficientRights
from ...models.internal_error import InternalError
from ...models.invalid_cursor import InvalidCursor
from ...models.invalid_limit import InvalidLimit
from ...models.invalid_range import InvalidRange
from ...models.invalid_token import InvalidToken
from ...models.ip_not_allowed import IpNotAllowed
from ...models.method_not_allowed import MethodNotAllowed
from ...models.missing_scope import MissingScope
from ...models.quota_exceeded import QuotaExceeded
from ...models.service_unavailable import ServiceUnavailable
from ...models.too_many_items import TooManyItems
from ...models.unknown_enum_value import UnknownEnumValue
from ...models.unknown_expand import UnknownExpand
from ...models.unknown_field import UnknownField
from ...models.unknown_parameter import UnknownParameter
from ...models.uptime_summary_page import UptimeSummaryPage
from ...models.validation_failed import ValidationFailed
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    monitor: list[str],
    group_by: GetResultSummaryGroupBy | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    bucket: GetResultSummaryBucket | Unset = UNSET,
    sla: float | Unset = UNSET,
    metrics: list[GetResultSummaryMetricsItem] | Unset = UNSET,
    expand: list[GetResultSummaryExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[GetResultSummaryFieldsItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_monitor = monitor

    params["monitor"] = json_monitor

    json_group_by: str | Unset = UNSET
    if not isinstance(group_by, Unset):
        json_group_by = group_by

    params["groupBy"] = json_group_by

    params["from"] = from_

    params["to"] = to

    json_bucket: str | Unset = UNSET
    if not isinstance(bucket, Unset):
        json_bucket = bucket

    params["bucket"] = json_bucket

    params["sla"] = sla

    json_metrics: list[str] | Unset = UNSET
    if not isinstance(metrics, Unset):
        json_metrics = []
        for metrics_item_data in metrics:
            metrics_item: str = metrics_item_data
            json_metrics.append(metrics_item)

    params["metrics"] = json_metrics

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
        "url": "/monitor/result/summary",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FilterRequired
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | TooManyItems
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | ServiceUnavailable
    | UptimeSummaryPage
    | None
):
    if response.status_code == 200:
        response_200 = UptimeSummaryPage.from_dict(response.json())

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
            FilterRequired
            | InvalidCursor
            | InvalidLimit
            | InvalidRange
            | TooManyItems
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
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_7 = FilterRequired.from_dict(data)

                return response_422_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_8 = TooManyItems.from_dict(data)

                return response_422_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_9 = UnknownParameter.from_dict(data)

            return response_422_type_9

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
    FilterRequired
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | TooManyItems
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | ServiceUnavailable
    | UptimeSummaryPage
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
    monitor: list[str],
    group_by: GetResultSummaryGroupBy | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    bucket: GetResultSummaryBucket | Unset = UNSET,
    sla: float | Unset = UNSET,
    metrics: list[GetResultSummaryMetricsItem] | Unset = UNSET,
    expand: list[GetResultSummaryExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[GetResultSummaryFieldsItem] | Unset = UNSET,
) -> Response[
    FilterRequired
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | TooManyItems
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | ServiceUnavailable
    | UptimeSummaryPage
]:
    """Get uptime, SLA and response-time figures across monitors.

     Returns aggregated uptime and SLA figures for the monitors named in the request over a time window -
    as one aggregate per monitor, or as a bucketed series ready to chart. Optional timing metrics add
    response time and its phases, each point carrying the mean, the 95th percentile and how many checks
    it was drawn from. Use it instead of reading raw results whenever the question is about a period
    rather than a check. A window that would produce too many buckets is refused with the largest window
    that would fit, not silently truncated. Every row carries the seconds it was built from - up, down,
    total measured, and the maintenance time split into the part the monitor spent up and the part it
    spent down - together with the checks recorded, split the same way. Read the uptime percentage
    rather than dividing those seconds yourself: on the whole-window aggregate it comes from the stored
    daily statistics, which is the figure the rest of the product reports. Set groupBy=account to fold
    the rows into one per bucket across the whole selection - seconds and counts summed, the percentage
    recomputed from those sums rather than averaged across monitors, plus how many monitors it covers,
    whether it covered the account or only a named selection, and whether the timing figures were
    sampled. The monitor filter is optional in that mode; because the roll-up reads every monitor it
    covers, its window is capped at 30 days and a selection of more than a couple of thousand monitors
    is refused rather than sampled - an availability figure over some of the monitors would be silently
    wrong. Timing metrics take the opposite trade there: over many monitors they are drawn from a
    bounded sample and the row says so, instead of being refused. Nothing is embedded by default: ask
    for expand=monitor for the monitor's identifying projection, and expand=monitor.settings /
    monitor.subscription / monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks
    inside it. An account roll-up row aggregates many monitors, so it has no monitor to embed and the
    monitor expansion is refused there.

    Args:
        monitor (list[str]):
        group_by (GetResultSummaryGroupBy | Unset):
        from_ (int | Unset):
        to (int | Unset):
        bucket (GetResultSummaryBucket | Unset):
        sla (float | Unset):
        metrics (list[GetResultSummaryMetricsItem] | Unset):
        expand (list[GetResultSummaryExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[GetResultSummaryFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilterRequired | InvalidCursor | InvalidLimit | InvalidRange | TooManyItems | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | QuotaExceeded | ServiceUnavailable | UptimeSummaryPage]
    """

    kwargs = _get_kwargs(
        monitor=monitor,
        group_by=group_by,
        from_=from_,
        to=to,
        bucket=bucket,
        sla=sla,
        metrics=metrics,
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
    monitor: list[str],
    group_by: GetResultSummaryGroupBy | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    bucket: GetResultSummaryBucket | Unset = UNSET,
    sla: float | Unset = UNSET,
    metrics: list[GetResultSummaryMetricsItem] | Unset = UNSET,
    expand: list[GetResultSummaryExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[GetResultSummaryFieldsItem] | Unset = UNSET,
) -> (
    FilterRequired
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | TooManyItems
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | ServiceUnavailable
    | UptimeSummaryPage
    | None
):
    """Get uptime, SLA and response-time figures across monitors.

     Returns aggregated uptime and SLA figures for the monitors named in the request over a time window -
    as one aggregate per monitor, or as a bucketed series ready to chart. Optional timing metrics add
    response time and its phases, each point carrying the mean, the 95th percentile and how many checks
    it was drawn from. Use it instead of reading raw results whenever the question is about a period
    rather than a check. A window that would produce too many buckets is refused with the largest window
    that would fit, not silently truncated. Every row carries the seconds it was built from - up, down,
    total measured, and the maintenance time split into the part the monitor spent up and the part it
    spent down - together with the checks recorded, split the same way. Read the uptime percentage
    rather than dividing those seconds yourself: on the whole-window aggregate it comes from the stored
    daily statistics, which is the figure the rest of the product reports. Set groupBy=account to fold
    the rows into one per bucket across the whole selection - seconds and counts summed, the percentage
    recomputed from those sums rather than averaged across monitors, plus how many monitors it covers,
    whether it covered the account or only a named selection, and whether the timing figures were
    sampled. The monitor filter is optional in that mode; because the roll-up reads every monitor it
    covers, its window is capped at 30 days and a selection of more than a couple of thousand monitors
    is refused rather than sampled - an availability figure over some of the monitors would be silently
    wrong. Timing metrics take the opposite trade there: over many monitors they are drawn from a
    bounded sample and the row says so, instead of being refused. Nothing is embedded by default: ask
    for expand=monitor for the monitor's identifying projection, and expand=monitor.settings /
    monitor.subscription / monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks
    inside it. An account roll-up row aggregates many monitors, so it has no monitor to embed and the
    monitor expansion is refused there.

    Args:
        monitor (list[str]):
        group_by (GetResultSummaryGroupBy | Unset):
        from_ (int | Unset):
        to (int | Unset):
        bucket (GetResultSummaryBucket | Unset):
        sla (float | Unset):
        metrics (list[GetResultSummaryMetricsItem] | Unset):
        expand (list[GetResultSummaryExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[GetResultSummaryFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilterRequired | InvalidCursor | InvalidLimit | InvalidRange | TooManyItems | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | QuotaExceeded | ServiceUnavailable | UptimeSummaryPage
    """

    return sync_detailed(
        client=client,
        monitor=monitor,
        group_by=group_by,
        from_=from_,
        to=to,
        bucket=bucket,
        sla=sla,
        metrics=metrics,
        expand=expand,
        limit=limit,
        cursor=cursor,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    monitor: list[str],
    group_by: GetResultSummaryGroupBy | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    bucket: GetResultSummaryBucket | Unset = UNSET,
    sla: float | Unset = UNSET,
    metrics: list[GetResultSummaryMetricsItem] | Unset = UNSET,
    expand: list[GetResultSummaryExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[GetResultSummaryFieldsItem] | Unset = UNSET,
) -> Response[
    FilterRequired
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | TooManyItems
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | ServiceUnavailable
    | UptimeSummaryPage
]:
    """Get uptime, SLA and response-time figures across monitors.

     Returns aggregated uptime and SLA figures for the monitors named in the request over a time window -
    as one aggregate per monitor, or as a bucketed series ready to chart. Optional timing metrics add
    response time and its phases, each point carrying the mean, the 95th percentile and how many checks
    it was drawn from. Use it instead of reading raw results whenever the question is about a period
    rather than a check. A window that would produce too many buckets is refused with the largest window
    that would fit, not silently truncated. Every row carries the seconds it was built from - up, down,
    total measured, and the maintenance time split into the part the monitor spent up and the part it
    spent down - together with the checks recorded, split the same way. Read the uptime percentage
    rather than dividing those seconds yourself: on the whole-window aggregate it comes from the stored
    daily statistics, which is the figure the rest of the product reports. Set groupBy=account to fold
    the rows into one per bucket across the whole selection - seconds and counts summed, the percentage
    recomputed from those sums rather than averaged across monitors, plus how many monitors it covers,
    whether it covered the account or only a named selection, and whether the timing figures were
    sampled. The monitor filter is optional in that mode; because the roll-up reads every monitor it
    covers, its window is capped at 30 days and a selection of more than a couple of thousand monitors
    is refused rather than sampled - an availability figure over some of the monitors would be silently
    wrong. Timing metrics take the opposite trade there: over many monitors they are drawn from a
    bounded sample and the row says so, instead of being refused. Nothing is embedded by default: ask
    for expand=monitor for the monitor's identifying projection, and expand=monitor.settings /
    monitor.subscription / monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks
    inside it. An account roll-up row aggregates many monitors, so it has no monitor to embed and the
    monitor expansion is refused there.

    Args:
        monitor (list[str]):
        group_by (GetResultSummaryGroupBy | Unset):
        from_ (int | Unset):
        to (int | Unset):
        bucket (GetResultSummaryBucket | Unset):
        sla (float | Unset):
        metrics (list[GetResultSummaryMetricsItem] | Unset):
        expand (list[GetResultSummaryExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[GetResultSummaryFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilterRequired | InvalidCursor | InvalidLimit | InvalidRange | TooManyItems | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | QuotaExceeded | ServiceUnavailable | UptimeSummaryPage]
    """

    kwargs = _get_kwargs(
        monitor=monitor,
        group_by=group_by,
        from_=from_,
        to=to,
        bucket=bucket,
        sla=sla,
        metrics=metrics,
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
    monitor: list[str],
    group_by: GetResultSummaryGroupBy | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    bucket: GetResultSummaryBucket | Unset = UNSET,
    sla: float | Unset = UNSET,
    metrics: list[GetResultSummaryMetricsItem] | Unset = UNSET,
    expand: list[GetResultSummaryExpandItem] | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    fields: list[GetResultSummaryFieldsItem] | Unset = UNSET,
) -> (
    FilterRequired
    | InvalidCursor
    | InvalidLimit
    | InvalidRange
    | TooManyItems
    | UnknownEnumValue
    | UnknownExpand
    | UnknownField
    | UnknownParameter
    | ValidationFailed
    | InsufficientRights
    | IpNotAllowed
    | MissingScope
    | InternalError
    | InvalidToken
    | MethodNotAllowed
    | QuotaExceeded
    | ServiceUnavailable
    | UptimeSummaryPage
    | None
):
    """Get uptime, SLA and response-time figures across monitors.

     Returns aggregated uptime and SLA figures for the monitors named in the request over a time window -
    as one aggregate per monitor, or as a bucketed series ready to chart. Optional timing metrics add
    response time and its phases, each point carrying the mean, the 95th percentile and how many checks
    it was drawn from. Use it instead of reading raw results whenever the question is about a period
    rather than a check. A window that would produce too many buckets is refused with the largest window
    that would fit, not silently truncated. Every row carries the seconds it was built from - up, down,
    total measured, and the maintenance time split into the part the monitor spent up and the part it
    spent down - together with the checks recorded, split the same way. Read the uptime percentage
    rather than dividing those seconds yourself: on the whole-window aggregate it comes from the stored
    daily statistics, which is the figure the rest of the product reports. Set groupBy=account to fold
    the rows into one per bucket across the whole selection - seconds and counts summed, the percentage
    recomputed from those sums rather than averaged across monitors, plus how many monitors it covers,
    whether it covered the account or only a named selection, and whether the timing figures were
    sampled. The monitor filter is optional in that mode; because the roll-up reads every monitor it
    covers, its window is capped at 30 days and a selection of more than a couple of thousand monitors
    is refused rather than sampled - an availability figure over some of the monitors would be silently
    wrong. Timing metrics take the opposite trade there: over many monitors they are drawn from a
    bounded sample and the row says so, instead of being refused. Nothing is embedded by default: ask
    for expand=monitor for the monitor's identifying projection, and expand=monitor.settings /
    monitor.subscription / monitor.lastIncident / monitor.maintenance to embed the monitor's own blocks
    inside it. An account roll-up row aggregates many monitors, so it has no monitor to embed and the
    monitor expansion is refused there.

    Args:
        monitor (list[str]):
        group_by (GetResultSummaryGroupBy | Unset):
        from_ (int | Unset):
        to (int | Unset):
        bucket (GetResultSummaryBucket | Unset):
        sla (float | Unset):
        metrics (list[GetResultSummaryMetricsItem] | Unset):
        expand (list[GetResultSummaryExpandItem] | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        fields (list[GetResultSummaryFieldsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilterRequired | InvalidCursor | InvalidLimit | InvalidRange | TooManyItems | UnknownEnumValue | UnknownExpand | UnknownField | UnknownParameter | ValidationFailed | InsufficientRights | IpNotAllowed | MissingScope | InternalError | InvalidToken | MethodNotAllowed | QuotaExceeded | ServiceUnavailable | UptimeSummaryPage
    """

    return (
        await asyncio_detailed(
            client=client,
            monitor=monitor,
            group_by=group_by,
            from_=from_,
            to=to,
            bucket=bucket,
            sla=sla,
            metrics=metrics,
            expand=expand,
            limit=limit,
            cursor=cursor,
            fields=fields,
        )
    ).parsed
