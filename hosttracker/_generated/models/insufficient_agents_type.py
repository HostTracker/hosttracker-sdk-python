from typing import Literal

InsufficientAgentsType = Literal["https://api2.host-tracker.com/problems/insufficient-agents"]

INSUFFICIENT_AGENTS_TYPE_VALUES: set[InsufficientAgentsType] = {
    "https://api2.host-tracker.com/problems/insufficient-agents",
}


def check_insufficient_agents_type(value: str) -> InsufficientAgentsType:
    if value in INSUFFICIENT_AGENTS_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INSUFFICIENT_AGENTS_TYPE_VALUES!r}")
