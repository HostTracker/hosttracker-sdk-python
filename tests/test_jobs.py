"""``wait_for_job`` - poll to a terminal state, honouring the server's pacing."""

from __future__ import annotations

import httpx
import pytest

from hosttracker import CODE_TIMEOUT, HostTrackerError

from .conftest import problem

JOB_ID = "55555555-5555-5555-5555-555555555555"


def job(state: str, **extra) -> dict:
    doc = {
        "id": JOB_ID,
        "kind": "monitor.bulkCreate",
        "state": state,
        "cancelRequested": False,
        "created": 1735689600,
        "expiresAt": 1735776000,
        "hasMore": False,
        "resumedCount": 0,
    }
    doc.update(extra)
    return doc


def _script(states: list[tuple[str, dict[str, str]]]):
    """Answer each poll with the next (state, headers) pair."""
    remaining = list(states)

    def handler(request: httpx.Request) -> httpx.Response:
        state, headers = remaining.pop(0)
        return httpx.Response(200, json=job(state), headers=headers)

    return handler


@pytest.mark.parametrize("terminal", ["succeeded", "partial", "failed", "cancelled"])
def test_returns_on_every_terminal_state(make_client, recorder, sleeps, terminal):
    ht = make_client(_script([("queued", {"Retry-After": "3"}), (terminal, {})]))
    result = ht.wait_for_job(JOB_ID)
    assert result.state == terminal
    assert len(recorder) == 2


def test_partial_is_not_an_error(make_client, sleeps):
    """A batch that ran to the end with some rows failed is a SUCCESS to the SDK."""
    ht = make_client(_script([("partial", {})]))
    result = ht.wait_for_job(JOB_ID)
    assert result.state == "partial"


def test_interrupted_is_returned_for_the_caller_to_resume(make_client, recorder, sleeps):
    """`interrupted` is NOT terminal, but spinning on it would never end."""
    ht = make_client(_script([("running", {"Retry-After": "2"}), ("interrupted", {})]))
    result = ht.wait_for_job(JOB_ID)
    assert result.state == "interrupted"
    assert len(recorder) == 2


def test_retry_after_paces_the_polls(make_client, sleeps):
    ht = make_client(
        _script(
            [
                ("queued", {"Retry-After": "5"}),
                ("running", {"Retry-After": "10"}),
                ("succeeded", {}),
            ]
        )
    )
    ht.wait_for_job(JOB_ID)
    assert sleeps == [5.0, 10.0]


def test_missing_retry_after_falls_back_to_a_fixed_interval(make_client, sleeps):
    ht = make_client(_script([("running", {}), ("succeeded", {})]))
    ht.wait_for_job(JOB_ID)
    assert sleeps == [2.0]


def test_poll_interval_overrides_the_server_pacing(make_client, sleeps):
    ht = make_client(_script([("running", {"Retry-After": "30"}), ("succeeded", {})]))
    ht.wait_for_job(JOB_ID, poll_interval=0.25)
    assert sleeps == [0.25]


def test_timeout_raises_with_the_last_known_state(make_client, monkeypatch):
    """The deadline is client-side; the job itself keeps running server-side."""
    clock = {"t": 0.0}
    monkeypatch.setattr("hosttracker.jobs.time.monotonic", lambda: clock["t"])

    def sleeper(seconds: float) -> None:
        clock["t"] += seconds

    monkeypatch.setattr("time.sleep", sleeper)

    ht = make_client(lambda r: httpx.Response(200, json=job("running"), headers={"Retry-After": "5"}))

    with pytest.raises(HostTrackerError) as caught:
        ht.wait_for_job(JOB_ID, timeout=12)

    assert caught.value.code == CODE_TIMEOUT
    assert "running" in (caught.value.detail or "")
    assert caught.value.errors[0]["jobId"] == JOB_ID


def test_on_poll_sees_every_intermediate_view(make_client, sleeps):
    seen: list[str] = []
    ht = make_client(_script([("queued", {"Retry-After": "1"}), ("running", {"Retry-After": "1"}), ("succeeded", {})]))
    ht.wait_for_job(JOB_ID, on_poll=lambda j: seen.append(j.state))
    assert seen == ["queued", "running", "succeeded"]


def test_a_failing_poll_still_raises_the_problem(make_client, sleeps):
    ht = make_client(
        lambda r: httpx.Response(
            403, json=problem("missing_scope", 403), headers={"content-type": "application/problem+json"}
        ),
        max_retries=0,
    )
    with pytest.raises(HostTrackerError) as caught:
        ht.wait_for_job(JOB_ID)
    assert caught.value.code == "missing_scope"


async def test_async_wait_for_job(make_async_client, recorder, sleeps):
    ht = make_async_client(_script([("running", {"Retry-After": "4"}), ("succeeded", {})]))
    result = await ht.wait_for_job(JOB_ID)
    assert result.state == "succeeded"
    assert sleeps == [4.0]
    await ht.aclose()
