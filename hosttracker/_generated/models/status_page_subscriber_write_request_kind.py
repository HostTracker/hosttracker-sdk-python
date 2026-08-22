from typing import Literal

StatusPageSubscriberWriteRequestKind = Literal["slack", "teams", "webhook"]

STATUS_PAGE_SUBSCRIBER_WRITE_REQUEST_KIND_VALUES: set[StatusPageSubscriberWriteRequestKind] = {
    "slack",
    "teams",
    "webhook",
}


def check_status_page_subscriber_write_request_kind(value: str) -> StatusPageSubscriberWriteRequestKind:
    if value in STATUS_PAGE_SUBSCRIBER_WRITE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_SUBSCRIBER_WRITE_REQUEST_KIND_VALUES!r}")
