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

## Maintaining combos (workflow)

Order is always `free → pecutopus → sumopod`. Rules that keep it working:

1. **Free tier.** Only free ids: `:free` / `-free`, or a model the provider lists at all-zero price.
   Every other provider's ids must be free — this is the hard requirement. Free providers in use:
   `thb`, `scloud`, `oc`, `openrouter`.
2. **Paid tail.** `pecutopus` then `sp` only. Cheapest-capable first (flash/lite/nano), strongest last.
3. **Verify before adding.** Probe each id through the gateway and require `200` + non-empty content:

   ```bash
   K=$(cat ~/.secrets/9router-key)
   curl -s http://localhost:20128/v1/chat/completions -H "Authorization: Bearer $K" \
     -H 'Content-Type: application/json' \
     -d '{"model":"thb/deepseek-v4.1-flash:free","stream":false,"messages":[{"role":"user","content":"reply ok"}]}'
   ```

   A dead/quota id left in a combo only burns latency before fallback — drop it.
4. **Shape.** Combos must be `kind: "llm"` or the dashboard hides them. Always send `stream`
   explicitly; omitting it makes 9router misread some replies as empty and fall through.
5. **Write path.** Edit `combos.json`, run `./apply.sh` (PUT/POST by name, so ids stay stable),
   then re-check the live list below.

### Declared context limits (`opencode/opencode.jsonc`)

Invariant: **declared `context` ≤ the smallest real input cap of any member in the combo, and
declared `output` ≤ the smallest real max-output.** That ceiling is what every fallback member
honours, so the combo can't 400. Current values: `128000/32000` for every mixed chain,
`200000/32000` for `thb-free` (its smallest member is `oc/big-pickle` at 200k).

`sp` publishes real caps at `https://ai.sumopod.com/v1/models`; 9router's own numbers for custom
nodes can be stale (it reports `hy4-flash` 200k vs real 960k, `gpt-5.6-sol` 1.05M vs real 922k).
The 9router `/v1/models` list is the best source for the other nodes.

Verify caps before changing a limit:

```bash
curl -s http://localhost:20128/v1/models -H "Authorization: Bearer $(cat ~/.secrets/9router-key)" \
  | jq '.data[] | select(.id=="oc/big-pickle") | .capabilities | {contextWindow, maxOutput}'
```

### Verify

```bash
K=$(cat ~/.secrets/9router-key)
curl -s http://localhost:20128/api/combos -H "Authorization: Bearer $K" | jq -r '.combos[].name'
opencode models | grep '^9r/'                 # 6 combos wired into OpenCode
opencode run --model 9r/free-coding "reply ok"
```

### Gotchas

- `9router show`/`connect` read `opencode.json`, not `opencode.jsonc` — don't use them here.
- `apply.sh` never prunes: a combo dropped from the snapshot stays live — delete it in the dashboard.
- 9router's cost column is a name-pattern estimate, not billing — ignore it for custom nodes.

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
