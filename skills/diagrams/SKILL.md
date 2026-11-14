---
name: diagrams
description: Architect-style draw.io diagrams (cloud, network, flow, IP plan, route tables) built from a Python script with a house style, exported and reviewed. Use before creating, editing or reviewing any architecture or network diagram. Extends the public drawio-skill and draw-io skills; needs them installed.
---

# Diagrams: think like a cloud architect

## Requires (public skills, not copied here)
- `drawio-skill` (Agents365-ai): draw.io XML rules, export commands, troubleshooting. Read it for anything about the file format or the CLI.
- `draw-io` (Sunwood-ai-labs): the SVG overlap linter used in step 5.
Install lines, licences and pinned commits: `references/sources.md`. Check them with `scripts/check-deps.sh`.

This skill only adds a house style and templates on top. Where it is silent, follow `drawio-skill`; where they conflict on style, this skill wins.

Build with `scripts/drawlib.py` (helpers `zone`, `subnet`, `card`, `edge`, `header`, `legend`, `end_page`, `write`). Start from `scripts/example.py`. A finished page set lives next to its source doc as `<name>.py`, `<name>.drawio`, `<name>.png`.

## 1. Decide before drawing
- Who reads it and which ONE question the page answers ("how does core-dev reach GCP?"). Title is the subject, subtitle is the answer in one sentence.
- Scope to the question: only components on the path or needed to act on it. A second question is a second page.
- Plan the set as layers, one page each: overview (containment), IP plan, traffic flows, route tables, special or temporary paths.

## 2. Facts first
- Every name, CIDR, IP, port and ID comes from live data, state or the source doc. Never invent; unknown is `<UNKNOWN>`.
- Mark what was tested ("tested OK", "not reachable", "not open yet"). Untested stays dashed grey.
- Header tag: status (`As built` or `Proposal`), date, source doc. Update the diagram in the same change as its source doc.

## 3. Layout
- Containment mirrors reality: provider/account > region > VPC (`name · CIDR`) > subnet > resource. Container titles carry name, CIDR, project.
- Traffic reads left to right, source to destination, one row per path. Align card centres on the path so edges are straight: no bends, no crossings.
- Vertical steps inside a VPC (workload, route table, attachment) stack in one column.
- Cards: bold title (name · IP) plus one or two muted lines with the fact that matters (route, SG rule, NAT, port). Detail goes in the doc.
- Put what the reader must act on in the page: blockers and revert steps as red cards next to where they apply.
- Even gutters, no empty half-pages. More than ~10 cards in a zone means split the page.

## 4. Visual language
- Colour encodes meaning, never decoration. Card kinds (see `CARD` in drawlib): core white, product green tint, gateway orange tint, routed teal, temporary yellow dashed, blocked/revert red, planned grey dashed. Zone colours are per project (the BytePlus set used blue `#3370FF`, GCP green `#2E7D32`, on-prem orange `#E65100`); set them once at the top of the page script.
- Solid = built, dashed = temporary or planned. Thick lines for tunnels and the traffic path, thin for internal links. Edge labels: protocol or relation only (`OpenVPN`, `peering`), in the gutter, never on a card.
- Generic service icons (draw.io `alibaba_cloud` stencils) recoloured by card kind. Swap the `ICON` map for another stencil set.
- Text: page title 28 bold, card title 14 bold, muted lines 12 `#56657A`. Never below 12. English.
- Legend lists only the styles used on that page.

## 5. Build and review (all required)
1. Generate `.drawio` from the script, never hand-edited XML. Several pages in one file.
2. Export SVG: `drawio -x -f svg -e -o <name>.drawio.svg <name>.drawio`, then `node <draw-io skill dir>/scripts/check-drawio-svg-overlaps.mjs <name>.drawio.svg` must print `OK` (it prints to stderr). Delete the `.svg`.
3. Export PNG per page (`drawio -x -f png -s 2 -p <index> -o <name>-<n>.png <name>.drawio`) and read it as a reviewer would: can the question be answered in 10 seconds? Any crossing line, overlap, label on a card, tiny text, empty area, or fact without a source? Fix and re-export. Lint passing is not enough.
4. Commit `.py`, `.drawio`, `.png`. Not the `.svg`.

Check this skill's helpers still work: `python3 scripts/example.py /tmp/x.drawio`.
