from typing import Literal

StatusPageComponentRowManualState = Literal["degraded", "down", "operational"]

STATUS_PAGE_COMPONENT_ROW_MANUAL_STATE_VALUES: set[StatusPageComponentRowManualState] = {
    "degraded",
    "down",
    "operational",
}


def check_status_page_component_row_manual_state(value: str) -> StatusPageComponentRowManualState:
    if value in STATUS_PAGE_COMPONENT_ROW_MANUAL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_PAGE_COMPONENT_ROW_MANUAL_STATE_VALUES!r}")
