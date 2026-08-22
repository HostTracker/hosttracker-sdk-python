"""`import hosttracker` must stay cheap.

The generated `models/__init__` imports ~1050 model modules, so the helpers import the
generated packages inside their functions instead. This test keeps it that way.
"""

from __future__ import annotations

import subprocess
import sys


def test_importing_the_package_does_not_load_the_generated_models():
    script = (
        "import sys, hosttracker;print(len([m for m in sys.modules if m.startswith('hosttracker._generated.models.')]))"
    )
    loaded = int(subprocess.run([sys.executable, "-c", script], capture_output=True, text=True, check=True).stdout)
    assert loaded == 0


def test_the_public_surface_is_importable_without_the_generated_models():
    script = (
        "from hosttracker import ("
        "HostTracker, AsyncHostTracker, HostTrackerError, ResponseMeta, RateLimit,"
        "paginate, pages, apaginate, apages, wait_for_job, await_for_job, run_check, arun_check,"
        "verify_webhook_signature, parse_webhook_event, WebhookEvent,"
        "to_datetime, from_datetime, idempotency_key, HtTransport, HtAsyncTransport, RequestPolicy,"
        "DEFAULT_BASE_URL, TAGS, TERMINAL_JOB_STATES, WEBHOOK_EVENT_MODELS,"
        "CODE_HTTP_ERROR, CODE_NETWORK_ERROR, CODE_TIMEOUT, __version__);"
        "print('ok')"
    )
    result = subprocess.run([sys.executable, "-c", script], capture_output=True, text=True, check=True)
    assert result.stdout.strip() == "ok"
