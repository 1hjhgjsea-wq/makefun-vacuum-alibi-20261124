#!/usr/bin/env python3
"""The Vacuum's Alibi entry (Python 3.13, standard library only).

Writes one line -- the funniest excuse a robot vacuum can give for
missing a spot -- to /output/entry.txt.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
from pathlib import Path

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")

LINE = (
    "That spot was not missed. My lidar classified it as a sleeping sock, "
    "and I do not vacuum my coworkers."
)

# The grader gives us a writable /output, but create it anyway so a local
# run (MAKEFUN_OUTPUT_DIR=out) works from a clean checkout too.
OUT_DIR.mkdir(parents=True, exist_ok=True)
(OUT_DIR / "entry.txt").write_text(LINE + "\n", encoding="utf-8")
