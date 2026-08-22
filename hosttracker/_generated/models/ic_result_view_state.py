from typing import Literal

IcResultViewState = Literal["done", "running"]

IC_RESULT_VIEW_STATE_VALUES: set[IcResultViewState] = {
    "done",
    "running",
}


def check_ic_result_view_state(value: str) -> IcResultViewState:
    if value in IC_RESULT_VIEW_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IC_RESULT_VIEW_STATE_VALUES!r}")
