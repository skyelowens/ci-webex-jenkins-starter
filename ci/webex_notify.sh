#!/usr/bin/env bash
set -euo pipefail
: "${WEBEX_TOKEN:?Missing WEBEX_TOKEN}"
: "${WEBEX_ROOM_ID:?Missing WEBEX_ROOM_ID}"
STATUS="${1:-UNKNOWN}"
TEXT="${2:-Build finished}"

curl -sS https://webexapis.com/v1/messages \
  -H "Authorization: Bearer ${WEBEX_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "$(jq -nc --arg roomId "$WEBEX_ROOM_ID" --arg markdown "$TEXT" '{roomId:$roomId, markdown:$markdown}')"
