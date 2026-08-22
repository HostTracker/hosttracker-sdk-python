from typing import Literal

InsufficientAgentsCode = Literal["insufficient_agents"]

INSUFFICIENT_AGENTS_CODE_VALUES: set[InsufficientAgentsCode] = {
    "insufficient_agents",
}


def check_insufficient_agents_code(value: str) -> InsufficientAgentsCode:
    if value in INSUFFICIENT_AGENTS_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INSUFFICIENT_AGENTS_CODE_VALUES!r}")
