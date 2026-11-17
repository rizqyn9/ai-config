#!/usr/bin/env bash
# Restore 9router combos and token-saver settings from the snapshots in this folder.
# Requires a running 9router on NINE_ROUTER_URL (default http://localhost:20128).
# No API keys or secrets are stored or sent by this script.
set -euo pipefail

D="$(cd "$(dirname "$0")" && pwd)"
BASE="${NINE_ROUTER_URL:-http://localhost:20128}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

if ! curl -sf -m 5 "$BASE/api/health" >/dev/null; then
  echo "9router is not reachable at $BASE — start it first (9router)." >&2
  exit 1
fi

curl -sf "$BASE/api/combos" > "$TMP/existing.json"
python3 "$D/render.py" combos "$D/combos.json" > "$TMP/combos.tsv"
python3 "$D/render.py" settings "$D/settings.json" > "$TMP/settings.json"

# Update by name so combo IDs and dashboard state stay stable.
while IFS=$'\t' read -r name payload; do
  [ -z "$name" ] && continue
  printf '%s' "$payload" > "$TMP/body.json"
  current_id="$(python3 - "$TMP/existing.json" "$name" <<'PY'
import json, sys
data = json.load(open(sys.argv[1], encoding="utf-8"))
name = sys.argv[2]
print(next((c["id"] for c in data["combos"] if c["name"] == name), ""))
PY
)"
  if [ -n "$current_id" ]; then
    curl -sf -o /dev/null -X PUT "$BASE/api/combos/$current_id" \
      -H 'Content-Type: application/json' --data-binary @"$TMP/body.json"
    echo "updated  $name"
  else
    curl -sf -o /dev/null -X POST "$BASE/api/combos" \
      -H 'Content-Type: application/json' --data-binary @"$TMP/body.json"
    echo "created  $name"
  fi
done < "$TMP/combos.tsv"

curl -sf -o /dev/null -X PATCH "$BASE/api/settings" \
  -H 'Content-Type: application/json' --data-binary @"$TMP/settings.json"
echo "settings applied"

echo "Done. Verify: curl -s $BASE/api/combos | python3 -m json.tool"
