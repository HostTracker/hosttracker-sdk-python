from typing import Literal

IpNotAllowedCode = Literal["ip_not_allowed"]

IP_NOT_ALLOWED_CODE_VALUES: set[IpNotAllowedCode] = {
    "ip_not_allowed",
}


def check_ip_not_allowed_code(value: str) -> IpNotAllowedCode:
    if value in IP_NOT_ALLOWED_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IP_NOT_ALLOWED_CODE_VALUES!r}")
