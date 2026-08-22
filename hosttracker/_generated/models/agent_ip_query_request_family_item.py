from typing import Literal

AgentIpQueryRequestFamilyItem = Literal["ipv4", "ipv6"]

AGENT_IP_QUERY_REQUEST_FAMILY_ITEM_VALUES: set[AgentIpQueryRequestFamilyItem] = {
    "ipv4",
    "ipv6",
}


def check_agent_ip_query_request_family_item(value: str) -> AgentIpQueryRequestFamilyItem:
    if value in AGENT_IP_QUERY_REQUEST_FAMILY_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AGENT_IP_QUERY_REQUEST_FAMILY_ITEM_VALUES!r}")
