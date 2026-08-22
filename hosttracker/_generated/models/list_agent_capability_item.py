from typing import Literal

ListAgentCapabilityItem = Literal["browser", "icmp", "internal"]

LIST_AGENT_CAPABILITY_ITEM_VALUES: set[ListAgentCapabilityItem] = {
    "browser",
    "icmp",
    "internal",
}


def check_list_agent_capability_item(value: str) -> ListAgentCapabilityItem:
    if value in LIST_AGENT_CAPABILITY_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_AGENT_CAPABILITY_ITEM_VALUES!r}")
