"""Polling a bulk job to its terminal state.

Every bulk mutation answers ``202 {jobId, accepted}`` with a ``Location: /job/{id}`` and
a ``Retry-After``. Poll ``GET /job/{id}`` - always a 200, whatever the outcome - until
the job stops moving. Every non-terminal poll carries a fresh ``Retry-After``; a terminal
one carries none, and that absence is the documented exit condition.
"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING, Any

import anyio

from ._generated.types import Unset
from .errors import CODE_TIMEOUT, HostTrackerError, ResponseMeta

if TYPE_CHECKING:  # pragma: no cover - typing only
    from ._generated.models import JobView
    from .client import AsyncHostTracker, HostTracker

__all__ = ["TERMINAL_JOB_STATES", "await_for_job", "wait_for_job"]

#: A job in one of these states will never change again.
TERMINAL_JOB_STATES = frozenset({"succeeded", "partial", "failed", "cancelled"})

#: NOT terminal: the server running the job died. ``POST /job/{id}/resume`` continues it,
#: skipping the items it already concluded. ``wait_for_job`` returns it for the caller
#: to decide rather than spinning on it.
INTERRUPTED = "interrupted"

DEFAULT_POLL_INTERVAL = 2.0
MAX_POLL_INTERVAL = 30.0


def _state_of(job: Any) -> str | None:
    state = getattr(job, "state", None)
    if state is None or isinstance(state, Unset):
        return None
    return str(state)


def _settled(job: Any) -> bool:
    state = _state_of(job)
    return state in TERMINAL_JOB_STATES or state == INTERRUPTED


def _next_delay(response: Any, floor: float | None) -> float:
    """Honour the server's ``Retry-After``; fall back to a modest fixed interval."""
    if floor is not None:
        return max(0.0, floor)
    retry_after = ResponseMeta.from_response(response).retry_after
    if retry_after is None:
        return DEFAULT_POLL_INTERVAL
    return min(max(retry_after, 0.0), MAX_POLL_INTERVAL)


def _timed_out(job_id: Any, job: Any, timeout: float) -> HostTrackerError:
    return HostTrackerError(
        code=CODE_TIMEOUT,
        title="Timed out waiting for job",
        detail=(
            f"job {job_id} was still in state {_state_of(job) or 'unknown'!r} "
            f"after {timeout:g}s; poll GET /job/{{id}} to keep waiting"
        ),
        errors=[{"jobId": str(job_id), "state": _state_of(job)}],
    )


def wait_for_job(
    client: HostTracker,
    job_id: Any,
    *,
    timeout: float = 300.0,
    poll_interval: float | None = None,
    on_poll: Any = None,
    **params: Any,
) -> JobView:
    """Poll ``GET /job/{id}`` until the job settles, and return the final view.

    Returns as soon as ``state`` is ``succeeded``, ``partial``, ``failed``, ``cancelled``
    - or ``interrupted``, which is NOT terminal and is handed back for the caller to
    resume. ``partial`` is a SUCCESS: the batch ran to the end and some rows failed, so
    read ``summary`` and the per-item ``results`` rather than treating it as a failure.

    Args:
        client: A :class:`~hosttracker.HostTracker`.
        job_id: The ``jobId`` from the 202 answer.
        timeout: Overall client-side deadline in seconds. On expiry a
            :class:`~hosttracker.HostTrackerError` with ``code == "timeout"`` is raised;
            the job itself keeps running server-side.
        poll_interval: Fixed seconds between polls. Omit to honour the server's
            ``Retry-After``, which is sized to the batch.
        on_poll: Optional callback invoked with each intermediate ``JobView``.
        **params: Forwarded to the operation (e.g. ``limit``/``cursor`` for the item
            receipts embedded in the view).
    """
    from ._generated.api.jobs import get_job

    deadline = time.monotonic() + timeout
    job: Any = None
    while True:
        response = get_job.sync_detailed(job_id, client=client.raw, **params)
        job = response.parsed
        if on_poll is not None:
            on_poll(job)
        if _settled(job):
            return job  # type: ignore[return-value]
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise _timed_out(job_id, job, timeout)
        time.sleep(min(_next_delay(response, poll_interval), remaining))


async def await_for_job(
    client: AsyncHostTracker,
    job_id: Any,
    *,
    timeout: float = 300.0,
    poll_interval: float | None = None,
    on_poll: Any = None,
    **params: Any,
) -> JobView:
    """Async twin of :func:`wait_for_job`."""
    from ._generated.api.jobs import get_job

    deadline = time.monotonic() + timeout
    job: Any = None
    while True:
        response = await get_job.asyncio_detailed(job_id, client=client.raw, **params)
        job = response.parsed
        if on_poll is not None:
            on_poll(job)
        if _settled(job):
            return job  # type: ignore[return-value]
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise _timed_out(job_id, job, timeout)
        await anyio.sleep(min(_next_delay(response, poll_interval), remaining))
