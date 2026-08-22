# hosttracker

Official Python SDK for the **HostTracker API v2** - uptime, blacklist, certificate and
risk monitoring, with alerting and status pages.

Sync and async, typed end to end, built on [httpx](https://www.python-httpx.org/).
Generated from the published OpenAPI document, with a small hand-written layer that
carries the things a raw generated client cannot: one error type, a retry policy that
knows which 429 is which, automatic idempotency keys, cursor paging, job polling,
instant-check polling and webhook signature verification.

- API reference: <https://www.host-tracker.com/apidocs/v2>
- OpenAPI document: <https://github.com/HostTracker/openapi>

## Install

```bash
pip install hosttracker
```

Python 3.11 or newer.

## 60-second quick start

### 1. Mint a token

Sign in at [host-tracker.com](https://www.host-tracker.com), open your profile page and
create an API token. Tokens are long-lived JWTs (10 years by default) and carry the
scopes you tick - `monitor`, `contact`, `webhook`, `check`, `account`, … Grant only what
the integration needs.

A token is **not stored server-side**: the whole grant lives in the signed claims, so a
leaked token cannot be revoked before it expires. Treat it like a password, keep it in
an environment variable or a secret store, and restrict it to specific IPs at mint time
if you can.

```python
import os
from hosttracker import HostTracker

ht = HostTracker(token=os.environ["HT_TOKEN"])
```

### 2. List your monitors

```python
page = ht.monitors.list_monitor(limit=50)
for monitor in page.data:
    print(monitor.name, monitor.state, monitor.url)

# Or walk every page without touching cursors yourself:
for monitor in ht.paginate(ht.monitors.list_monitor, state=["down"]):
    print("DOWN:", monitor.name)
```

### 3. Create a monitor

```python
created = ht.monitors.create_monitor(
    body={
        "name": "Marketing site",
        "type": "http",
        "url": "https://www.example.com",
        "interval": 5,
        "locations": {"pools": ["allworld"]},
    }
)
print(created.id)
```

`body=` accepts a plain dict (converted to the operation's request model for you) or the
model itself - `from hosttracker.models import MonitorWriteRequest`.

### 4. Run an instant check

```python
result = ht.run_check({"url": "https://www.example.com", "type": "http"})
print(result.state)                      # "done"
for event in result.events:
    print(event.location, event.done_at)
```

`run_check` starts the check, then follows the `resultUrl` the API returns, honouring the
server's own `retryAfter` pacing, until the check is done.

### 5. Verify a webhook

```python
from hosttracker import parse_webhook_event, verify_webhook_signature

def handle(request):                                   # any web framework
    if not verify_webhook_signature(request.headers, request.body, os.environ["HT_WEBHOOK_SECRET"]):
        return 400
    event = parse_webhook_event(request.body)          # verify FIRST, then parse
    if event.event == "monitor.down":
        alert(event.data["monitor"]["name"])
    return 204
```

Pass the **raw request bytes**, never a re-serialised dict. See
[Webhooks](#webhooks) below for rotation and the second signature scheme.

## Async

Same options, same helper names, everything awaited:

```python
import asyncio
from hosttracker import AsyncHostTracker

async def main():
    async with AsyncHostTracker(token=os.environ["HT_TOKEN"]) as ht:
        page = await ht.monitors.list_monitor(limit=10)
        async for monitor in ht.paginate(ht.monitors.list_monitor):
            print(monitor.name)
        result = await ht.run_check({"url": "https://www.example.com", "type": "http"})

asyncio.run(main())
```

## Configuration

```python
ht = HostTracker(
    token=None,                                  # omit for the anonymous reference tier
    base_url="https://api2.host-tracker.com",
    timeout=30,                                  # seconds, or an httpx.Timeout
    user_agent_suffix=None,                      # appended to hosttracker-sdk-python/<version>
    max_retries=2,
    idempotency="auto",                          # or "off"
    raise_on_error=True,
    verify=True,                                 # TLS verification
    headers=None,                                # extra headers on every request
    transport=None,                              # a custom httpx.BaseTransport
    httpx_client=None,                           # a fully caller-owned httpx.Client
)
```

| Option | What it does |
| --- | --- |
| `token` | Sent as `Authorization: Bearer <token>` on every call. Omit it for the anonymous reference tier (monitor types, agent pools, contact/report/alert catalogues); every other call then answers `401 invalid_token`. There is no refresh flow. |
| `base_url` | Production by default. v2 has **no path version prefix** - a future breaking version gets a new hostname, not a `/v3` segment. |
| `max_retries` | Extra attempts for the retryable failures only (see [Retries](#retries)). `0` disables. |
| `idempotency` | `"auto"` stamps a fresh UUID `Idempotency-Key` on every POST/PATCH/PUT/DELETE that is not a `/q` read twin. That is what makes a retried write safe. Nine operations (the bulk doors, `reset_monitor_stats`, `generate_report` and the two status-page incident writers) *require* the header; the SDK supplies it there even under `"off"`, since the API refuses those without one. |
| `raise_on_error` | `True` raises `HostTrackerError` on any status ≥ 400. `False` returns the generated problem model instead; the generated parser is strict about the exact problem shape, so the exception path is the supported one. |
| `verify` | Passed to httpx. Use `verify=False` **only** against a local instance with a self-signed certificate. |
| `transport` | Slotted UNDER the SDK's policy wrapper, so retries, idempotency and error mapping still apply. This is the right hook for proxies, custom TLS, and `httpx.MockTransport` in tests. |
| `httpx_client` | Used verbatim, which means it bypasses the SDK's policy. Wrap your own transport in `hosttracker.HtTransport` if you want the policy back. |

The client is a context manager; `close()` / `aclose()` release the connection pool.

### Calling operations

`ht.<family>.<operation_id>(...)` reaches all 182 operations across the 14 families
(`hosttracker.TAGS` lists them; `dir(ht.monitors)` lists a family's operations). The
names are the OpenAPI `operationId`s in snake_case, and arguments are the spec's
parameter names in snake_case (`updated_since`, `open_stat`, `paused_last`). Names that
collide with a Python keyword or builtin get a trailing underscore - `type_`, `from_`,
`id_` - on request parameters and on model attributes alike.

Two keywords are added by the SDK on every call:

- `detailed=True` returns the response wrapper (status, headers, `parsed`) instead of the
  parsed body - this is how you read `X-Request-Id`, the `RateLimit-*` snapshot and
  `Idempotency-Replayed`, and how you get the bytes of the two binary endpoints
  (`get_report_content`, `get_monitor_result_snapshot`, whose bodies are on `.content`).
- `idempotency_key="..."` pins the key for that one call.

For full static typing, call the generated module directly:

```python
from hosttracker._generated.api.monitors import list_monitor

page = list_monitor.sync(client=ht.raw, limit=50, state=["down"])
```

Models and helper types are re-exported at the top level:

```python
from hosttracker.models import MonitorWriteRequest, MonitorView
from hosttracker.types import UNSET
```

`UNSET` is how the generated layer distinguishes "member absent" from `None` - a real
distinction on this API: an absent member leaves a value unchanged, while an explicit
`null` clears it.

## Error handling

Every failure - problem document, HTML error page from a proxy, DNS failure, timeout -
raises one `HostTrackerError`.

```python
from hosttracker import HostTrackerError

try:
    ht.monitors.create_monitor(body={"type": "http", "url": "https://example.com", "interval": 7})
except HostTrackerError as err:
    err.code          # "invalid_interval" - THE field to branch on
    err.status        # 422
    err.type          # https://api2.host-tracker.com/problems/invalid-interval
    err.title, err.detail, err.instance
    err.errors        # [{"pointer": "/interval", "value": 7, "allowed": [1, 5, 15, 30, 60]}]
    err.request_id    # X-Request-Id - quote this in support requests
    err.retry_after   # seconds, when the server named one
    err.rate_limit    # RateLimit-Policy / -Limit / -Remaining / -Reset snapshot
```

**Branch on `code`, never on `status` alone.** `rate_limited` and `quota_exceeded` are
both `429` and need opposite remediation: one is "come back in N seconds", the other is
"your window is spent - wait for the reset or upgrade". Failures that are not problem
documents carry `code = "http_error"` (an HTTP failure with a non-problem body) or
`code = "network_error"` (no answer at all, timeouts included). Unknown codes pass
through as plain strings, so a code added after your SDK release still reaches your
`else` branch instead of crashing.

The full 52-code registry is documented at
<https://www.host-tracker.com/apidocs/v2>, and every `type` URI dereferences:
`GET /problems/{code}`.

## Retries

Automatic, and deliberately narrow:

| Failure | Retried? |
| --- | --- |
| `429 rate_limited` | yes - honouring `Retry-After`, capped at 60 s |
| `429` with no problem body (the per-IP+endpoint throttle) | yes - same rule |
| `429 quota_exceeded`, or any other code on a 429 | **never** - retrying cannot help, and the SDK does not guess |
| `503 service_unavailable` **with** a `Retry-After` | yes |
| `503` with no `Retry-After`, or another code | no |
| Transport failure (DNS, reset, timeout) on `GET`/`HEAD` or a `POST …/q` read twin | yes - 200 ms · 2ⁿ full jitter, capped at 5 s |
| Transport failure on a write | no - it may already have been applied; you decide |
| Anything else (4xx, 5xx) | no |

The `timeout` you configure is per attempt, not per call.

A write is only replayed when it carries an `Idempotency-Key`, and the SAME key rides
every attempt - so the retry is the same operation, not a second one. Under the default
`idempotency="auto"` that is always the case.

## Idempotency

The API keys a stored response by `Idempotency-Key` + resolved path + body, for **24
hours**. A replay returns the stored response with `Idempotency-Replayed: true`; the same
key with a *different* body is `409 idempotency_key_conflict`.

```python
# Automatic (default): a fresh UUID per mutating call.
ht.monitors.create_monitor(body=payload)

# Your own key - safe to re-run after a crash without creating a duplicate.
ht.monitors.create_monitor(body=payload, idempotency_key=f"import-{row.id}")

# Or around a call that does not declare the header itself:
from hosttracker import idempotency_key
with idempotency_key("delete-monitor-4711"):
    ht.monitors.delete_monitor(monitor_id)

# Did the server replay a stored response?
from hosttracker import ResponseMeta
response = ht.monitors.create_monitor(body=payload, idempotency_key="import-42", detailed=True)
ResponseMeta.from_response(response).idempotency_replayed
```

Scope a key to exactly one call - reusing it for a different body is a conflict, by
design.

## Paging

Every collection answers the same envelope: `{data, nextCursor, hasMore, syncCursor?,
count?, summary?}`. Cursors are **opaque** - never build, parse or replay one under a
different `sort`.

```python
# Items across every page:
for monitor in ht.paginate(ht.monitors.list_monitor, limit=200, state=["down"]):
    ...

# Page envelopes, when you need syncCursor / count / summary:
for page in ht.pages(ht.monitors.list_monitor, limit=200, expand="count"):
    print(page.count.matched, page.sync_cursor)

# Bound the walk:
rows = list(ht.paginate(ht.monitors.list_monitor, max_pages=5))
```

`limit` defaults to 50 and caps at 500. On `/monitor`, `/contact`, `/maintenance` and
`/webhook` you can poll incrementally with `updated_since=<the previous syncCursor>` -
note there are **no tombstones**, so deletions never appear in a sync feed; watch the
`monitor.deleted` / `contact.updated` webhooks and reconcile fully now and then.

Every paged `GET` also has a `POST <path>/q` twin that takes the same parameters in a
JSON body - useful when a filter list is too long for a query string. The response is
byte-identical. `paginate()`/`pages()` drive the `GET` operations; a `/q` twin carries its
cursor inside the body, so loop that one yourself by feeding each page's `next_cursor`
into the next request body.

## Jobs

Bulk mutations answer `202 {jobId, accepted}` with a `Location` and a `Retry-After`.

```python
accepted = ht.monitors.bulk_create_monitor(body={"items": [...]}, idempotency_key="import-2025-01")
job = ht.wait_for_job(accepted.job_id, timeout=600)

if job.state == "partial":
    # SUCCESS with some rows failed - resubmit only those.
    for item in job.results:
        if item.status == "failed":
            print(item.index, item.error.code, item.error.detail)
elif job.state == "interrupted":
    # NOT terminal: the server running it died. You decide whether to continue.
    ht.jobs.resume_job(job.id)
```

`wait_for_job` polls `GET /job/{id}` (always a `200`, whatever the outcome) honouring the
server's `Retry-After`, and returns on `succeeded`, `partial`, `failed`, `cancelled` - or
`interrupted`, which is handed back rather than spun on. `partial` is **not** an error.
Pass `on_poll=` to watch progress, `poll_interval=` to override the pacing.

## Instant checks

```python
result = ht.run_check(
    {"url": "https://www.example.com", "type": "http", "pools": ["allworld"]},
    timeout=90,
    on_poll=lambda view: print(len(view.events), "locations reported"),
)
```

The check is addressed by the pair `(dbId, id)`, and `run_check` follows the `resultUrl`
the create call returned rather than building that path. The SDK follows `resultUrl` on the
configured host only. The poll answer is incremental -
`events[]` grows as fleet locations report. If the checking pipeline is down the API
refuses the create outright (`503 service_unavailable`) rather than handing back an id
that never resolves.

## Webhooks

Each delivery is signed twice, so you can use whichever scheme your stack already speaks.
`verify_webhook_signature` accepts either:

```python
verify_webhook_signature(headers, raw_body, secret)                     # either scheme
verify_webhook_signature(headers, raw_body, secret, scheme="ht")        # HT only
verify_webhook_signature(headers, raw_body, secret, scheme="standard")  # Standard Webhooks only
```

- **HT scheme** - `HT-Signature: t=<unix>,v1=<hex>[,v1=<hex>…]`. Signed string is
  `"<t>." + raw body`; the HMAC-SHA256 key is the UTF-8 bytes of the whole secret,
  `whsec_` prefix included; lowercase hex.
- **Standard Webhooks** - `webhook-id` / `webhook-timestamp` / `webhook-signature`.
  Signed string is `"<id>.<ts>.<body>"`; the key is the base64-decoded remainder after
  `whsec_`; base64 output.

Deliveries older than 300 seconds are rejected (`tolerance=` to change it, `now=` for
deterministic tests).

**Rotation.** `PATCH /webhook/{id} {"secret": {"rotate": true}}` returns the new secret
once and signs with both secrets for 24 hours - two `v1` values ride the header. Pass
both while you migrate:

```python
verify_webhook_signature(headers, raw_body, [new_secret, old_secret])
```

**Parsing.**

```python
event = parse_webhook_event(raw_body)
event.id            # "d_5b1f…" - same as the HT-Delivery header, stable across retries: your dedupe key
event.event         # "monitor.down"
event.occurred_at   # Unix seconds
event.data          # always the raw dict
event.typed         # the generated envelope model for the 15 published events, else None
```

The event vocabulary is **open** - a new event type parses with `typed=None` and a
readable `data`, never an exception.

Delivery behaviour: any 2xx counts as delivered; `410 Gone`
disables the webhook immediately; 20 consecutive failures auto-disable it (re-enable with
`PATCH {"enabled": true}`); alert-grade events retry five more times over ~2.5 hours with
the same `HT-Delivery` id, while config and job events are sent inline and not retried.

## Timestamps

Every instant on this API is an integer count of Unix **seconds**, in both directions -
never ISO-8601, never milliseconds. (A member whose name ends in `Ms` is an elapsed
duration, not an instant.)

```python
from hosttracker import from_datetime, to_datetime

to_datetime(monitor.since)                    # -> aware UTC datetime
from_datetime(datetime(2025, 1, 1, tzinfo=UTC))  # -> 1735689600
```

## Forward compatibility

The API adds things without a version bump: new endpoints, new optional request members,
new response members, new values in the open vocabularies (monitor types, webhook events,
problem codes), new response headers. To stay compatible:

- Ignore response members you do not know - the generated models keep them in
  `additional_properties`.
- Default-branch unknown enum and problem codes rather than exhaustively matching.
- Treat cursors, selection tokens and delivery ids as opaque strings.

One caveat specific to this SDK: closed value sets are generated as `Literal` string
aliases, so **requests** accept a newly added server-side value without an SDK release,
but a **response** carrying an enum value this release predates raises while parsing.
Upgrade the SDK when the API publishes a new value in a closed set, or call with
`detailed=True` and read `.content` yourself.

That caveat covers the nine vocabularies the spec now marks `x-extensible-enum` (monitor
types, contact types, alert types, report frequencies, webhook events, contact-group
events). The marker declares them open, but `openapi-python-client` does not read it, so
this SDK still types them as `Literal` and a value added server-side needs a regenerated
release before a response carrying it parses.

## Regenerating from the spec

The generated client is committed - you never need the generator to use this package. To
refresh it after a spec release:

```bash
scripts/regen.sh                                    # fetch the published document
HT_SPEC=../openapi/openapi-3.1.gen.json scripts/regen.sh   # or a local copy
```

The script pins `openapi-python-client` and `ruff`, writes `hosttracker/_generated`, and
lints the hand-written layer. Generator settings live in `openapi-python-client.yaml`.
**Generated files are never hand-edited** - everything custom belongs in the hand-written
modules beside them.

## Development

```bash
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"
.venv/bin/python -m pytest              # unit tests, fully mocked
.venv/bin/ruff check hosttracker tests
```

The live smoke run is opt-in:

```bash
HT_BASE_URL=https://api2.host-tracker.com HT_TOKEN=... .venv/bin/python -m pytest tests/test_live_smoke.py -v -s
```

## Licence

MIT - see [LICENSE](LICENSE).
