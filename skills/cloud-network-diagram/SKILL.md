---
name: cloud-network-diagram
description: Make sure to use this skill whenever the user wants to draw, update or review a cloud architecture, VPC/subnet layout, network path (VPN, peering, transit, routing), traffic flow, IP plan or route-table picture, even if they only say "diagram", "draw how X reaches Y" or point at a .drawio file. Builds pages from a script in a fixed house style, then lints and reviews.
compatibility: Needs the skills drawio-skill and draw-io (pins in references/sources.md) and the drawio, node and python3 commands.
---
# Cloud and network diagrams

`drawio-skill` covers the file format and export; `draw-io` provides the linter. Where they differ on style, this skill wins.
Build with `scripts/drawlib.py`, starting from `scripts/example.py`. Keep `<name>.py`, `.drawio`, `.png` next to the source doc.

## Before drawing
- One page, one question, one reader. A page that answers two questions is not answerable in 10 seconds. Title is the subject, subtitle is the answer in one sentence; a second question is a second page.
- Layers, one page each: overview (containment), IP plan, flows, route tables, temporary paths.
- Take facts only from live data, state or the source doc; unknown is `<UNKNOWN>`. A wrong CIDR in a polished diagram gets trusted. Draw untested things grey dashed so nobody reads them as verified. Header tag: `As built` or `Proposal`, date, source doc.

## Layout
- Containment mirrors reality (account > region > VPC `name · CIDR` > subnet > resource), so a reader can find a thing where it lives.
- Flow left to right, one row per path. Align card centres so edges are straight and never cross; crossings are what readers misread.
- Card: bold `name · IP`, then one or two muted lines (route, rule, port). Detail belongs in the doc.
- Blockers and revert steps are red cards where they apply, so the reader sees what to act on.
- About 10 cards per zone at most, else split the page. No empty half-pages.

## Style
- Colour carries meaning (card kinds in `CARD`), never decoration. Solid = built, dashed = temporary or planned, thick = tunnel or traffic path.
- Edge labels: protocol or relation only, in the gutter with 60 px or more free on each side. The linter flags labels that touch a card or arrowhead.
- Fonts, colours and icons live in `drawlib.py`. The legend lists only styles used on that page.

## Review (required)
1. Generate from the script, never hand-edit XML: a regenerated page stays reproducible and its diff stays readable.
2. Export SVG and run `check-drawio-svg-overlaps.mjs` from `draw-io`; it must print `OK` (on stderr). Fix every issue, then delete the `.svg`.
3. Export PNG per page and look, because the linter misses meaning: answerable in 10 seconds? Crossings, overlaps, labels on cards, tiny text, empty areas, unsourced facts: fix and re-export.
4. Commit `.py`, `.drawio`, `.png`; not the `.svg`.
