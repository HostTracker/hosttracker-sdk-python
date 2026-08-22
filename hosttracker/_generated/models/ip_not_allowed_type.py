from typing import Literal

IpNotAllowedType = Literal["https://api2.host-tracker.com/problems/ip-not-allowed"]

IP_NOT_ALLOWED_TYPE_VALUES: set[IpNotAllowedType] = {
    "https://api2.host-tracker.com/problems/ip-not-allowed",
}


def check_ip_not_allowed_type(value: str) -> IpNotAllowedType:
    if value in IP_NOT_ALLOWED_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IP_NOT_ALLOWED_TYPE_VALUES!r}")
