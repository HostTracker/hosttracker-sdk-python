from typing import Literal

CredentialWriteOnlyType = Literal["https://api2.host-tracker.com/problems/credential-write-only"]

CREDENTIAL_WRITE_ONLY_TYPE_VALUES: set[CredentialWriteOnlyType] = {
    "https://api2.host-tracker.com/problems/credential-write-only",
}


def check_credential_write_only_type(value: str) -> CredentialWriteOnlyType:
    if value in CREDENTIAL_WRITE_ONLY_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDENTIAL_WRITE_ONLY_TYPE_VALUES!r}")
