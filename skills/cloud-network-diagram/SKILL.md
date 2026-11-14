---
name: cloud-network-diagram
description: Use when asked for a cloud architecture, network, traffic-flow, IP-plan or route-table diagram (draw.io). Builds pages from a script in a fixed house style, then lints and reviews. Needs drawio-skill and draw-io.
---
# Cloud and network diagrams

Needs `drawio-skill` (file format, export) and `draw-io` (lint); pins and install lines in `references/sources.md`. Where they differ on style, this skill wins.
Build with `scripts/drawlib.py`, starting from `scripts/example.py`. Keep `<name>.py`, `.drawio`, `.png` next to the source doc.

## Before drawing
- One page = one question, one reader. Title is the subject, subtitle is the answer in one sentence. A second question is a second page.
- Layers, one page each: overview (containment), IP plan, flows, route tables, temporary paths.
- Facts only from live data, state or the source doc; unknown is `<UNKNOWN>`. Mark tested vs untested (untested = grey dashed). Header tag: `As built` or `Proposal`, date, source doc.

## Layout
- Containment mirrors reality: account > region > VPC (`name · CIDR`) > subnet > resource.
- Flow left to right, one row per path; align card centres so edges are straight, none crossing.
- Card: bold `name · IP`, then one or two muted lines (route, rule, port). Detail goes in the doc.
- Blockers and revert steps: red cards where they apply.
- At most ~10 cards per zone, else split. No empty half-pages.

## Style
- Colour carries meaning (card kinds in `CARD`), never decoration. Solid = built, dashed = temporary or planned; thick = tunnel or traffic path.
- Edge labels: protocol or relation only, in the gutter (60 px or more free each side), never on a card.
- Fonts, colours and icons are set in `drawlib.py`. The legend lists only styles used on that page.

## Review (required)
1. Generate from the script; never hand-edit the XML.
2. Export SVG, run `check-drawio-svg-overlaps.mjs` from `draw-io`; it must print `OK` (on stderr). Fix every issue, delete the `.svg`.
3. Export PNG per page and look: answerable in 10 seconds? Crossings, overlaps, labels on cards, tiny text, empty areas, unsourced facts: fix and re-export.
4. Commit `.py`, `.drawio`, `.png`; not the `.svg`.
