from typing import Literal

TypeImmutableCode = Literal["type_immutable"]

TYPE_IMMUTABLE_CODE_VALUES: set[TypeImmutableCode] = {
    "type_immutable",
}


def check_type_immutable_code(value: str) -> TypeImmutableCode:
    if value in TYPE_IMMUTABLE_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TYPE_IMMUTABLE_CODE_VALUES!r}")
