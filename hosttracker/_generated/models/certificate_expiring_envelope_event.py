from typing import Literal

CertificateExpiringEnvelopeEvent = Literal["certificate.expiring"]

CERTIFICATE_EXPIRING_ENVELOPE_EVENT_VALUES: set[CertificateExpiringEnvelopeEvent] = {
    "certificate.expiring",
}


def check_certificate_expiring_envelope_event(value: str) -> CertificateExpiringEnvelopeEvent:
    if value in CERTIFICATE_EXPIRING_ENVELOPE_EVENT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CERTIFICATE_EXPIRING_ENVELOPE_EVENT_VALUES!r}")
