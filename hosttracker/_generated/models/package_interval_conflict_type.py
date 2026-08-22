from typing import Literal

PackageIntervalConflictType = Literal["https://api2.host-tracker.com/problems/package-interval-conflict"]

PACKAGE_INTERVAL_CONFLICT_TYPE_VALUES: set[PackageIntervalConflictType] = {
    "https://api2.host-tracker.com/problems/package-interval-conflict",
}


def check_package_interval_conflict_type(value: str) -> PackageIntervalConflictType:
    if value in PACKAGE_INTERVAL_CONFLICT_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PACKAGE_INTERVAL_CONFLICT_TYPE_VALUES!r}")
