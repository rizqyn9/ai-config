#!/usr/bin/env python3
"""Static checks for every skill in skills/. Usage: python3 evals/static.py > dist/static.json"""
import json, os, re, sys
ROOT = os.path.join(os.path.dirname(__file__), "..", "skills")
res = []
for n in sorted(os.listdir(ROOT)):
    d = os.path.join(ROOT, n)
    if not os.path.isdir(d): continue
    f = os.path.join(d, "SKILL.md")
    r = {"skill": n, "checks": {}}
    if not os.path.exists(f):
        r["checks"]["has_SKILL.md"] = False; res.append(r); continue
    t = open(f).read()
    m = re.match(r"---\n(.*?)\n---\n(.*)", t, re.S)
    fm = dict(re.findall(r"^(\w[\w-]*):\s*(.+)$", m.group(1), re.M)) if m else {}
    body = m.group(2) if m else t
    c = r["checks"]
    c["frontmatter"] = bool(m)
    c["name_matches_folder"] = fm.get("name") == n.lstrip("_") or fm.get("name") == n
    c["description_has_when"] = bool(re.search(r"\b(use|when|before)\b", fm.get("description", ""), re.I))
    c["description_chars<=400"] = len(fm.get("description", "")) <= 400
    c["body_lines<=200"] = body.count("\n") <= 200
    refs = re.findall(r"`((?:scripts|references|assets)/[\w./-]+)`", body)
    c["referenced_files_exist"] = all(os.path.exists(os.path.join(d, x)) for x in refs)
    r["description_chars"] = len(fm.get("description", "")); r["body_lines"] = body.count("\n"); r["refs"] = refs
    r["template"] = n.startswith("_")
    res.append(r)
json.dump(res, sys.stdout, indent=2)
