from typing import Literal

NotFoundCode = Literal["not_found"]

NOT_FOUND_CODE_VALUES: set[NotFoundCode] = {
    "not_found",
}


def check_not_found_code(value: str) -> NotFoundCode:
    if value in NOT_FOUND_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOT_FOUND_CODE_VALUES!r}")
