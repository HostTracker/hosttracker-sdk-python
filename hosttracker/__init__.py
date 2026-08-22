"""Official Python SDK for the HostTracker API v2.

::

    from hosttracker import HostTracker

    with HostTracker(token="...") as ht:
        for monitor in ht.paginate(ht.monitors.list_monitor, limit=100):
            print(monitor.name, monitor.state)

The package is two layers. ``hosttracker._generated`` is produced from the published
OpenAPI document by ``scripts/regen.sh`` and is never edited by hand; everything else -
the client, the error type, paging, jobs, instant checks, webhook verification - is
hand-written and stable across regenerations.

Importing this module is cheap: the generated models load lazily, on the first call
that reaches the API.
"""

from __future__ import annotations

from ._transport import HtAsyncTransport, HtTransport, RequestPolicy, idempotency_key
from ._version import __version__
from .checks import arun_check, run_check
from .client import DEFAULT_BASE_URL, TAGS, AsyncHostTracker, HostTracker
from .errors import (
    CODE_HTTP_ERROR,
    CODE_NETWORK_ERROR,
    CODE_TIMEOUT,
    HostTrackerError,
    RateLimit,
    ResponseMeta,
)
from .jobs import TERMINAL_JOB_STATES, await_for_job, wait_for_job
from .paging import apages, apaginate, pages, paginate
from .timestamps import from_datetime, to_datetime
from .webhooks import (
    WEBHOOK_EVENT_MODELS,
    WebhookEvent,
    parse_webhook_event,
    verify_webhook_signature,
)

__all__ = [
    "CODE_HTTP_ERROR",
    "CODE_NETWORK_ERROR",
    "CODE_TIMEOUT",
    "DEFAULT_BASE_URL",
    "TAGS",
    "TERMINAL_JOB_STATES",
    "WEBHOOK_EVENT_MODELS",
    "AsyncHostTracker",
    "HostTracker",
    "HostTrackerError",
    "HtAsyncTransport",
    "HtTransport",
    "RateLimit",
    "RequestPolicy",
    "ResponseMeta",
    "WebhookEvent",
    "__version__",
    "apages",
    "apaginate",
    "arun_check",
    "await_for_job",
    "from_datetime",
    "idempotency_key",
    "pages",
    "paginate",
    "parse_webhook_event",
    "run_check",
    "to_datetime",
    "verify_webhook_signature",
    "wait_for_job",
]
