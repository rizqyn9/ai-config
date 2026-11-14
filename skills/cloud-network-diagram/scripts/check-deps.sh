#!/usr/bin/env bash
# Verify what `cloud-network-diagram` depends on. Run from the project root. Exit 1 if anything is missing.
set -u
miss=0
for c in drawio node python3; do command -v "$c" >/dev/null || { echo "missing command: $c"; miss=1; }; done
here="$(cd "$(dirname "$0")/.." && pwd)"
for s in drawio-skill draw-io; do
  found=$(ls -d .agents/skills/$s .claude/skills/$s .kiro/skills/$s ~/.agents/skills/$s 2>/dev/null | head -1)
  [ -n "$found" ] || { echo "missing skill: $s (install line in $here/references/sources.md)"; miss=1; }
done
[ $miss = 0 ] && echo "diagrams: dependencies OK"
exit $miss
