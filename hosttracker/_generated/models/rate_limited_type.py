from typing import Literal

RateLimitedType = Literal["https://api2.host-tracker.com/problems/rate-limited"]

RATE_LIMITED_TYPE_VALUES: set[RateLimitedType] = {
    "https://api2.host-tracker.com/problems/rate-limited",
}


def check_rate_limited_type(value: str) -> RateLimitedType:
    if value in RATE_LIMITED_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RATE_LIMITED_TYPE_VALUES!r}")
