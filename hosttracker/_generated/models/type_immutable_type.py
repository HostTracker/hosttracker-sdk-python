from typing import Literal

TypeImmutableType = Literal["https://api2.host-tracker.com/problems/type-immutable"]

TYPE_IMMUTABLE_TYPE_VALUES: set[TypeImmutableType] = {
    "https://api2.host-tracker.com/problems/type-immutable",
}


def check_type_immutable_type(value: str) -> TypeImmutableType:
    if value in TYPE_IMMUTABLE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TYPE_IMMUTABLE_TYPE_VALUES!r}")
