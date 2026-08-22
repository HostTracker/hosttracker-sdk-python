from typing import Literal

MonitorSpanQueryRequestFieldsItem = Literal[
    "comment", "eventCount", "firstCheckNumber", "from", "incidentId", "lastCheckNumber", "to", "up"
]

MONITOR_SPAN_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[MonitorSpanQueryRequestFieldsItem] = {
    "comment",
    "eventCount",
    "firstCheckNumber",
    "from",
    "incidentId",
    "lastCheckNumber",
    "to",
    "up",
}


def check_monitor_span_query_request_fields_item(value: str) -> MonitorSpanQueryRequestFieldsItem:
    if value in MONITOR_SPAN_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MONITOR_SPAN_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
