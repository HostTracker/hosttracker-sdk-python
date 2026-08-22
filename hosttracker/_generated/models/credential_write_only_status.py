from typing import Literal

CredentialWriteOnlyStatus = Literal[422]

CREDENTIAL_WRITE_ONLY_STATUS_VALUES: set[CredentialWriteOnlyStatus] = {
    422,
}


def check_credential_write_only_status(value: int) -> CredentialWriteOnlyStatus:
    if value in CREDENTIAL_WRITE_ONLY_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDENTIAL_WRITE_ONLY_STATUS_VALUES!r}")
