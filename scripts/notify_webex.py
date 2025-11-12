#!/usr/bin/env python3
import sys, json, requests
if len(sys.argv) < 4:
    print("Usage: notify_webex.py <BOT_TOKEN> <ROOM_ID> <MESSAGE>", file=sys.stderr)
    sys.exit(2)
token, room_id, message = sys.argv[1:4]
url = "https://webexapis.com/v1/messages"
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
payload = {"roomId": room_id, "markdown": message}
resp = requests.post(url, headers=headers, data=json.dumps(payload))
resp.raise_for_status()
