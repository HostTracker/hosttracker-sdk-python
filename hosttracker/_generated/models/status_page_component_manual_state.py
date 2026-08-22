from typing import Literal

StatusPageComponentManualState = Literal["degraded", "down", "operational"]

STATUS_PAGE_COMPONENT_MANUAL_STATE_VALUES: set[StatusPageComponentManualState] = {
    "degraded",
    "down",
    "operational",
}


def check_status_page_component_manual_state(value: str) -> StatusPageComponentManualState:
    if value in STATUS_PAGE_COMPONENT_MANUAL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_COMPONENT_MANUAL_STATE_VALUES!r}")
