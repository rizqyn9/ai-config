#!/usr/bin/env bash
# Behavioral eval for diagram skills. Variants: base (no skills), public (drawio-skill + draw-io, pinned upstream),
# ext (diagrams + the same two). Usage: [VARIANTS="ext"] evals/diagrams_run.sh <workdir> [reps=2]
set -euo pipefail
W="${1:?workdir}"; N="${2:-2}"; R="$(cd "$(dirname "$0")/.." && pwd)"
A=Agents365-ai/drawio-skill@6550495129d9a42eff7e71434d15bfc9846b6202
S=Sunwood-ai-labs/draw-io-skill@131921b2039b02fc8ee16b23bdb951b1fbb59594
rm -rf "$W"; mkdir -p "$W"
PROMPT='Make an architecture diagram as a draw.io file out/diagram.drawio and export each page to out/diagram-<n>.png.
Question to answer: how does the core-dev workload reach the GCP database?
Facts (use only these): BytePlus ap-southeast-3, VPC core-dev 10.20.0.0/16, subnet app 10.20.1.0/24, workload app-1 10.20.1.15. Path: Transit Router -> IPsec VPN (tested OK) -> GCP Cloud VPN in project gems-dev, VPC gems-dev 10.30.0.0/16 -> Cloud SQL postgres 10.30.5.4:5432. Status: as built, 2026-11-14, source docs/network.md.
Work without asking questions; finish all files.'
add() { (cd "$1" && bunx skills add "$2" --skill "$3" -a claude-code -y </dev/null >/dev/null 2>&1); }
for i in $(seq "$N"); do for v in ${VARIANTS:-base public ext}; do
  d="$W/$v-$i"; mkdir -p "$d/out"; git -C "$d" init -q
  [ "$v" != base ] && { add "$d" "$A" drawio-skill; add "$d" "$S" draw-io; }
  [ "$v" = ext ] && add "$d" "$R" cloud-network-diagram
  (cd "$d" && timeout 900 omp -p --no-session --model sonnet "$PROMPT" > "$d.log" 2>&1; echo "exit $?" >> "$d.log") &
done; done
wait; tail -qn1 "$W"/*.log
