from typing import Literal

IcHistoryViewState = Literal["done", "running"]

IC_HISTORY_VIEW_STATE_VALUES: set[IcHistoryViewState] = {
    "done",
    "running",
}


def check_ic_history_view_state(value: str) -> IcHistoryViewState:
    if value in IC_HISTORY_VIEW_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IC_HISTORY_VIEW_STATE_VALUES!r}")
