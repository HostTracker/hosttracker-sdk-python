from typing import Literal

ListAgentPoolFieldsItem = Literal["agentIds", "agents", "children", "hidden", "id", "name", "parents", "priority"]

LIST_AGENT_POOL_FIELDS_ITEM_VALUES: set[ListAgentPoolFieldsItem] = {
    "agentIds",
    "agents",
    "children",
    "hidden",
    "id",
    "name",
    "parents",
    "priority",
}


def check_list_agent_pool_fields_item(value: str) -> ListAgentPoolFieldsItem:
    if value in LIST_AGENT_POOL_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_AGENT_POOL_FIELDS_ITEM_VALUES!r}")
