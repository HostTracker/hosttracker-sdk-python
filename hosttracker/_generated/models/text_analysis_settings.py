from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.text_analysis_settings_auth_schema import (
    TextAnalysisSettingsAuthSchema,
    check_text_analysis_settings_auth_schema,
)
from ..models.text_analysis_settings_content_type import (
    TextAnalysisSettingsContentType,
    check_text_analysis_settings_content_type,
)
from ..models.text_analysis_settings_keyword_mode import (
    TextAnalysisSettingsKeywordMode,
    check_text_analysis_settings_keyword_mode,
)
from ..models.text_analysis_settings_method import TextAnalysisSettingsMethod, check_text_analysis_settings_method
from ..models.text_analysis_settings_preset import TextAnalysisSettingsPreset, check_text_analysis_settings_preset
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitor_settings_api_expectation import MonitorSettingsApiExpectation
    from ..models.monitor_settings_assert_row import MonitorSettingsAssertRow
    from ..models.monitor_settings_http_attached_checks import MonitorSettingsHttpAttachedChecks
    from ..models.monitor_settings_http_header import MonitorSettingsHttpHeader


T = TypeVar("T", bound="TextAnalysisSettings")


@_attrs_define
class TextAnalysisSettings:
    """An Http check plus response-content analysis: parse the body by content type, select a value, and assert a predicate
    on it - for third-party APIs and QA scenarios.

    """

    method: TextAnalysisSettingsMethod | Unset = "G"
    """ HTTP method, as the single letter the executor takes. An absent key means G, which is why the default is
    never written. """
    keywords: str | Unset = UNSET
    """ Comma-separated keywords matched against the response body. The whole list, not each entry, is capped at 255
    characters. """
    keyword_mode: TextAnalysisSettingsKeywordMode | Unset = "PresentAny"
    """ How `keywords` decides the verdict. Only read when `keywords` is present. """
    timeout: int | Unset = 40000
    """ Request timeout in milliseconds. The cap is 100000, not 120000: the executor's runner deadline is 110 s, so
    a longer config was silently cut short. 40000 is the default and is deliberately not written. """
    username: str | Unset = UNSET
    """ HTTP basic auth user name. """
    password: str | Unset = UNSET
    """ HTTP basic auth password. Send it again to change it. Credential. Read visibility is tiered: the monitor's
    owner and a subaccount holding the task-edit right receive the stored value; a view-only subaccount receives the
    { set, updatedAt } sentinel instead. On write, an absent field means unchanged, null clears it, and the read
    sentinel is never accepted as a literal value. """
    auth_schema: TextAnalysisSettingsAuthSchema | Unset = UNSET
    """ Authentication scheme. Only Basic is accepted. """
    headers: list[MonitorSettingsHttpHeader] | Unset = UNSET
    """ Extra request headers. Combined name+value length across all headers is capped at 1023 characters;
    `connection`, `content-length` and `date` are dropped. STORED as an array of [name, value] PAIRS, not objects -
    the server translates. """
    body: str | Unset = UNSET
    """ Raw request body. """
    post_parameters: str | Unset = UNSET
    """ Form-encoded POST parameters. """
    ignored_statuses: list[int] | Unset = UNSET
    """ HTTP status codes that must NOT fail the check. At most 20. """
    error_statuses: list[int] | Unset = UNSET
    """ HTTP status codes that MUST fail the check. At most 20. """
    follow_redirect: bool | Unset = True
    """ Follow 3xx redirects. On by default; send false explicitly to stop at the first hop. """
    max_redirects: int | Unset = 20
    """ How many redirect hops to follow before the check gives up, while `followRedirect` is on. The executor never
    follows more than 20, so 20 is both the ceiling and the default and is deliberately not written. """
    error_on_redirect: bool | Unset = False
    """ Treat a 3xx as a failure. Stored as 1/absent rather than as a boolean. """
    user_agent: str | Unset = UNSET
    """ User-Agent header. """
    accept: str | Unset = UNSET
    """ Accept header. """
    referer: str | Unset = UNSET
    """ Referer header. """
    max_size: int | Unset = 1048576
    """ Largest response body to download, in bytes. """
    dns: list[str] | Unset = UNSET
    """ Resolver IPs to use instead of the agent's own. At most 4. """
    public_dns: int | Unset = UNSET
    """ Use public-DNS-filtered locations. 0 means absent. """
    dns_no_cache: bool | Unset = UNSET
    """ Bypass the agent's DNS cache. """
    expected_dns: list[str] | Unset = UNSET
    """ Resolver IPs the lookup is expected to come from. At most 10. """
    expected_ips: list[str] | Unset = UNSET
    """ IPs the host is expected to resolve to; anything else fails the check. At most 10. """
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
    """ Days-before-expiry thresholds to alert on for the served certificate. At most 8 entries, each a whole number
    of days in [1, 3650]. This is also where the ATTACHED sslExp sub-check reads its thresholds from. """
    assert_mode: bool | Unset = False
    """ Switch the response verdict to the assertion list (AssertRuleLang). While on, the legacy response-judgment
    fields are refused - transport failures still fail the check regardless. """
    asserts: list[MonitorSettingsAssertRow] | Unset = UNSET
    """ AssertRuleLang rows - the core assertion AST the wire carries. At most 20 rows, or the account package's own
    lower cap, which is enforced per account rather than by this bound. """
    asserts_text: str | Unset = UNSET
    """ The display twin of `asserts` - the desugared rows rendered back as source text. Server-owned: the server
    writes it from `asserts`, a caller never sets it. """
    asserts_source: str | Unset = UNSET
    """ The assertion list as AssertRuleLang SOURCE TEXT - one rule per line, in the written form the language
    documents (`status eq 200`, `body.json.path("$.ok") eq true`), optionally labelled (`name: expression`). The
    sugar layer is accepted here and nowhere else. It is parsed, desugared and validated as a save would - a rule
    that does not compile is refused per line - and what is stored is the canonical `asserts` rows plus their
    `assertsText` twin, so this member is never read back. Mutually exclusive with `asserts`: send the text or the
    rows, not both. """
    preset: TextAnalysisSettingsPreset | Unset = UNSET
    """ Region-blacklist preset: the server builds the entire settings object and pins the agent pool. `bl:ru` is a
    GET check against public-DNS-filtered Russian locations whose keyword mode is ReverseAny, i.e. it passes only
    while the block banner is absent. There is no separate Russian-registry monitor type in v2 - further regions are
    additive here rather than new types. An unrecognised preset is refused with invalid_settings. """
    force_recheck: int | Unset = UNSET
    """ Server-set from the caller's `forceRecheck` role. Never accepted on write. """
    attached: MonitorSettingsHttpAttachedChecks | Unset = UNSET
    """ Sub-checks attached to this monitor. An absent member means the sub-check is off. """
    content_type: TextAnalysisSettingsContentType | Unset = UNSET
    """ How the response body is parsed before `valueSelector` runs. Required unless `assertMode` is on. Required
    when assertMode is off. """
    value_selector: str | Unset = UNSET
    """ Extracts the value to assert on. Its SYNTAX is decided by `contentType` - JSONPath, XPath or regex - and is
    compiled at validation time, so a malformed selector is a 422 rather than a runtime failure. """
    expectation: MonitorSettingsApiExpectation | Unset = UNSET
    """ An API response expectation - the pre-AssertRuleLang predicate the `api` type has always had. """

    def to_dict(self) -> dict[str, Any]:
        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method

        keywords = self.keywords

        keyword_mode: str | Unset = UNSET
        if not isinstance(self.keyword_mode, Unset):
            keyword_mode = self.keyword_mode

        timeout = self.timeout

        username = self.username

        password = self.password

        auth_schema: str | Unset = UNSET
        if not isinstance(self.auth_schema, Unset):
            auth_schema = self.auth_schema

        headers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()
                headers.append(headers_item)

        body = self.body

        post_parameters = self.post_parameters

        ignored_statuses: list[int] | Unset = UNSET
        if not isinstance(self.ignored_statuses, Unset):
            ignored_statuses = self.ignored_statuses

        error_statuses: list[int] | Unset = UNSET
        if not isinstance(self.error_statuses, Unset):
            error_statuses = self.error_statuses

        follow_redirect = self.follow_redirect

        max_redirects = self.max_redirects

        error_on_redirect = self.error_on_redirect

        user_agent = self.user_agent

        accept = self.accept

        referer = self.referer

        max_size = self.max_size

        dns: list[str] | Unset = UNSET
        if not isinstance(self.dns, Unset):
            dns = self.dns

        public_dns = self.public_dns

        dns_no_cache = self.dns_no_cache

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

        assert_mode = self.assert_mode

        asserts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.asserts, Unset):
            asserts = []
            for asserts_item_data in self.asserts:
                asserts_item = asserts_item_data.to_dict()
                asserts.append(asserts_item)

        asserts_text = self.asserts_text

        asserts_source = self.asserts_source

        preset: str | Unset = UNSET
        if not isinstance(self.preset, Unset):
            preset = self.preset

        force_recheck = self.force_recheck

        attached: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attached, Unset):
            attached = self.attached.to_dict()

        content_type: str | Unset = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type

        value_selector = self.value_selector

        expectation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expectation, Unset):
            expectation = self.expectation.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if keyword_mode is not UNSET:
            field_dict["keywordMode"] = keyword_mode
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if auth_schema is not UNSET:
            field_dict["authSchema"] = auth_schema
        if headers is not UNSET:
            field_dict["headers"] = headers
        if body is not UNSET:
            field_dict["body"] = body
        if post_parameters is not UNSET:
            field_dict["postParameters"] = post_parameters
        if ignored_statuses is not UNSET:
            field_dict["ignoredStatuses"] = ignored_statuses
        if error_statuses is not UNSET:
            field_dict["errorStatuses"] = error_statuses
        if follow_redirect is not UNSET:
            field_dict["followRedirect"] = follow_redirect
        if max_redirects is not UNSET:
            field_dict["maxRedirects"] = max_redirects
        if error_on_redirect is not UNSET:
            field_dict["errorOnRedirect"] = error_on_redirect
        if user_agent is not UNSET:
            field_dict["userAgent"] = user_agent
        if accept is not UNSET:
            field_dict["accept"] = accept
        if referer is not UNSET:
            field_dict["referer"] = referer
        if max_size is not UNSET:
            field_dict["maxSize"] = max_size
        if dns is not UNSET:
            field_dict["dns"] = dns
        if public_dns is not UNSET:
            field_dict["publicDns"] = public_dns
        if dns_no_cache is not UNSET:
            field_dict["dnsNoCache"] = dns_no_cache
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
        if assert_mode is not UNSET:
            field_dict["assertMode"] = assert_mode
        if asserts is not UNSET:
            field_dict["asserts"] = asserts
        if asserts_text is not UNSET:
            field_dict["assertsText"] = asserts_text
        if asserts_source is not UNSET:
            field_dict["assertsSource"] = asserts_source
        if preset is not UNSET:
            field_dict["preset"] = preset
        if force_recheck is not UNSET:
            field_dict["forceRecheck"] = force_recheck
        if attached is not UNSET:
            field_dict["attached"] = attached
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if value_selector is not UNSET:
            field_dict["valueSelector"] = value_selector
        if expectation is not UNSET:
            field_dict["expectation"] = expectation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitor_settings_api_expectation import MonitorSettingsApiExpectation
        from ..models.monitor_settings_assert_row import MonitorSettingsAssertRow
        from ..models.monitor_settings_http_attached_checks import MonitorSettingsHttpAttachedChecks
        from ..models.monitor_settings_http_header import MonitorSettingsHttpHeader

        d = dict(src_dict)
        _method = d.pop("method", UNSET)
        method: TextAnalysisSettingsMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = check_text_analysis_settings_method(_method)

        keywords = d.pop("keywords", UNSET)

        _keyword_mode = d.pop("keywordMode", UNSET)
        keyword_mode: TextAnalysisSettingsKeywordMode | Unset
        if isinstance(_keyword_mode, Unset):
            keyword_mode = UNSET
        else:
            keyword_mode = check_text_analysis_settings_keyword_mode(_keyword_mode)

        timeout = d.pop("timeout", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        _auth_schema = d.pop("authSchema", UNSET)
        auth_schema: TextAnalysisSettingsAuthSchema | Unset
        if isinstance(_auth_schema, Unset):
            auth_schema = UNSET
        else:
            auth_schema = check_text_analysis_settings_auth_schema(_auth_schema)

        _headers = d.pop("headers", UNSET)
        headers: list[MonitorSettingsHttpHeader] | Unset = UNSET
        if _headers is not UNSET:
            headers = []
            for headers_item_data in _headers:
                headers_item = MonitorSettingsHttpHeader.from_dict(headers_item_data)

                headers.append(headers_item)

        body = d.pop("body", UNSET)

        post_parameters = d.pop("postParameters", UNSET)

        ignored_statuses = cast(list[int], d.pop("ignoredStatuses", UNSET))

        error_statuses = cast(list[int], d.pop("errorStatuses", UNSET))

        follow_redirect = d.pop("followRedirect", UNSET)

        max_redirects = d.pop("maxRedirects", UNSET)

        error_on_redirect = d.pop("errorOnRedirect", UNSET)

        user_agent = d.pop("userAgent", UNSET)

        accept = d.pop("accept", UNSET)

        referer = d.pop("referer", UNSET)

        max_size = d.pop("maxSize", UNSET)

        dns = cast(list[str], d.pop("dns", UNSET))

        public_dns = d.pop("publicDns", UNSET)

        dns_no_cache = d.pop("dnsNoCache", UNSET)

        expected_dns = cast(list[str], d.pop("expectedDns", UNSET))

        expected_ips = cast(list[str], d.pop("expectedIps", UNSET))

        require_valid_chain = d.pop("requireValidChain", UNSET)

        check_revocation = d.pop("checkRevocation", UNSET)

        require_strong_tls = d.pop("requireStrongTls", UNSET)

        block_weak_ciphers = d.pop("blockWeakCiphers", UNSET)

        cert_watch_days = cast(list[int], d.pop("certWatchDays", UNSET))

        assert_mode = d.pop("assertMode", UNSET)

        _asserts = d.pop("asserts", UNSET)
        asserts: list[MonitorSettingsAssertRow] | Unset = UNSET
        if _asserts is not UNSET:
            asserts = []
            for asserts_item_data in _asserts:
                asserts_item = MonitorSettingsAssertRow.from_dict(asserts_item_data)

                asserts.append(asserts_item)

        asserts_text = d.pop("assertsText", UNSET)

        asserts_source = d.pop("assertsSource", UNSET)

        _preset = d.pop("preset", UNSET)
        preset: TextAnalysisSettingsPreset | Unset
        if isinstance(_preset, Unset):
            preset = UNSET
        else:
            preset = check_text_analysis_settings_preset(_preset)

        force_recheck = d.pop("forceRecheck", UNSET)

        _attached = d.pop("attached", UNSET)
        attached: MonitorSettingsHttpAttachedChecks | Unset
        if isinstance(_attached, Unset):
            attached = UNSET
        else:
            attached = MonitorSettingsHttpAttachedChecks.from_dict(_attached)

        _content_type = d.pop("contentType", UNSET)
        content_type: TextAnalysisSettingsContentType | Unset
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = check_text_analysis_settings_content_type(_content_type)

        value_selector = d.pop("valueSelector", UNSET)

        _expectation = d.pop("expectation", UNSET)
        expectation: MonitorSettingsApiExpectation | Unset
        if isinstance(_expectation, Unset):
            expectation = UNSET
        else:
            expectation = MonitorSettingsApiExpectation.from_dict(_expectation)

        text_analysis_settings = cls(
            method=method,
            keywords=keywords,
            keyword_mode=keyword_mode,
            timeout=timeout,
            username=username,
            password=password,
            auth_schema=auth_schema,
            headers=headers,
            body=body,
            post_parameters=post_parameters,
            ignored_statuses=ignored_statuses,
            error_statuses=error_statuses,
            follow_redirect=follow_redirect,
            max_redirects=max_redirects,
            error_on_redirect=error_on_redirect,
            user_agent=user_agent,
            accept=accept,
            referer=referer,
            max_size=max_size,
            dns=dns,
            public_dns=public_dns,
            dns_no_cache=dns_no_cache,
            expected_dns=expected_dns,
            expected_ips=expected_ips,
            require_valid_chain=require_valid_chain,
            check_revocation=check_revocation,
            require_strong_tls=require_strong_tls,
            block_weak_ciphers=block_weak_ciphers,
            cert_watch_days=cert_watch_days,
            assert_mode=assert_mode,
            asserts=asserts,
            asserts_text=asserts_text,
            asserts_source=asserts_source,
            preset=preset,
            force_recheck=force_recheck,
            attached=attached,
            content_type=content_type,
            value_selector=value_selector,
            expectation=expectation,
        )

        return text_analysis_settings
