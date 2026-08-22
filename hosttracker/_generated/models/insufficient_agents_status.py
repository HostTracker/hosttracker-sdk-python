from typing import Literal

InsufficientAgentsStatus = Literal[422]

INSUFFICIENT_AGENTS_STATUS_VALUES: set[InsufficientAgentsStatus] = {
    422,
}


def check_insufficient_agents_status(value: int) -> InsufficientAgentsStatus:
    if value in INSUFFICIENT_AGENTS_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INSUFFICIENT_AGENTS_STATUS_VALUES!r}")
