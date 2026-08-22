from typing import Literal

ContactActivePeriodDaysItem = Literal["Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"]

CONTACT_ACTIVE_PERIOD_DAYS_ITEM_VALUES: set[ContactActivePeriodDaysItem] = {
    "Friday",
    "Monday",
    "Saturday",
    "Sunday",
    "Thursday",
    "Tuesday",
    "Wednesday",
}


def check_contact_active_period_days_item(value: str) -> ContactActivePeriodDaysItem:
    if value in CONTACT_ACTIVE_PERIOD_DAYS_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_ACTIVE_PERIOD_DAYS_ITEM_VALUES!r}")
