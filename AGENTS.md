# AGENTS.md

Orientation for AI agents working **in this repo**. It is the source of truth for a set
of AI coding-agent configs that `install.sh` symlinks into the home directory.

## What is live

Edits here change real, running config. If a file is already symlinked, the next session
picks up your change immediately; otherwise it lands after `./install.sh`. Treat every
file as production config, not a draft: match the style around it and keep the diff small.

Tracked: configs, steering/rules, private skills, docs, restore scripts.
Never tracked: generated agents, sessions, DBs, memories, secrets.

## Layout

| Path | Tool | Notes |
| --- | --- | --- |
| `install.sh` | all | the only "entry point"; symlinks repo files into home |
| `kiro/` | Kiro | `steering/*.md` + `settings/*` |
| `omp/` | oh-my-pi | `config.yml`, `RULES.md`, `aliases.zsh`, `profiles/` |
| `opencode/` | OpenCode | `opencode.jsonc`, `AGENTS.md`, `agents/*.md` |
| `claude/settings.json` | Claude Code | copied/merged by hand, not symlinked |
| `9router/` | 9router gateway | secret-free snapshots + `apply.sh` restore |
| `skills/` | skills CLI | private skills + `README.md` + `public.md` catalog |
| `evals/` | skills | static + behavioral checks |
| `docs/` | — | `tools.md` (per-tool detail), `operations.md` (runbook) |

Start from [`README.md`](README.md); details in [`docs/`](docs/).

## How it fits together

- OpenCode's `9r/*` models point at the local **9router** gateway
  (`http://localhost:20128/v1`). Each `9r/*` model is a fallback combo ordered
  **free → pecutopus → sumopod**. Key comes from `~/.secrets/9router-key`.
- omp and Claude Code run on **Amazon Bedrock**. Kiro uses its own settings.
- Private skills install per project into `.agents/skills/`; `skills-lock.json` records
  the sources.

## Rules for editing

- **Changing which files link:** add the mapping to `install.sh`, not just the file.
- **Secrets:** the owner's provider keys are deliberately tracked in
  `omp/aliases.zsh` (this repo is private and personal). Do not add secrets to any other
  file, and do not strip them out of `aliases.zsh`. `install.sh` derives
  `~/.secrets/9router-key` from `$AI_9ROUTER`; the `9router/` snapshots stay key-free
  because they mirror the gateway DB, not the shell env.
- **Commits:** do not commit or push unless asked in the current turn.
- **Skills:** a new skill is `skills/<name>/SKILL.md`; keep it ≤ 200 body lines with a
  trigger word in the description, or `evals/static.py` fails.
- **9router combos:** edit `9router/combos.json`, run `9router/apply.sh`, re-verify.
  Combos must be `kind: "llm"`; declared OpenCode context limits must not exceed the
  smallest real cap of any member.

## Verify before claiming done

```bash
bash -n install.sh
python3 evals/static.py > dist/static.json      # skill frontmatter checks
K=$(cat ~/.secrets/9router-key)
curl -s http://localhost:20128/api/combos -H "Authorization: Bearer $K" | jq -r '.combos[].name'
opencode models | grep '^9r/'
```

`opencode.jsonc` is JSON-with-comments: validate it by loading it (`opencode models`),
not with a plain JSON parser.

## Gotchas

- `9router show`/`connect` read `opencode.json`, not `opencode.jsonc` — do not use them
  to configure OpenCode here.
- `9router/apply.sh` never prunes: a combo removed from the snapshot stays live — delete
  it in the 9router dashboard.
- Always send `stream` explicitly (true/false) to the gateway; omitting it makes 9router
  misread some replies as empty and fall through the combo.
- 9router reports stale context caps for custom nodes (e.g. `hy4-flash` 200k vs real
  960k); sumopod publishes real caps at `https://ai.sumopod.com/v1/models`.
