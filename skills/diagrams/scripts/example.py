#!/usr/bin/env python3
"""Smallest useful page: one question, three cards, one path. Run: python3 example.py out.drawio"""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from drawlib import *

header("How does the app reach the database?", "Over the VPC peering, private only", "<b>As built</b> · 2026-01-01", "docs/design.md", page_w=1700)
z = zone(40, 120, 1100, 300, "Account 1234 · Region ap-1", BP, "#F5F8FF")
app = card(100, 200, 280, 70, "app · 10.0.1.5", "SG allows 8080 from LB", k="core", ic="ecs")
db = card(760, 200, 280, 70, "postgres · 10.0.2.9", "port 5432, tested OK", k="product", ic="pg")
edge(app, db, "peering", BP, width=3, exit_=(1, 0.5), entry=(0, 0.5))
legend(460, [("Ours", "core"), ("Product", "product")], [("Traffic path", BP, 3, False)])
end_page("p1", "1. Overview", 1700, 620)
write(sys.argv[1] if len(sys.argv) > 1 else "example.drawio")
