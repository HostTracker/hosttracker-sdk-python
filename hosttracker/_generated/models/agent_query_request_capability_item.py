from typing import Literal

AgentQueryRequestCapabilityItem = Literal["browser", "icmp", "internal"]

AGENT_QUERY_REQUEST_CAPABILITY_ITEM_VALUES: set[AgentQueryRequestCapabilityItem] = {
    "browser",
    "icmp",
    "internal",
}


def check_agent_query_request_capability_item(value: str) -> AgentQueryRequestCapabilityItem:
    if value in AGENT_QUERY_REQUEST_CAPABILITY_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENT_QUERY_REQUEST_CAPABILITY_ITEM_VALUES!r}")
