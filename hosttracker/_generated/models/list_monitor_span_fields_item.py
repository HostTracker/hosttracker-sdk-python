from typing import Literal

ListMonitorSpanFieldsItem = Literal[
    "comment", "eventCount", "firstCheckNumber", "from", "incidentId", "lastCheckNumber", "to", "up"
]

LIST_MONITOR_SPAN_FIELDS_ITEM_VALUES: set[ListMonitorSpanFieldsItem] = {
    "comment",
    "eventCount",
    "firstCheckNumber",
    "from",
    "incidentId",
    "lastCheckNumber",
    "to",
    "up",
}


def check_list_monitor_span_fields_item(value: str) -> ListMonitorSpanFieldsItem:
    if value in LIST_MONITOR_SPAN_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MONITOR_SPAN_FIELDS_ITEM_VALUES!r}")
