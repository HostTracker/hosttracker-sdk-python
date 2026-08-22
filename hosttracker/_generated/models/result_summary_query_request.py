from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.result_summary_query_request_bucket import (
    ResultSummaryQueryRequestBucket,
    check_result_summary_query_request_bucket,
)
from ..models.result_summary_query_request_expand_item import (
    ResultSummaryQueryRequestExpandItem,
    check_result_summary_query_request_expand_item,
)
from ..models.result_summary_query_request_fields_item import (
    ResultSummaryQueryRequestFieldsItem,
    check_result_summary_query_request_fields_item,
)
from ..models.result_summary_query_request_group_by import (
    ResultSummaryQueryRequestGroupBy,
    check_result_summary_query_request_group_by,
)
from ..models.result_summary_query_request_metrics_item import (
    ResultSummaryQueryRequestMetricsItem,
    check_result_summary_query_request_metrics_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResultSummaryQueryRequest")


@_attrs_define
class ResultSummaryQueryRequest:
    """The parameters, as one JSON object. A list-valued filter is a JSON array; everything else is a string, number or
    boolean. An omitted member and an explicit null both mean the parameter was not sent, and an empty array means it
    was sent empty - which every list filter refuses, exactly as it refuses an empty value on the query string.

    """

    monitor: list[str]
    """ The monitors to summarise. **Required** for the default per-monitor grouping - there is no account-wide
    default on a per-monitor read. With `groupBy=account` it becomes OPTIONAL: omitting it rolls the whole account
    into one row per bucket, which is the question that grouping exists for. """
    group_by: ResultSummaryQueryRequestGroupBy | Unset = UNSET
    """ `monitor` (the default) - one row per monitor per bucket; `account` - one row per bucket, aggregated across
    every monitor the request covers. """
    from_: int | Unset = UNSET
    """ The start of the time window, in Unix seconds. """
    to: int | Unset = UNSET
    """ The end of the time window, in Unix seconds. """
    bucket: ResultSummaryQueryRequestBucket | Unset = UNSET
    """ `none` | `hour` | `day` | `week` | `month`. `none` (the default) is the aggregate; anything else is the
    SERIES - which is why the chart leg is no longer a different endpoint with a different date vocabulary. """
    sla: float | Unset = UNSET
    """ An ad-hoc SLA target in percent, overriding each monitor's own `slaTarget` for this request only. The per-
    monitor target is what stops a tiered account multiplying the call. """
    metrics: list[ResultSummaryQueryRequestMetricsItem] | Unset = UNSET
    """ Which timing metrics to include. """
    expand: list[ResultSummaryQueryRequestExpandItem] | Unset = UNSET
    """ Comma-separated names of the extra blocks to embed. The only composition spelling on this surface - an
    unrecognised name is refused, never dropped, and the refusal lists what is allowed. A repeated key is accepted
    too and unions with the comma list, so expand=a,b and expand=a&expand=b ask the same thing. Sending it REPLACES
    the endpoint's defaults, so `expand=` on its own asks for the leanest row - present and empty, which is not the
    same as not sending it. Nothing relational is ever on by default: a list returns bare rows and a single read
    returns the resource's own detail. On a row that belongs to a monitor, `monitor.<value>` (settings,
    subscription, lastIncident, maintenance) embeds that block inside the row's `monitor` object and implies
    `monitor` itself. """
    limit: int | Unset = 50
    """ Rows to return. """
    cursor: str | Unset = UNSET
    """ Opaque cursor from a previous response's `nextCursor`. Absent ⇒ first page. """
    fields: list[ResultSummaryQueryRequestFieldsItem] | Unset = UNSET
    """ Which top-level members to keep on each row - `fields=id,name`. Everything else is dropped; `id` is always
    returned whether or not you name it, and the envelope (`data`, `nextCursor`, `hasMore`, `count`, `summary`) is
    never affected. A block an `expand=` adds is a member like any other, so `fields=id,monitor&expand=monitor`
    returns the id and the monitor block. An unrecognised name is refused, never dropped, and the refusal lists what
    this row publishes. `id` is accepted on every row, including the rows that publish no `id` member - there it
    simply keeps nothing, and a mask that would keep NOTHING at all (`fields=` or `fields=id` on such a row) is
    refused rather than answered with an empty object. """

    def to_dict(self) -> dict[str, Any]:
        monitor = self.monitor

        group_by: str | Unset = UNSET
        if not isinstance(self.group_by, Unset):
            group_by = self.group_by

        from_ = self.from_

        to = self.to

        bucket: str | Unset = UNSET
        if not isinstance(self.bucket, Unset):
            bucket = self.bucket

        sla = self.sla

        metrics: list[str] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item: str = metrics_item_data
                metrics.append(metrics_item)

        expand: list[str] | Unset = UNSET
        if not isinstance(self.expand, Unset):
            expand = []
            for expand_item_data in self.expand:
                expand_item: str = expand_item_data
                expand.append(expand_item)

        limit = self.limit

        cursor = self.cursor

        fields: list[str] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item: str = fields_item_data
                fields.append(fields_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "monitor": monitor,
            }
        )
        if group_by is not UNSET:
            field_dict["groupBy"] = group_by
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if sla is not UNSET:
            field_dict["sla"] = sla
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if expand is not UNSET:
            field_dict["expand"] = expand
        if limit is not UNSET:
            field_dict["limit"] = limit
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monitor = cast(list[str], d.pop("monitor"))

        _group_by = d.pop("groupBy", UNSET)
        group_by: ResultSummaryQueryRequestGroupBy | Unset
        if isinstance(_group_by, Unset):
            group_by = UNSET
        else:
            group_by = check_result_summary_query_request_group_by(_group_by)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        _bucket = d.pop("bucket", UNSET)
        bucket: ResultSummaryQueryRequestBucket | Unset
        if isinstance(_bucket, Unset):
            bucket = UNSET
        else:
            bucket = check_result_summary_query_request_bucket(_bucket)

        sla = d.pop("sla", UNSET)

        _metrics = d.pop("metrics", UNSET)
        metrics: list[ResultSummaryQueryRequestMetricsItem] | Unset = UNSET
        if _metrics is not UNSET:
            metrics = []
            for metrics_item_data in _metrics:
                metrics_item = check_result_summary_query_request_metrics_item(metrics_item_data)

                metrics.append(metrics_item)

        _expand = d.pop("expand", UNSET)
        expand: list[ResultSummaryQueryRequestExpandItem] | Unset = UNSET
        if _expand is not UNSET:
            expand = []
            for expand_item_data in _expand:
                expand_item = check_result_summary_query_request_expand_item(expand_item_data)

                expand.append(expand_item)

        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[ResultSummaryQueryRequestFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = check_result_summary_query_request_fields_item(fields_item_data)

                fields.append(fields_item)

        result_summary_query_request = cls(
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

        return result_summary_query_request
