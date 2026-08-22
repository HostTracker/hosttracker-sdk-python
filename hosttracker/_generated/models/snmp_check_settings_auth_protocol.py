from typing import Literal

SNMPCheckSettingsAuthProtocol = Literal["MD5", "SHA", "SHA-1", "SHA-256", "SHA1", "SHA256"]

SNMP_CHECK_SETTINGS_AUTH_PROTOCOL_VALUES: set[SNMPCheckSettingsAuthProtocol] = {
    "MD5",
    "SHA",
    "SHA-1",
    "SHA-256",
    "SHA1",
    "SHA256",
}


def check_snmp_check_settings_auth_protocol(value: str) -> SNMPCheckSettingsAuthProtocol:
    if value in SNMP_CHECK_SETTINGS_AUTH_PROTOCOL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SNMP_CHECK_SETTINGS_AUTH_PROTOCOL_VALUES!r}")
