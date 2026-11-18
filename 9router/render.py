#!/usr/bin/env python3
"""Render snapshot JSON into the small payloads apply.sh sends to 9router."""

import json
import sys

mode, path = sys.argv[1], sys.argv[2]
data = json.load(open(path, encoding="utf-8"))

if mode == "combos":
    for combo in data["combos"]:
        payload = {
            "name": combo["name"],
            "kind": combo.get("kind") or "llm",
            "models": combo["models"],
        }
        print(combo["name"], json.dumps(payload, ensure_ascii=False), sep="\t")
elif mode == "settings":
    keys = (
        "comboStrategy",
        "comboStickyRoundRobinLimit",
        "rtkEnabled",
        "ponytailEnabled",
        "ponytailLevel",
        "cavemanEnabled",
        "cavemanLevel",
        "requireApiKey",
        "requireLogin",
    )
    print(json.dumps({k: data[k] for k in keys if k in data}))
else:
    raise SystemExit(f"unknown mode: {mode}")
