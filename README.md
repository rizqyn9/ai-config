# ai-config

Source of truth for my AI coding-agent setup. Every tool's config lives here and is
symlinked into its home location, so a change is one edit plus `./install.sh`.

Tracked: configs, steering/rules, private skills, docs, restore scripts.
Not tracked: generated agents, sessions, DBs, memories, secrets.

## Tools

| Tool | Repo path | Lands at | What it configures |
| --- | --- | --- | --- |
| Kiro | `kiro/` | `~/.kiro/{steering,settings}` | steering docs, CLI/MCP/permission settings |
| oh-my-pi (`omp`) | `omp/` | `~/.omp/agent/{config.yml,RULES.md}` | models, advisor, compaction, rules |
| OpenCode | `opencode/` | `~/.config/opencode/` | providers, combos, subagents, working rules |
| Claude Code | `claude/settings.json` | `~/.claude/settings.json` (copied) | Bedrock env, model, permissions |
| 9router gateway | `9router/` | live gateway (`~/.9router`) | provider nodes + fallback combos |
| Skills | `skills/` | per-project `.agents/skills` | private skills (see `skills/README.md`) |
| Evals | `evals/` | — | skill static + behavioral checks |

Per-tool detail: [`docs/tools.md`](docs/tools.md). Day-to-day operations:
[`docs/operations.md`](docs/operations.md).

## Quick start

```bash
./install.sh     # symlink configs into home; existing files become *.bak
```

Prereqs: `bun`, `python3`, and the CLIs you use (`opencode`, `omp`). The `9r/*` models
additionally need the 9router gateway running locally.

The `9r` provider in `opencode/opencode.jsonc` reads its key from
`~/.secrets/9router-key`, which `install.sh` writes from `$AI_9ROUTER`.

## 9router

`9router/` snapshots the local gateway: provider nodes, fallback combos ordered
**free → pecutopus → sumopod**, token-saver settings, and a secret-free OpenCode view.
`9router/apply.sh` restores combos and settings over the HTTP API; provider API keys are
never stored here. Start with [`9router/README.md`](9router/README.md) (workflow) and
[`9router/SETUP.md`](9router/SETUP.md) (full notes, Indonesian).

## Skills

Private skills live in `skills/` — one folder per skill, `SKILL.md` plus optional
`scripts/` and `references/`. Installed per project, never globally:

```bash
bunx skills add ~/workspace/rdev-space/ai-config --skill <name> -a claude-code -a kiro-cli -a omp
```

`skills-lock.json` records installed sources; `skills/public.md` is the catalog of
public skills I use. See [`skills/README.md`](skills/README.md).

## Evals

```bash
python3 evals/static.py > dist/static.json                     # skill frontmatter checks
evals/diagrams_run.sh <workdir> 2                              # behavioral diagram-skill run
python3 evals/diagrams_score.py <workdir> > dist/behavior.json # score that run
```

## Secrets

Keep secrets out of the repo; use env vars. `install.sh` turns `$AI_9ROUTER` into
`~/.secrets/9router-key` (mode 0600). `claude/settings.json` is a sanitized copy (no
Bedrock token, no Orca-injected hooks/statusLine), so it is copied or merged, not
symlinked. Caveat: `omp/aliases.zsh` currently holds live keys inline — see
[`docs/operations.md`](docs/operations.md).

## Notes

- Orca: nothing tracked here; its config is app state and generated hooks
  (`orca-opencode-status*` plugins are Orca-managed).
- Kirocrew generates `kirocrew-skill-view-*` agents that clutter the Kiro agent picker.
  Fix: `KIROCREW_NATIVE_SKILL_PROJECTION=0` in
  `~/Library/LaunchAgents/dev.kirocrew.gateway.plist` (`EnvironmentVariables`), then
  `launchctl bootout/bootstrap gui/$(id -u) <plist>`. Re-check after app updates, which
  may rewrite the plist.
- omp variants: `omp-lite` (no Opus, advisor off) and `omp-pro` (Opus default/plan/
  advisor) are `--config` overlays in `omp/profiles/`, loaded by `omp/aliases.zsh`. They
  share sessions and memory with plain `omp`; `--profile` would isolate everything instead.
