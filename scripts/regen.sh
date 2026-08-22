#!/usr/bin/env bash
# Regenerate hosttracker/_generated from the published OpenAPI document.
#
#   scripts/regen.sh                     # fetch the 3.1 twin from the openapi repo
#   HT_SPEC=../openapi/openapi-3.1.gen.json scripts/regen.sh
#
# The generated tree is COMMITTED - consumers must never need the generator - and is never
# hand-edited: everything custom lives in the hand-written modules beside it.
#
# Generator settings live in openapi-python-client.yaml at the repo root.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# --- pinned toolchain -------------------------------------------------------------
OPENAPI_PYTHON_CLIENT_VERSION="${OPENAPI_PYTHON_CLIENT_VERSION:-0.29.0}"
RUFF_VERSION="${RUFF_VERSION:-0.16.4}"

# --- spec source ------------------------------------------------------------------
# openapi-python-client reads OpenAPI 3.1 natively, so the 3.1 document is used as-is.
SPEC_URL="${HT_SPEC_URL:-https://raw.githubusercontent.com/HostTracker/openapi/main/openapi-3.1.gen.json}"
SPEC_LOCAL="${HT_SPEC:-}"

VENV="${HT_VENV:-$REPO_ROOT/.venv}"
PY="$VENV/bin/python"
OUT="hosttracker/_generated"

if [ ! -x "$PY" ]; then
  echo "==> creating $VENV"
  python3 -m venv "$VENV"
fi

echo "==> installing pinned generator toolchain"
"$PY" -m pip install --quiet --upgrade pip
"$PY" -m pip install --quiet \
  "openapi-python-client==${OPENAPI_PYTHON_CLIENT_VERSION}" \
  "ruff==${RUFF_VERSION}"

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

if [ -n "$SPEC_LOCAL" ]; then
  echo "==> using local spec: $SPEC_LOCAL"
  cp "$SPEC_LOCAL" "$WORK/openapi.json"
else
  echo "==> fetching spec: $SPEC_URL"
  curl -fsSL "$SPEC_URL" -o "$WORK/openapi.json"
fi

"$PY" - "$WORK/openapi.json" <<'PYCHECK'
import json, sys
doc = json.load(open(sys.argv[1]))
version = doc.get("openapi", "?")
print(f"    openapi {version}: {len(doc.get('paths', {}))} paths, "
      f"{len(doc.get('components', {}).get('schemas', {}))} schemas, "
      f"servers={[s.get('url') for s in doc.get('servers', [])]}")
if not version.startswith("3.1"):
    sys.exit(f"expected an OpenAPI 3.1 document, got {version}")
PYCHECK

echo "==> generating $OUT"
rm -rf "$OUT"
# `ruff` must be on PATH: the generator's post_hooks shell out to it by name.
PATH="$VENV/bin:$PATH" "$VENV/bin/openapi-python-client" generate \
  --path "$WORK/openapi.json" \
  --output-path "$OUT" \
  --meta none \
  --config openapi-python-client.yaml \
  --overwrite

# `--meta none` writes the package body only; hosttracker/py.typed at the top level
# already marks every subpackage as typed.

echo "==> generated:"
echo "    $(find "$OUT/api" -mindepth 1 -maxdepth 1 -type d | wc -l) operation families"
echo "    $(find "$OUT/api" -name '*.py' ! -name '__init__.py' | wc -l) operations"
echo "    $(find "$OUT/models" -name '*.py' ! -name '__init__.py' | wc -l) models"

echo "==> linting the hand-written layer"
"$VENV/bin/ruff" check hosttracker tests scripts
"$VENV/bin/ruff" format --check hosttracker tests

echo
echo "Done. Review the diff, run 'pytest', and bump CHANGELOG.md if the surface changed."
