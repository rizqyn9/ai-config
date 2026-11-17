# ai-config

AI agent configs (Kiro, oh-my-pi, OpenCode, Claude Code). Repo is the source of truth.

Setup on a machine: `./install.sh` (symlinks into `~/.kiro`, `~/.omp/agent`, `~/.config/opencode` and `~/.claude`; existing files become `*.bak`).

Not tracked: generated Kiro agents, sessions, DBs, memories. Keep secrets out; use env vars.

Orca: nothing tracked. Its config is app state and generated hooks (`orca-opencode-status*` plugins are Orca-managed).

Claude: `settings.json` is a sanitized copy (no Bedrock token, no Orca-injected hooks/statusLine), so it is copied or merged, not symlinked. Skills live in `~/.agents/skills` and are not tracked.

omp variants: `omp-lite` (no Opus, advisor off) and `omp-pro` (Opus default/plan/advisor) are `--config` overlays in `omp/profiles/`, loaded by `omp/aliases.zsh`. They share sessions and memory with plain `omp`; `--profile` would isolate everything instead.

Skills: none are global. Private skills live in `skills/` (see `skills/README.md`) and are installed per project with `bunx skills add`. The old global set is parked in `~/.agents/skills-disabled/` (with a list of removed symlinks).

Kirocrew: it generates `kirocrew-skill-view-*` agents that clutter Kiro IDE's agent picker. Fix: `KIROCREW_NATIVE_SKILL_PROJECTION=0` in `~/Library/LaunchAgents/dev.kirocrew.gateway.plist` (`EnvironmentVariables`), then `launchctl bootout/bootstrap gui/$(id -u) <plist>`. Re-check after Kirocrew app updates, which may rewrite the plist.

9router: `9router/` holds the local gateway setup (providers, fallback combos ordered free → pecutopus → sumopod, token savers, and a sanitized OpenCode snapshot). `9router/apply.sh` restores combos and settings over HTTP; provider API keys are intentionally not stored.
