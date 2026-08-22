from typing import Literal

ListAgentIpFamilyItem = Literal["ipv4", "ipv6"]

LIST_AGENT_IP_FAMILY_ITEM_VALUES: set[ListAgentIpFamilyItem] = {
    "ipv4",
    "ipv6",
}


def check_list_agent_ip_family_item(value: str) -> ListAgentIpFamilyItem:
    if value in LIST_AGENT_IP_FAMILY_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_AGENT_IP_FAMILY_ITEM_VALUES!r}")
