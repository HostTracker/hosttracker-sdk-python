from typing import Literal

PackageIntervalConflictStatus = Literal[403]

PACKAGE_INTERVAL_CONFLICT_STATUS_VALUES: set[PackageIntervalConflictStatus] = {
    403,
}


def check_package_interval_conflict_status(value: int) -> PackageIntervalConflictStatus:
    if value in PACKAGE_INTERVAL_CONFLICT_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PACKAGE_INTERVAL_CONFLICT_STATUS_VALUES!r}")
