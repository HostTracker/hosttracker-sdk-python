from typing import Literal

DomainExpiringEnvelopeEvent = Literal["domain.expiring"]

DOMAIN_EXPIRING_ENVELOPE_EVENT_VALUES: set[DomainExpiringEnvelopeEvent] = {
    "domain.expiring",
}


def check_domain_expiring_envelope_event(value: str) -> DomainExpiringEnvelopeEvent:
    if value in DOMAIN_EXPIRING_ENVELOPE_EVENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOMAIN_EXPIRING_ENVELOPE_EVENT_VALUES!r}")
