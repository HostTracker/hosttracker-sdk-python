# Changelog

All notable changes to this package are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the package follows
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The API itself versions separately: v2 is stable, additive changes never bump it, and a
breaking change would get a new hostname rather than a path prefix. A regeneration that
only adds endpoints, members or vocabulary values is a MINOR release here.

## [Unreleased]

### Changed

- Regenerated from the spec-polish revision of the OpenAPI document: same 145 paths and
  182 operations, 508 schemas. 94 shapes that used to be inline objects are now named
  components, so the generated model tree drops from 1279 modules to 1053 and the models
  a caller constructs by hand gained stable names: `MonitorLocations`, `MonitorRecheck`,
  `MonitorBulkItem`, `MonitorInlineContact`, `MonitorAlertSubscription`,
  `ContactActivePeriod`, `ContactAlertSubscription`, `JobCallback`,
  `StatusPageComponent`, `WebhookHeader`, `WebhookSecretRotate`, `ContactTypeRowPage`,
  `AlertTypeRowPage`, plus the 48 per-code problem shapes such as
  `ValidationFailedError`. The old generated names (`MonitorWriteRequestLocations`,
  `ContactBulkRequestCreateItem` and the rest of the position-derived family) are gone.
- The two per-code problem shapes whose code ends in `_error` are published as
  `InternalErrorDetail` and `UpstreamErrorDetail` (all 48 problem shapes and their `500`/`502`
  arms are generated).
- `Problem.errors[]` entries are typed `ProblemError` in the spec. `HostTrackerError.errors`
  deliberately stays a list of raw dicts, so nothing changes for callers.
- The four renamed spec tags (`MonitorTypes`, `StatusPages`, `InstantChecks`,
  `MonitoringLocations`) keep their existing SDK package names: `ht.monitor_types`,
  `ht.status_pages`, `ht.instant_checks`, `ht.monitoring_locations`.
- `IcCreateView.result_url` is now required, matching the API's guarantee that the 202
  always names the result address. `run_check()` still falls back to the `Location`
  header, and then to the spec-built path, if a deployment answers without one.
- `MonitorRecheckStrategy` no longer accepts the empty string.
- `get_monitor_result_snapshot` gained the optional `if_none_match` parameter and a `304`
  arm.

### Security

- `run_check()` / `arun_check()` take only the path and query of the server's `resultUrl`
  and always dial the client's configured `base_url`, so the bearer token cannot reach a
  foreign origin. A `resultUrl` naming a scheme other than http(s) raises
  `HostTrackerError(code="http_error")` before any request goes out.

## [0.1.0] - unreleased

First release. Generated from the HostTracker API2 v2 OpenAPI document
(145 paths, 182 operations, 508 schemas) with `openapi-python-client` 0.29.0.

### Added

- `HostTracker` and `AsyncHostTracker` clients over httpx, with every operation reachable
  as `ht.<family>.<operation_id>(...)` across the 14 published families.
- One error type, `HostTrackerError`, carrying the whole RFC 9457 problem document plus
  `request_id`, `retry_after` and the `RateLimit-*` snapshot. Non-problem HTTP failures
  and transport failures map to the same type with `code = "http_error"` / `"network_error"`.
- Retry policy: `429` other than `quota_exceeded`, `503` that named a `Retry-After`, and
  transport failures on reads. Writes are only replayed when they carry an idempotency key.
- `idempotency="auto"` (default): a fresh UUID `Idempotency-Key` on every mutating call
  that is not a `/q` read twin, reused across every retry of that call.
- `paginate()` / `pages()` (and `apaginate()` / `apages()`) over the cursor envelope.
- `wait_for_job()` honouring the server's `Retry-After`, returning on every terminal
  state plus `interrupted`.
- `run_check()` following the create response's `resultUrl` to a finished instant check.
- `verify_webhook_signature()` for both signing schemes, with secret rotation and a
  configurable replay window, and `parse_webhook_event()` returning the typed envelope
  for the 15 published events and a readable raw payload for anything newer.
- `to_datetime()` / `from_datetime()` for the Unix-seconds wire format.
- Inline type hints throughout (`py.typed`).

[Unreleased]: https://github.com/HostTracker/hosttracker-sdk-python/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/HostTracker/hosttracker-sdk-python/releases/tag/v0.1.0
