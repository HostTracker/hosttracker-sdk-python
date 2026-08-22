from typing import Literal

ListAgentIpFieldsItem = Literal["addedAt", "country", "family", "ip"]

LIST_AGENT_IP_FIELDS_ITEM_VALUES: set[ListAgentIpFieldsItem] = {
    "addedAt",
    "country",
    "family",
    "ip",
}


def check_list_agent_ip_fields_item(value: str) -> ListAgentIpFieldsItem:
    if value in LIST_AGENT_IP_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_AGENT_IP_FIELDS_ITEM_VALUES!r}")
