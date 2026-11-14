# ai-config

AI agent configs (Kiro, oh-my-pi, OpenCode, Claude Code). Repo is the source of truth.

Setup on a machine: `./install.sh` (symlinks into `~/.kiro`, `~/.omp/agent`, `~/.config/opencode` and `~/.claude`; existing files become `*.bak`).

Not tracked: generated Kiro agents, sessions, DBs, memories. Keep secrets out; use env vars.

Orca: nothing tracked. Its config is app state and generated hooks (`orca-opencode-status*` plugins are Orca-managed).

Claude: `settings.json` is a sanitized copy (no Bedrock token, no Orca-injected hooks/statusLine), so it is copied or merged, not symlinked. Skills live in `~/.agents/skills` and are not tracked.

omp variants: `omp-lite` (no Opus, advisor off) and `omp-pro` (Opus default/plan/advisor) are `--config` overlays in `omp/profiles/`, loaded by `omp/aliases.zsh`. They share sessions and memory with plain `omp`; `--profile` would isolate everything instead.
