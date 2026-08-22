from typing import Literal

AgentPoolQueryRequestFieldsItem = Literal[
    "agentIds", "agents", "children", "hidden", "id", "name", "parents", "priority"
]

AGENT_POOL_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[AgentPoolQueryRequestFieldsItem] = {
    "agentIds",
    "agents",
    "children",
    "hidden",
    "id",
    "name",
    "parents",
    "priority",
}


def check_agent_pool_query_request_fields_item(value: str) -> AgentPoolQueryRequestFieldsItem:
    if value in AGENT_POOL_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENT_POOL_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
