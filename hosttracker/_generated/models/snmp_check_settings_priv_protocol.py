from typing import Literal

SNMPCheckSettingsPrivProtocol = Literal["AES", "AES-128", "AES-192", "AES-256", "AES128", "AES192", "AES256", "DES"]

SNMP_CHECK_SETTINGS_PRIV_PROTOCOL_VALUES: set[SNMPCheckSettingsPrivProtocol] = {
    "AES",
    "AES-128",
    "AES-192",
    "AES-256",
    "AES128",
    "AES192",
    "AES256",
    "DES",
}


def check_snmp_check_settings_priv_protocol(value: str) -> SNMPCheckSettingsPrivProtocol:
    if value in SNMP_CHECK_SETTINGS_PRIV_PROTOCOL_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SNMP_CHECK_SETTINGS_PRIV_PROTOCOL_VALUES!r}")
