#!/usr/bin/env python3
"""Recount funnel/VSL-script.md: spoken words per beat, running times at 150 words
a minute, and the word count of every cut. With --write it also updates the beat
headings, the shoot card (Time and Words columns) and the Runtime line."""
import re, sys
from pathlib import Path

F = Path(__file__).resolve().parent.parent / "funnel" / "VSL-script.md"
WPM = 150

def mmss(sec):
    sec = int(round(sec)); return "%d:%02d" % (sec // 60, sec % 60)

def parse(t):
    s = t[t.index("## The script"):t.index("## Proof to have in hand")]
    beats, cur = [], None
    for line in s.splitlines():
        m = re.match(r"### (\d+)\. (.*?)(?: \(\d+:\d\d-\d+:\d\d\))?$", line)
        if m:
            cur = {"n": int(m.group(1)), "title": m.group(2), "lines": []}; beats.append(cur)
        elif cur is not None and line.startswith(">") and line[1:].strip():
            cur["lines"].append(line[1:].strip())
    return beats

def cut_words(spec, beats):
    idx = {(b["n"], i + 1): l for b in beats for i, l in enumerate(b["lines"])}
    total, missing = 0, []
    for part in re.split(r",\s*", re.sub(r"\([^)]*\)", "", spec).strip().rstrip(".")):
        m = re.match(r"(\d+)\.(\d+)(?: to (\d+)\.(\d+))?$", part.strip())
        if not m: missing.append(part); continue
        b, a = int(m.group(1)), int(m.group(2)); z = int(m.group(4)) if m.group(4) else a
        for i in range(a, z + 1):
            if (b, i) in idx: total += len(idx[(b, i)].split())
            else: missing.append("%d.%d" % (b, i))
    return total - spec.count('trim the opening'), missing

def main():
    t = F.read_text(); beats = parse(t)
    total = sum(len(l.split()) for b in beats for l in b["lines"]); clock = 0.0
    for b in beats:
        b["words"] = sum(len(l.split()) for l in b["lines"])
        b["start"] = clock; clock += b["words"] * 60.0 / WPM; b["end"] = clock
        print("%2d  %-44s %4d words  %s-%s  (%d lines)" % (b["n"], b["title"][:44], b["words"], mmss(b["start"]), mmss(b["end"]), len(b["lines"])))
    print("TOTAL %d words, %s" % (total, mmss(clock)))
    cuts = t[t.index("## The two-minute cut"):t.index("## Hook variants")]
    for m in re.finditer(r"^- (\*\*[^*]+\*\*\s*)?((?:\d+\.\d+)[^\n]*)$", cuts, re.M):
        w, miss = cut_words(m.group(2), beats)
        print("cut %-28s -> %d words, %s%s" % ((m.group(1) or "two-minute cut").strip("* "), w, mmss(w * 60.0 / WPM), "  MISSING " + ",".join(miss) if miss else ""))
    over = [("%d.%d" % (b["n"], i + 1), len(l.split())) for b in beats for i, l in enumerate(b["lines"]) if len(l.split()) > 24]
    if over: print("lines over 24 words:", over)
    if "--write" in sys.argv:
        for b in beats:
            rng = "%s-%s" % (mmss(b["start"]), mmss(b["end"]))
            t = re.sub(r"^### %d\. .*$" % b["n"], "### %d. %s (%s)" % (b["n"], b["title"], rng), t, count=1, flags=re.M)
            t = re.sub(r"^\| %d \| ([^|]*) \| [^|]* \| [^|]* \|" % b["n"], lambda m: "| %d | %s | %s | %d |" % (b["n"], m.group(1), rng, b["words"]), t, count=1, flags=re.M)
        t = re.sub(r"^\*\*Runtime:\*\*.*$", "**Runtime:** about %s at 150 words a minute. %s spoken words (the \">\" lines only)." % (mmss(clock), format(total, ",")), t, count=1, flags=re.M)
        F.write_text(t); print("written")

main()
