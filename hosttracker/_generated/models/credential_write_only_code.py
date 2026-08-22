from typing import Literal

CredentialWriteOnlyCode = Literal["credential_write_only"]

CREDENTIAL_WRITE_ONLY_CODE_VALUES: set[CredentialWriteOnlyCode] = {
    "credential_write_only",
}


def check_credential_write_only_code(value: str) -> CredentialWriteOnlyCode:
    if value in CREDENTIAL_WRITE_ONLY_CODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDENTIAL_WRITE_ONLY_CODE_VALUES!r}")
