# Tool configs

How each surface in this repo maps onto the machine. `install.sh` does the linking;
this page explains what each file actually configures.

## Kiro

`kiro/steering/*.md` → `~/.kiro/steering/`; `kiro/settings/*` → `~/.kiro/settings/`.

- `steering/ponytail.md` — "lazy senior dev" working style, `inclusion: always`, so it
  loads in every Kiro session.
- `steering/dev-server-management.md` — check the port before starting a server,
  `inclusion: fileMatch` on `server` / `start` / `dev` filenames.
- `settings/cli.json` — telemetry, autocomplete, inline suggestions and greeting off.
- `settings/permissions.yaml` — allow-all capability rule with `approve-for-me`.
- `settings/mcp.json` — only the `domscribe` MCP power; no plain MCP servers.
- `settings/sandbox.json` — sandbox disabled.

## oh-my-pi (`omp`)

`omp/config.yml` → `~/.omp/agent/config.yml`; `omp/RULES.md` → `~/.omp/agent/RULES.md`.

- Models run through Amazon Bedrock: Sonnet 5.5 default/task, Opus 5.5 for slow/plan/
  advisor, Haiku 5.5 smol. `advisor.reviewMode: agent-end`.
- Compaction threshold 250k tokens, Haiku threshold 80%, `extendedContext: true`.
- `tools.approvalMode: yolo`; LSP format-on-write and diagnostics-on-edit on; autolearn
  and checkpoint on; GitHub integration on; `generate_image` off.
- `RULES.md` — bun only (never npm/npx/yarn/pnpm), docs and replies in English and
  minimal, no CI pipelines, Zod (not TypeBox) in Elysia.
- Profiles are `--config` overlays that share sessions and memory with plain `omp`:
  - `profiles/lite.yml` — cheap: no Opus, advisor off.
  - `profiles/pro.yml` — quality first: Opus for default, plan and advisor.
  - Loaded from `omp/aliases.zsh` as `omp-lite` / `omp-pro`.

## OpenCode

`opencode/opencode.jsonc` and `opencode/AGENTS.md` → `~/.config/opencode/`;
`opencode/agents/*.md` → `~/.config/opencode/agents/`.

- Default model `9r/free-coding`. Provider `9r` → `http://localhost:20128/v1` (the
  9router gateway), key read from `{file:~/.secrets/9router-key}`.
- Six combo models declared under `9r`: `free-coding`, `thb-free`, `daily-coding`,
  `fast-cheap`, `reasoning-coding`, `vision-coding`. Declared limits equal the smallest
  real cap of any member in the combo (see `9router/README.md`).
- A direct `sp` (Sumopod) provider is also declared, intentionally.
- Subagents: `scout` (read-only search, `9r/fast-cheap`) and `reviewer` (read-only
  review, `9r/reasoning-coding`). Both deny edit and subagent calls.
- `AGENTS.md` — working rules: run it before claiming it works, smallest working diff,
  never commit/push unless asked this turn, reply in the language the user writes in.
- `9router show`/`connect` read `opencode.json`, not `opencode.jsonc` — don't use them
  to configure OpenCode here.

## Claude Code

`claude/settings.json` is **copied/merged by hand**, not symlinked, because Orca injects
hooks/statusLine and the Bedrock token lives in the home file.

- `CLAUDE_CODE_USE_BEDROCK=1`, `AWS_REGION=us-east-1`; the token comes from
  `AWS_BEARER_TOKEN_BEDROCK` and is never stored.
- Model `us.anthropic.claude-sonnet-4-6[1m]`, `permissions.defaultMode: auto`, dark theme.

## 9router

`9router/` snapshots the local gateway whose live data is `~/.9router/db/data.sqlite`.

- `combos.json`, `settings.json`, `provider-nodes.json`, `providers.json` — secret-free
  exports from the API (no keys, no connection `data`).
- `apply.sh` + `render.py` — restore combos and settings over HTTP, matching combos by
  name so ids and dashboard state stay stable.
- `README.md` — maintain-combos workflow plus the context-limit invariant.
  `SETUP.md` — full provider/combo notes (Indonesian).

## Skills

`skills/<name>/SKILL.md` with optional `scripts/` and `references/`. Installed per
project into `.agents/skills/` via `bunx skills add <path|repo>`. `skills-lock.json`
records each installed source; `skills/public.md` is the public-skill catalog. See
`skills/README.md`.

## Evals

Checks for the skills in `skills/`:

- `static.py` — frontmatter present, name matches folder, description has a trigger
  word and fits 400 chars, body ≤ 200 lines, referenced `scripts/`/`references/` exist.
- `diagrams_run.sh` / `diagrams_score.py` — behavioral run of the diagram skills across
  three variants (`base`, `public`, `ext`), scored on the `.drawio` and exported `.png`.
