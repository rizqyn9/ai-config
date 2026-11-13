#!/usr/bin/env bash
# Symlink repo configs into their home locations. Existing files are moved to *.bak.
set -euo pipefail
R="$(cd "$(dirname "$0")" && pwd)"
link() { # src dst
  mkdir -p "$(dirname "$2")"
  if [ -e "$2" ] && [ ! -L "$2" ]; then mv "$2" "$2.bak"; fi
  ln -sfn "$1" "$2"; echo "$2 -> $1"
}
for f in "$R"/kiro/steering/*.md; do link "$f" ~/.kiro/steering/"$(basename "$f")"; done
for f in "$R"/kiro/settings/*;    do link "$f" ~/.kiro/settings/"$(basename "$f")"; done
link "$R/omp/config.yml" ~/.omp/agent/config.yml
link "$R/omp/RULES.md"   ~/.omp/agent/RULES.md
for f in opencode/opencode.jsonc opencode/AGENTS.md opencode/agents opencode/plugins/cbm-augment.ts opencode/skills/codebase-memory; do
  link "$R/$f" ~/.config/"$f"
done
