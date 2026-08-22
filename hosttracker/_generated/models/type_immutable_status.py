from typing import Literal

TypeImmutableStatus = Literal[422]

TYPE_IMMUTABLE_STATUS_VALUES: set[TypeImmutableStatus] = {
    422,
}


def check_type_immutable_status(value: int) -> TypeImmutableStatus:
    if value in TYPE_IMMUTABLE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TYPE_IMMUTABLE_STATUS_VALUES!r}")
