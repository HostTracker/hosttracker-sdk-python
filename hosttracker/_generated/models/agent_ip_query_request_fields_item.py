from typing import Literal

AgentIpQueryRequestFieldsItem = Literal["addedAt", "country", "family", "ip"]

AGENT_IP_QUERY_REQUEST_FIELDS_ITEM_VALUES: set[AgentIpQueryRequestFieldsItem] = {
    "addedAt",
    "country",
    "family",
    "ip",
}


def check_agent_ip_query_request_fields_item(value: str) -> AgentIpQueryRequestFieldsItem:
    if value in AGENT_IP_QUERY_REQUEST_FIELDS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENT_IP_QUERY_REQUEST_FIELDS_ITEM_VALUES!r}")
