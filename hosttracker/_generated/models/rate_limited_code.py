from typing import Literal

RateLimitedCode = Literal["rate_limited"]

RATE_LIMITED_CODE_VALUES: set[RateLimitedCode] = {
    "rate_limited",
}


def check_rate_limited_code(value: str) -> RateLimitedCode:
    if value in RATE_LIMITED_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RATE_LIMITED_CODE_VALUES!r}")
