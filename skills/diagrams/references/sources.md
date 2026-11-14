# Sources and dependencies

`diagrams` extends public skills. It does not copy them. Install them next to it; update them from upstream.

| role | skill name when installed | upstream | licence | pinned at | install |
|---|---|---|---|---|---|
| generate, export, troubleshoot draw.io | `drawio-skill` | https://github.com/Agents365-ai/drawio-skill | MIT | `6550495129d9a42eff7e71434d15bfc9846b6202` (2026-11-10) | `bunx skills add Agents365-ai/drawio-skill@6550495129d9a42eff7e71434d15bfc9846b6202 --skill drawio-skill -a <agent>` |
| lint exported SVG (overlaps, label collisions, contrast) | `draw-io` | https://github.com/Sunwood-ai-labs/draw-io-skill | MIT | `131921b2039b02fc8ee16b23bdb951b1fbb59594` (2026-06-04) | `bunx skills add Sunwood-ai-labs/draw-io-skill@131921b2039b02fc8ee16b23bdb951b1fbb59594 --skill draw-io -a <agent>` |

Run `bunx skills add <repo> --list` to see the skill names an upstream offers. To move to a newer upstream, change the pin here, reinstall, and re-run `scripts/example.py` and `scripts/check-deps.sh`.

## What comes from where

| piece | origin |
|---|---|
| draw.io XML rules, export commands, troubleshooting, diagram types | `drawio-skill` (read its SKILL.md; this skill does not repeat it) |
| `check-drawio-svg-overlaps.mjs` | `draw-io` (Sunwood). The copy in gems-rdev-devops `.agents/skills/drawio-lint` is a byte-identical trim of it |
| decide/facts/layout/visual rules, `drawlib.py`, `example.py`, review loop | this skill (the BytePlus review set, `systems/byteplus-infra/docs/diagrams/architecture-overview.py` in gems-rdev-devops) |

## Not covered
- Excalidraw (`excalidraw-diagram`): a different format. Likely source `coleam00/excalidraw-diagram-skill` (unconfirmed; the local copy was installed as SKILL.md only, without its render script).
