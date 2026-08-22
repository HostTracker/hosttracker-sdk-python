from typing import Literal

StatusPageSubscriberViewKind = Literal["email", "slack", "teams", "webhook"]

STATUS_PAGE_SUBSCRIBER_VIEW_KIND_VALUES: set[StatusPageSubscriberViewKind] = {
    "email",
    "slack",
    "teams",
    "webhook",
}


def check_status_page_subscriber_view_kind(value: str) -> StatusPageSubscriberViewKind:
    if value in STATUS_PAGE_SUBSCRIBER_VIEW_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_SUBSCRIBER_VIEW_KIND_VALUES!r}")
