#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${BASE_URL:-http://127.0.0.1:8000}"
ENDPOINT="${ENDPOINT:-/tasks/execute}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PAYLOAD_FILE="${SCRIPT_DIR}/task_marketing_plan.json"

curl -sS -X POST "${BASE_URL}${ENDPOINT}" \
  -H "Content-Type: application/json" \
  -d @"${PAYLOAD_FILE}" | python -m json.tool