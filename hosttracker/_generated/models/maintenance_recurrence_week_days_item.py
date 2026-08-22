from typing import Literal

MaintenanceRecurrenceWeekDaysItem = Literal[
    "Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"
]

MAINTENANCE_RECURRENCE_WEEK_DAYS_ITEM_VALUES: set[MaintenanceRecurrenceWeekDaysItem] = {
    "Friday",
    "Monday",
    "Saturday",
    "Sunday",
    "Thursday",
    "Tuesday",
    "Wednesday",
}


def check_maintenance_recurrence_week_days_item(value: str) -> MaintenanceRecurrenceWeekDaysItem:
    if value in MAINTENANCE_RECURRENCE_WEEK_DAYS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MAINTENANCE_RECURRENCE_WEEK_DAYS_ITEM_VALUES!r}")
