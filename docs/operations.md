# Operations

Day-to-day commands and the manual steps no script covers.

## Install / update

```bash
./install.sh
```

Symlinks repo files into home. An existing real file is moved to `*.bak` before the
link, so the first run is safe; symlinks are replaced in place. Re-run after moving to a
new machine or adding a steering/agent file.

`install.sh` also:

- writes `~/.secrets/9router-key` (0600) from `$AI_9ROUTER` when the file is missing;
- copies `claude/settings.json`, or prints a merge note when one already exists;
- appends `source <repo>/omp/aliases.zsh` to `~/.zshrc.local` once (grep-guarded).

Manual steps it cannot do:

- set `AWS_BEARER_TOKEN_BEDROCK` for Claude Code;
- recreate 9router provider connections and keys in the dashboard
  (`http://localhost:20128/dashboard`) — `apply.sh` restores combos/settings only;
- merge `claude/settings.json` by hand when a home file already exists.

## Secrets

- `omp/aliases.zsh` is the one place provider keys are tracked on purpose: it holds live
  `AI_SUMAPOD_RDEV` and `AI_9ROUTER` values, so a fresh machine has them after a clone
  plus `source`. It is only appended to `~/.zshrc.local`, never overwritten.
- Keys go nowhere else. `9router/` snapshots stay key-free (they mirror the gateway DB),
  and `claude/settings.json` stays sanitized.
- `install.sh` writes `~/.secrets/9router-key` (0600) from `$AI_9ROUTER` when missing, so
  OpenCode needs no inline key.
- Rotating a key means editing `omp/aliases.zsh`, re-running `install.sh` to refresh
  `~/.secrets/9router-key` (delete that file first), and updating the matching 9router
  connection in the dashboard.

## 9router combos

Full workflow in `9router/README.md`. Short version: edit `9router/combos.json`, run
`9router/apply.sh`, then re-verify the live list. Declared OpenCode limits track the
smallest real cap of each combo's members.

```bash
K=$(cat ~/.secrets/9router-key)
curl -s http://localhost:20128/api/combos -H "Authorization: Bearer $K" | jq -r '.combos[].name'
opencode models | grep '^9r/'
```

## Skills

Add a skill: copy `_template`, fill `SKILL.md`, then install it into a project:

```bash
bunx skills add ~/workspace/rdev-space/ai-config --list
bunx skills add ~/workspace/rdev-space/ai-config --skill <name> -a claude-code -a kiro-cli -a omp
```

A local path is copied at install time — re-run `bunx skills update` after editing a
skill here. Commit the consuming project's `.agents/skills` and `skills-lock.json`.

## Evals

```bash
python3 evals/static.py > dist/static.json
evals/diagrams_run.sh /tmp/diag-eval 2
python3 evals/diagrams_score.py /tmp/diag-eval > dist/behavior.json
```

`diagrams_run.sh` needs `omp` and `bunx`; `diagrams_score.py` needs the `drawio` CLI and
`node`. It also pulls the upstream `drawio-skill` and `draw-io` at pinned commits.
