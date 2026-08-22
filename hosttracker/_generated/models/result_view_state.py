from typing import Literal

ResultViewState = Literal["down", "up"]

RESULT_VIEW_STATE_VALUES: set[ResultViewState] = {
    "down",
    "up",
}


def check_result_view_state(value: str) -> ResultViewState:
    if value in RESULT_VIEW_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESULT_VIEW_STATE_VALUES!r}")
