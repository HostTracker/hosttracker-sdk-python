from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.snmp_check_settings_auth_protocol import (
    SNMPCheckSettingsAuthProtocol,
    check_snmp_check_settings_auth_protocol,
)
from ..models.snmp_check_settings_priv_protocol import (
    SNMPCheckSettingsPrivProtocol,
    check_snmp_check_settings_priv_protocol,
)
from ..models.snmp_check_settings_security_level import (
    SNMPCheckSettingsSecurityLevel,
    check_snmp_check_settings_security_level,
)
from ..models.snmp_check_settings_verb import SNMPCheckSettingsVerb, check_snmp_check_settings_verb
from ..types import UNSET, Unset

T = TypeVar("T", bound="SNMPCheckSettings")


@_attrs_define
class SNMPCheckSettings:
    """Reads a numeric OID from network equipment - routers, switches, UPS units, printers - over SNMP v1/v2c/v3. It always
    runs from a fixed internal check network rather than the public agent fleet, so there is no location to choose -
    `locations.pools` is refused if sent; omit `locations` entirely when creating this type.

    """

    host: str
    """ The device to query. """
    oid: str
    """ The object identifier to read, in dotted-decimal form: at least two parts, every part a uint32. Symbolic
    names are not accepted. """
    port: int | Unset = 161
    """ SNMP port. 161 is the default and is deliberately not persisted, so an explicit 161 and an absent value are
    indistinguishable in storage. """
    version: int | Unset = 1
    """ SNMP version - 1, 2 (v2c) or 3. """
    verb: SNMPCheckSettingsVerb | Unset = UNSET
    """ The SNMP operation. """
    community: str | Unset = UNSET
    """ The v1/v2c community string - a shared secret. There is nothing to configure here on version 3: sending it
    alongside version 3 is refused, not silently dropped. Credential. Read visibility is tiered: the monitor's owner
    and a subaccount holding the task-edit right receive the stored value; a view-only subaccount receives the {
    set, updatedAt } sentinel instead. On write, an absent field means unchanged, null clears it, and the read
    sentinel is never accepted as a literal value. """
    security_name: str | Unset = UNSET
    """ v3 USM user name. Required when version is 3. """
    security_level: SNMPCheckSettingsSecurityLevel | Unset = UNSET
    """ v3 security level - it decides which of the key fields below are required. Matched case-insensitively.
    Required when version is 3. """
    auth_protocol: SNMPCheckSettingsAuthProtocol | Unset = UNSET
    """ v3 authentication digest. Matched case-insensitively. Required when version is 3 and securityLevel is
    authNoPriv or authPriv. """
    auth_key: str | Unset = UNSET
    """ v3 authentication key. At least 8 characters, per RFC 3414. Required when version is 3 and authentication is
    on. Credential. Read visibility is tiered: the monitor's owner and a subaccount holding the task-edit right
    receive the stored value; a view-only subaccount receives the { set, updatedAt } sentinel instead. On write, an
    absent field means unchanged, null clears it, and the read sentinel is never accepted as a literal value. """
    priv_protocol: SNMPCheckSettingsPrivProtocol | Unset = UNSET
    """ v3 privacy cipher. Matched case-insensitively. Required when version is 3 and securityLevel is authPriv. """
    priv_key: str | Unset = UNSET
    """ v3 privacy key. At least 8 characters. Required when version is 3 and securityLevel is authPriv. Credential.
    Read visibility is tiered: the monitor's owner and a subaccount holding the task-edit right receive the stored
    value; a view-only subaccount receives the { set, updatedAt } sentinel instead. On write, an absent field means
    unchanged, null clears it, and the read sentinel is never accepted as a literal value. """

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        oid = self.oid

        port = self.port

        version = self.version

        verb: str | Unset = UNSET
        if not isinstance(self.verb, Unset):
            verb = self.verb

        community = self.community

        security_name = self.security_name

        security_level: str | Unset = UNSET
        if not isinstance(self.security_level, Unset):
            security_level = self.security_level

        auth_protocol: str | Unset = UNSET
        if not isinstance(self.auth_protocol, Unset):
            auth_protocol = self.auth_protocol

        auth_key = self.auth_key

        priv_protocol: str | Unset = UNSET
        if not isinstance(self.priv_protocol, Unset):
            priv_protocol = self.priv_protocol

        priv_key = self.priv_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "host": host,
                "oid": oid,
            }
        )
        if port is not UNSET:
            field_dict["port"] = port
        if version is not UNSET:
            field_dict["version"] = version
        if verb is not UNSET:
            field_dict["verb"] = verb
        if community is not UNSET:
            field_dict["community"] = community
        if security_name is not UNSET:
            field_dict["securityName"] = security_name
        if security_level is not UNSET:
            field_dict["securityLevel"] = security_level
        if auth_protocol is not UNSET:
            field_dict["authProtocol"] = auth_protocol
        if auth_key is not UNSET:
            field_dict["authKey"] = auth_key
        if priv_protocol is not UNSET:
            field_dict["privProtocol"] = priv_protocol
        if priv_key is not UNSET:
            field_dict["privKey"] = priv_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host")

        oid = d.pop("oid")

        port = d.pop("port", UNSET)

        version = d.pop("version", UNSET)

        _verb = d.pop("verb", UNSET)
        verb: SNMPCheckSettingsVerb | Unset
        if isinstance(_verb, Unset):
            verb = UNSET
        else:
            verb = check_snmp_check_settings_verb(_verb)

        community = d.pop("community", UNSET)

        security_name = d.pop("securityName", UNSET)

        _security_level = d.pop("securityLevel", UNSET)
        security_level: SNMPCheckSettingsSecurityLevel | Unset
        if isinstance(_security_level, Unset):
            security_level = UNSET
        else:
            security_level = check_snmp_check_settings_security_level(_security_level)

        _auth_protocol = d.pop("authProtocol", UNSET)
        auth_protocol: SNMPCheckSettingsAuthProtocol | Unset
        if isinstance(_auth_protocol, Unset):
            auth_protocol = UNSET
        else:
            auth_protocol = check_snmp_check_settings_auth_protocol(_auth_protocol)

        auth_key = d.pop("authKey", UNSET)

        _priv_protocol = d.pop("privProtocol", UNSET)
        priv_protocol: SNMPCheckSettingsPrivProtocol | Unset
        if isinstance(_priv_protocol, Unset):
            priv_protocol = UNSET
        else:
            priv_protocol = check_snmp_check_settings_priv_protocol(_priv_protocol)

        priv_key = d.pop("privKey", UNSET)

        snmp_check_settings = cls(
            host=host,
            oid=oid,
            port=port,
            version=version,
            verb=verb,
            community=community,
            security_name=security_name,
            security_level=security_level,
            auth_protocol=auth_protocol,
            auth_key=auth_key,
            priv_protocol=priv_protocol,
            priv_key=priv_key,
        )

        return snmp_check_settings
