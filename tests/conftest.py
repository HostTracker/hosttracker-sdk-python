"""Shared fixtures: a mocked transport, a client factory, and instant sleeps."""

from __future__ import annotations

import time
from collections.abc import Callable
from typing import Any

import anyio
import httpx
import pytest

from hosttracker import AsyncHostTracker, HostTracker

BASE_URL = "https://api2.test"
TOKEN = "test-token"

MONITOR_A = "11111111-1111-1111-1111-111111111111"
MONITOR_B = "22222222-2222-2222-2222-222222222222"
MONITOR_C = "33333333-3333-3333-3333-333333333333"


def monitor_row(monitor_id: str, name: str) -> dict[str, Any]:
    """A MonitorView with every member the schema marks required."""
    return {
        "id": monitor_id,
        "name": name,
        "enabled": True,
        "fullLog": False,
        "openStat": False,
        "since": 1735689600,
        "updated": 1735689600,
    }


def problem(code: str, status: int, **extra: Any) -> dict[str, Any]:
    """An RFC 9457 document shaped like the API's: snake_case `code`, kebab-case `type` URI."""
    doc: dict[str, Any] = {
        "type": f"https://api2.host-tracker.com/problems/{code.replace('_', '-')}",
        "title": code.replace("_", " ").title(),
        "status": status,
        "code": code,
    }
    doc.update(extra)
    return doc


PROBLEM_HEADERS = {"content-type": "application/problem+json", "x-request-id": "req-test"}


class Recorder:
    """Collects every request a mocked transport saw, in order."""

    def __init__(self) -> None:
        self.requests: list[httpx.Request] = []

    def __len__(self) -> int:
        return len(self.requests)

    @property
    def last(self) -> httpx.Request:
        return self.requests[-1]

    def idempotency_keys(self) -> list[str | None]:
        return [r.headers.get("Idempotency-Key") for r in self.requests]


@pytest.fixture
def recorder() -> Recorder:
    return Recorder()


@pytest.fixture
def make_client(recorder: Recorder) -> Callable[..., HostTracker]:
    """Build a HostTracker over a scripted mock transport."""

    def factory(handler: Callable[[httpx.Request], httpx.Response], **kwargs: Any) -> HostTracker:
        def wrapped(request: httpx.Request) -> httpx.Response:
            request.read()
            recorder.requests.append(request)
            return handler(request)

        kwargs.setdefault("token", TOKEN)
        kwargs.setdefault("base_url", BASE_URL)
        return HostTracker(transport=httpx.MockTransport(wrapped), **kwargs)

    return factory


@pytest.fixture
def make_async_client(recorder: Recorder) -> Callable[..., AsyncHostTracker]:
    def factory(handler: Callable[[httpx.Request], httpx.Response], **kwargs: Any) -> AsyncHostTracker:
        def wrapped(request: httpx.Request) -> httpx.Response:
            request.read()
            recorder.requests.append(request)
            return handler(request)

        kwargs.setdefault("token", TOKEN)
        kwargs.setdefault("base_url", BASE_URL)
        return AsyncHostTracker(transport=httpx.MockTransport(wrapped), **kwargs)

    return factory


@pytest.fixture
def sleeps(monkeypatch: pytest.MonkeyPatch) -> list[float]:
    """Make every SDK sleep instant, and record the durations it asked for."""
    recorded: list[float] = []

    def fake_sleep(seconds: float) -> None:
        recorded.append(seconds)

    async def fake_async_sleep(seconds: float) -> None:
        recorded.append(seconds)

    monkeypatch.setattr(time, "sleep", fake_sleep)
    monkeypatch.setattr(anyio, "sleep", fake_async_sleep)
    return recorded
