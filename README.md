# ai-config

AI agent configs (Kiro, oh-my-pi, OpenCode). Repo is the source of truth.

Setup on a machine: `./install.sh` (symlinks into `~/.kiro` , `~/.omp/agent` and `~/.config/opencode`; existing files become `*.bak`).

Not tracked: generated Kiro agents, sessions, DBs, memories. Keep secrets out; use env vars.

Orca: nothing tracked. Its config is app state and generated hooks (`orca-opencode-status*` plugins are Orca-managed).
