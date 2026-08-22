from typing import Literal

PackageIntervalConflictCode = Literal["package_interval_conflict"]

PACKAGE_INTERVAL_CONFLICT_CODE_VALUES: set[PackageIntervalConflictCode] = {
    "package_interval_conflict",
}


def check_package_interval_conflict_code(value: str) -> PackageIntervalConflictCode:
    if value in PACKAGE_INTERVAL_CONFLICT_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PACKAGE_INTERVAL_CONFLICT_CODE_VALUES!r}")
