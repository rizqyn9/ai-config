#!/usr/bin/env python3
"""Score the outputs of diagrams_run.sh. Usage: python3 evals/diagrams_score.py <workdir> > dist/behavior.json"""
import glob, json, os, re, subprocess, sys, xml.dom.minidom as md
W = sys.argv[1]
LINT = os.path.expanduser(os.environ.get("DRAWIO_LINT", "~/workspace/sinarmas/gems-rdev-devops/.agents/skills/drawio-lint")) + "/scripts/check-drawio-svg-overlaps.mjs"
ALLOWED = {"10.20.0.0/16", "10.20.1.0/24", "10.20.1.15", "10.30.0.0/16", "10.30.5.4", "10.30.5.4:5432"}
out = {}
for v in sorted(x for x in os.listdir(W) if os.path.isdir(os.path.join(W, x))):
    o = os.path.join(W, v, "out"); c = {}
    drawio = os.path.join(o, "diagram.drawio")
    c["drawio_exists"] = os.path.exists(drawio)
    c["generator_script"] = any(glob.glob(os.path.join(W, v, p)) for p in ("out/*.py", "*.py", "out/*.ts", "out/*.js", "out/*.mjs", "out/*.sh"))
    c["png_exported"] = bool(glob.glob(os.path.join(o, "diagram-*.png")))
    cells = []
    if c["drawio_exists"]:
        try:
            d = md.parse(drawio); cells = [x.getAttribute("value") + " " + x.getAttribute("style") for x in d.getElementsByTagName("mxCell")]
            c["well_formed"] = True
        except Exception: c["well_formed"] = False
    txt = " ".join(cells)
    sizes = [int(s) for s in re.findall(r"fontSize=(\d+)", txt)]
    c["min_font>=12"] = bool(sizes) and min(sizes) >= 12
    c["has_legend"] = "Legend" in txt
    c["has_status_tag"] = bool(re.search(r"As built", txt)) and "network.md" in txt
    c["dashed_or_color_semantics"] = "dashed=1" in txt or "fillColor=#" in txt
    found = set(re.findall(r"\b\d+\.\d+\.\d+\.\d+(?:/\d+|:\d+)?", re.sub(r"<[^>]+>", " ", txt)))
    bad = sorted(x for x in found if x not in ALLOWED and x.split(":")[0] not in ALLOWED)
    c["no_invented_addresses"] = not bad; c["invented"] = bad
    c["states_tested_ok"] = "tested" in txt.lower()
    c["card_count"] = len(re.findall(r"rounded=1", txt))
    # overlap lint via svg export
    c["overlap_lint_ok"] = None
    if c["drawio_exists"] and os.path.exists(LINT):
        svg = os.path.join(o, "_lint.drawio.svg")
        subprocess.run(["drawio", "-x", "-f", "svg", "-e", "-o", svg, drawio], capture_output=True, timeout=120)
        if os.path.exists(svg):
            p = subprocess.run(["node", LINT, svg], capture_output=True, text=True, timeout=120)
            o2 = p.stdout + p.stderr; c["overlap_lint_ok"] = "[diagram:check] OK" in o2; c["overlap_lint_out"] = o2.strip()[-200:]
            os.remove(svg)
    out[v] = c
def score(c): return sum(1 for k, x in c.items() if isinstance(x, bool) and x), sum(1 for x in c.values() if isinstance(x, bool))
for v in list(out): out[v]["score"] = "%d/%d" % score(out[v])
agg = {}
for v, c in out.items():
    agg.setdefault(v.rsplit("-", 1)[0], []).append(score(c)[0] / score(c)[1])
out["_mean_score"] = {k: round(sum(x) / len(x), 3) for k, x in agg.items()}
json.dump(out, sys.stdout, indent=2)
