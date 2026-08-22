from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_settings_net_attached_checks import MonitorSettingsNetAttachedChecks


T = TypeVar("T", bound="TCPPortCheckSettings")


@_attrs_define
class TCPPortCheckSettings:
    """Opens a TCP connection to a host:port, optionally negotiating TLS and matching a banner pattern - for FTP, SMTP and
    other network-faced protocols.

    """

    pattern: str | Unset = UNSET
    """ Text expected in the banner the port returns. """
    ssl: bool | Unset = False
    """ Negotiate TLS on the connection. This is also what an sslExp monitor is under the hood - a port check with
    TLS and certificate-expiry watching. """
    dns: list[str] | Unset = UNSET
    """ Resolver IPs to use instead of the agent's own. """
    public_dns: int | Unset = UNSET
    """ Use public-DNS-filtered locations. """
    expected_dns: list[str] | Unset = UNSET
    """ Resolver IPs the lookup is expected to come from. """
    expected_ips: list[str] | Unset = UNSET
    """ IPs the host is expected to resolve to. """
    require_valid_chain: bool | Unset = False
    """ Fail the check unless the server presents a complete, trusted certificate chain - an expired, self-signed,
    name-mismatched or mis-chained certificate fails. Off by default, which is why a self-signed host is reachable
    until this is switched on. Sold by the package's SSL-policy entitlement. """
    check_revocation: bool | Unset = False
    """ Fail the check when the certificate has been revoked by its authority, verified online (CRL/OCSP) during the
    handshake. Sold SEPARATELY: the package needs the revocation entitlement on top of the SSL-policy one, and a
    write that turns it on without both is refused with package_limit. """
    require_strong_tls: bool | Unset = False
    """ Fail the check unless the connection negotiates TLS 1.2 or newer - a server that only offers the deprecated
    TLS 1.0/1.1 or SSL protocols fails. Sold by the package's SSL-policy entitlement. """
    block_weak_ciphers: bool | Unset = False
    """ Fail the check when the negotiated cipher suite is 128-bit or weaker. Sold by the package's SSL-policy
    entitlement. """
    cert_watch_days: list[int] | Unset = UNSET
    """ Days-before-expiry thresholds for the served certificate. At most 8 entries, each in [1, 3650]. """
    attached: MonitorSettingsNetAttachedChecks | Unset = UNSET
    """ Sub-checks attachable to a Ping or Port monitor. """

    def to_dict(self) -> dict[str, Any]:
        pattern = self.pattern

        ssl = self.ssl

        dns: list[str] | Unset = UNSET
        if not isinstance(self.dns, Unset):
            dns = self.dns

        public_dns = self.public_dns

        expected_dns: list[str] | Unset = UNSET
        if not isinstance(self.expected_dns, Unset):
            expected_dns = self.expected_dns

        expected_ips: list[str] | Unset = UNSET
        if not isinstance(self.expected_ips, Unset):
            expected_ips = self.expected_ips

        require_valid_chain = self.require_valid_chain

        check_revocation = self.check_revocation

        require_strong_tls = self.require_strong_tls

        block_weak_ciphers = self.block_weak_ciphers

        cert_watch_days: list[int] | Unset = UNSET
        if not isinstance(self.cert_watch_days, Unset):
            cert_watch_days = self.cert_watch_days

        attached: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attached, Unset):
            attached = self.attached.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if ssl is not UNSET:
            field_dict["ssl"] = ssl
        if dns is not UNSET:
            field_dict["dns"] = dns
        if public_dns is not UNSET:
            field_dict["publicDns"] = public_dns
        if expected_dns is not UNSET:
            field_dict["expectedDns"] = expected_dns
        if expected_ips is not UNSET:
            field_dict["expectedIps"] = expected_ips
        if require_valid_chain is not UNSET:
            field_dict["requireValidChain"] = require_valid_chain
        if check_revocation is not UNSET:
            field_dict["checkRevocation"] = check_revocation
        if require_strong_tls is not UNSET:
            field_dict["requireStrongTls"] = require_strong_tls
        if block_weak_ciphers is not UNSET:
            field_dict["blockWeakCiphers"] = block_weak_ciphers
        if cert_watch_days is not UNSET:
            field_dict["certWatchDays"] = cert_watch_days
        if attached is not UNSET:
            field_dict["attached"] = attached

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_settings_net_attached_checks import MonitorSettingsNetAttachedChecks

        d = dict(src_dict)
        pattern = d.pop("pattern", UNSET)

        ssl = d.pop("ssl", UNSET)

        dns = cast(list[str], d.pop("dns", UNSET))

        public_dns = d.pop("publicDns", UNSET)

        expected_dns = cast(list[str], d.pop("expectedDns", UNSET))

        expected_ips = cast(list[str], d.pop("expectedIps", UNSET))

        require_valid_chain = d.pop("requireValidChain", UNSET)

        check_revocation = d.pop("checkRevocation", UNSET)

        require_strong_tls = d.pop("requireStrongTls", UNSET)

        block_weak_ciphers = d.pop("blockWeakCiphers", UNSET)

        cert_watch_days = cast(list[int], d.pop("certWatchDays", UNSET))

        _attached = d.pop("attached", UNSET)
        attached: MonitorSettingsNetAttachedChecks | Unset
        if isinstance(_attached, Unset):
            attached = UNSET
        else:
            attached = MonitorSettingsNetAttachedChecks.from_dict(_attached)

        tcp_port_check_settings = cls(
            pattern=pattern,
            ssl=ssl,
            dns=dns,
            public_dns=public_dns,
            expected_dns=expected_dns,
            expected_ips=expected_ips,
            require_valid_chain=require_valid_chain,
            check_revocation=check_revocation,
            require_strong_tls=require_strong_tls,
            block_weak_ciphers=block_weak_ciphers,
            cert_watch_days=cert_watch_days,
            attached=attached,
        )

        return tcp_port_check_settings
