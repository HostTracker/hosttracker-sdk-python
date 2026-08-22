from typing import Literal

IpNotAllowedStatus = Literal[403]

IP_NOT_ALLOWED_STATUS_VALUES: set[IpNotAllowedStatus] = {
    403,
}


def check_ip_not_allowed_status(value: int) -> IpNotAllowedStatus:
    if value in IP_NOT_ALLOWED_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {IP_NOT_ALLOWED_STATUS_VALUES!r}")
