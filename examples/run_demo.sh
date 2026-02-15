#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${BASE_URL:-http://127.0.0.1:8000}"
ENDPOINT="${ENDPOINT:-/tasks/execute}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Usage:
#   ./examples/run_demo.sh                # uses task_marketing_plan.json
#   ./examples/run_demo.sh task_ops.json  # uses a different payload file inside examples/
PAYLOAD_NAME="${1:-task_marketing_plan.json}"
PAYLOAD_FILE="${SCRIPT_DIR}/${PAYLOAD_NAME}"

if [ ! -f "${PAYLOAD_FILE}" ]; then
  echo "Payload file not found: ${PAYLOAD_FILE}" >&2
  echo "Available payloads:" >&2
  ls -1 "${SCRIPT_DIR}"/*.json 2>/dev/null | xargs -n1 basename >&2 || true
  exit 1
fi

if [ ! -s "${PAYLOAD_FILE}" ]; then
  echo "Payload file is empty: ${PAYLOAD_FILE}" >&2
  exit 1
fi

curl -sS -X POST "${BASE_URL}${ENDPOINT}" \
  -H "Content-Type: application/json" \
  -d @"${PAYLOAD_FILE}" | python -m json.tool