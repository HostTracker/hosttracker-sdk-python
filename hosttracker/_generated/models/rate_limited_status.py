from typing import Literal

RateLimitedStatus = Literal[429]

RATE_LIMITED_STATUS_VALUES: set[RateLimitedStatus] = {
    429,
}


def check_rate_limited_status(value: int) -> RateLimitedStatus:
    if value in RATE_LIMITED_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RATE_LIMITED_STATUS_VALUES!r}")
