from typing import Literal

ContactTemplateEvent = Literal["down", "repeatedlyDown", "up"]

CONTACT_TEMPLATE_EVENT_VALUES: set[ContactTemplateEvent] = {
    "down",
    "repeatedlyDown",
    "up",
}


def check_contact_template_event(value: str) -> ContactTemplateEvent:
    if value in CONTACT_TEMPLATE_EVENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_TEMPLATE_EVENT_VALUES!r}")
