# 9router setup

Snapshot of the local 9router gateway setup that fronts OpenCode. Live data lives in
`~/.9router/db/data.sqlite`; these files are the portable, secret-free copy.

## Files

- `SETUP.md` — full notes: providers, tested models, combo ordering, token savers, OpenCode integration.
- `combos.json` — all fallback combos, exported from `/api/combos`.
- `settings.json` — token saver / combo strategy settings, exported from `/api/settings`.
- `provider-nodes.json` — custom OpenAI-compatible nodes (base URLs only).
- `providers.json` — connection metadata (no `data` field, no API keys).
- `apply.sh` — idempotent restore of combos + settings over the 9router HTTP API.
- `render.py` — helper used by `apply.sh` to turn the snapshots into API payloads.

## Priority

`free → pecutopus → sumopod`. `free-coding` and `thb-free` are intentionally free-only.

## Restore

```bash
9router                       # start the gateway
./apply.sh                    # restore combos + token saver settings
```

Provider connections and API keys are **not** restored by `apply.sh` — recreate them in
the dashboard (`http://localhost:20128/dashboard`). The known nodes are:

| Prefix | Base URL | Node id |
| --- | --- | --- |
| `sp` | `https://ai.sumopod.com/v1` | `openai-compatible-chat-070a8a6c-cfe8-40c3-9a9c-69e86039fbaa` |
| `thb` | `https://tokenharbor.ai/v1` | `openai-compatible-chat-62b40173-985f-4839-96d8-44ae14644270` |
| `pecutopus` | `https://api.pecutopus.web.id/v1` | `openai-compatible-chat-pecutopus` |
| `ka` | `https://kiosapi.com/v1` | `openai-compatible-chat-5f9a377e-8dfa-4909-b2ea-016cc221b276` |
| `scloud` | `https://ai.sinarcloud.com/v1` | `openai-compatible-chat-4fbe9e47-7ff4-4dd6-b932-9a417afc1ec1` |

Built-in connections also snapshotted in `providers.json`: `openrouter` (2), `gemini-cli`
(prefix `gc`), and inactive `xiaomi-mimo`. Connection credentials are not stored.

Notes:
- Combos must use `kind: "llm"` or the dashboard hides them.
- Send `stream: true`/`false` explicitly; otherwise 9router can mis-detect empty content and fall through.
- `9router show`/`connect` read `opencode.json`, not `opencode.jsonc` — don't use `connect` to configure OpenCode here.
